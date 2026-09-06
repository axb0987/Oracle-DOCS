# DNS Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#dcoc-content-body)

## DNS Functions

Package: DBMS_CLOUD_OCI_DNS_DNS

### CHANGE_RESOLVER_COMPARTMENT Function

Moves a resolver into a different compartment along with its protected default view and any endpoints. Zones in the default view are not moved. VCN-dedicated resolvers are initially created in the same compartment as their corresponding VCN, but can then be moved to a different compartment.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`change_resolver_compartment_details`

(required) Details for moving a resolver, along with its protected default view and endpoints, into a different compartment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_STEERING_POLICY_COMPARTMENT Function

Moves a steering policy into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_id`

(required) The OCID of the target steering policy.

`change_steering_policy_compartment_details`

(required) Details for moving a steering policy into a different compartment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TSIG_KEY_COMPARTMENT Function

Moves a TSIG key into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`tsig_key_id`

(required) The OCID of the target TSIG key.

`change_tsig_key_compartment_details`

(required) Details for moving a TSIG key into a different compartment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VIEW_COMPARTMENT Function

Moves a view into a different compartment. To change the compartment of a protected view, change the compartment of its corresponding resolver.

Syntax
```

```

Parameters

Parameter Description

`view_id`

(required) The OCID of the target view.

`change_view_compartment_details`

(required) Details for moving a view into a different compartment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ZONE_COMPARTMENT Function

Moves a zone into a different compartment. Protected zones cannot have their compartment changed. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. **Note:** All SteeringPolicyAttachment objects associated with this zone will also be moved into the provided compartment.

Syntax
```

```

Parameters

Parameter Description

`zone_id`

(required) The OCID of the target zone.

`change_zone_compartment_details`

(required) Details for moving a zone into a different compartment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RESOLVER_ENDPOINT Function

Creates a new resolver endpoint in the same compartment as the resolver.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`create_resolver_endpoint_details`

(required) Details for creating a new resolver endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STEERING_POLICY Function

Creates a new steering policy in the specified compartment. For more information on creating policies with templates, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm).

Syntax
```

```

Parameters

Parameter Description

`create_steering_policy_details`

(required) Details for creating a new steering policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STEERING_POLICY_ATTACHMENT Function

Creates a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain. For the purposes of access control, the attachment is automatically placed into the same compartment as the domain's zone.

Syntax
```

```

Parameters

Parameter Description

`create_steering_policy_attachment_details`

(required) Details for creating a new steering policy attachment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TSIG_KEY Function

Creates a new TSIG key in the specified compartment. There is no `opc-retry-token` header since TSIG key names must be globally unique.

Syntax
```

```

Parameters

Parameter Description

`create_tsig_key_details`

(required) Details for creating a new TSIG key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIEW Function

Creates a new view in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_view_details`

(required) Details for creating a new view.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ZONE Function

Creates a new zone in the specified compartment. Private zones must have a zone type of `PRIMARY`. Creating a private zone at or under `oraclevcn.com` within the default protected view of a VCN-dedicated resolver is not permitted.

Syntax
```

```

Parameters

Parameter Description

`create_zone_details`

(required) Details for creating a new zone.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ZONE_FROM_ZONE_FILE Function

Creates a new zone from a zone file in the specified compartment. Not supported for private zones.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`create_zone_from_zone_file_details`

(required) The zone file contents.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DOMAIN_RECORDS Function

Deletes all records at the specified zone and domain. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RR_SET Function

Deletes all records in the specified RRSet. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`rtype`

(required) The type of the target RRSet within the target zone.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RESOLVER_ENDPOINT Function

Deletes the specified resolver endpoint. Note that attempting to delete a resolver endpoint in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the API. Resolver endpoints may not be deleted if they are referenced by a resolver rule.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`resolver_endpoint_name`

(required) The name of the target resolver endpoint.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STEERING_POLICY Function

Deletes the specified steering policy. A `204` response indicates that the delete has been successful. Deletion will fail if the policy is attached to any zones. To detach a policy from a zone, see `DeleteSteeringPolicyAttachment`.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_id`

(required) The OCID of the target steering policy.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STEERING_POLICY_ATTACHMENT Function

Deletes the specified steering policy attachment. A `204` response indicates that the delete has been successful.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_attachment_id`

(required) The OCID of the target steering policy attachment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TSIG_KEY Function

Deletes the specified TSIG key.

Syntax
```

```

Parameters

Parameter Description

`tsig_key_id`

(required) The OCID of the target TSIG key.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIEW Function

Deletes the specified view. Note that attempting to delete a view in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API. Views cannot be deleted if they are referenced by non-deleted zones or resolvers. Protected views cannot be deleted.

Syntax
```

```

Parameters

Parameter Description

`view_id`

(required) The OCID of the target view.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ZONE Function

Deletes the specified zone and all its steering policy attachments. A `204` response indicates that the zone has been successfully deleted. Protected zones cannot be deleted. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DOMAIN_RECORDS Function

Gets a list of all records at the specified zone and domain. The results are sorted by `rtype` in alphabetical order by default. You can optionally filter and/or sort the results using the listed parameters. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`zone_version`

(optional) The version of the zone for which data is requested.

`rtype`

(optional) Search by record type. Will match any record whose[type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4)(case-insensitive) equals the provided value.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`sort_by`

(optional) The field by which to sort records.

Allowed values are: 'rtype', 'ttl'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RR_SET Function

Gets a list of all records in the specified RRSet. The results are sorted by `recordHash` by default. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`rtype`

(required) The type of the target RRSet within the target zone.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`zone_version`

(optional) The version of the zone for which data is requested.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESOLVER Function

Gets information about a specific resolver. Note that attempting to get a resolver in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESOLVER_ENDPOINT Function

Gets information about a specific resolver endpoint. Note that attempting to get a resolver endpoint in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`resolver_endpoint_name`

(required) The name of the target resolver endpoint.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STEERING_POLICY Function

Gets information about the specified steering policy.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_id`

(required) The OCID of the target steering policy.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STEERING_POLICY_ATTACHMENT Function

Gets information about the specified steering policy attachment.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_attachment_id`

(required) The OCID of the target steering policy attachment.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TSIG_KEY Function

Gets information about the specified TSIG key.

Syntax
```

```

Parameters

Parameter Description

`tsig_key_id`

(required) The OCID of the target TSIG key.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIEW Function

Gets information about a specific view. Note that attempting to get a view in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`view_id`

(required) The OCID of the target view.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ZONE Function

Gets information about the specified zone, including its creation date, zone type, and serial. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ZONE_CONTENT Function

Gets the requested zone's zone file.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ZONE_RECORDS Function

Gets all records in the specified zone. The results are sorted by `domain` in alphabetical order by default. For more information about records, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4). When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`if_modified_since`

(optional) The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value. Transfer of the selected representation's data is avoided if that data has not changed.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`zone_version`

(optional) The version of the zone for which data is requested.

`domain`

(optional) Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.

`domain_contains`

(optional) Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.

`rtype`

(optional) Search by record type. Will match any record whose[type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4)(case-insensitive) equals the provided value.

`sort_by`

(optional) The field by which to sort records.

Allowed values are: 'domain', 'rtype', 'ttl'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOLVER_ENDPOINTS Function

Gets a list of all endpoints within a resolver. The collection can be filtered by name or lifecycle state. It can be sorted on creation time or name both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include resolver endpoints in the DELETED lifecycle state to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`name`

(optional) The name of a resource.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field by which to sort resolver endpoints.

Allowed values are: 'name', 'timeCreated'

`lifecycle_state`

(optional) The state of a resource.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOLVERS Function

Gets a list of all resolvers within a compartment. The collection can be filtered by display name, id, or lifecycle state. It can be sorted on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include resolvers in the DELETED lifecycleState to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`display_name`

(optional) The displayName of a resource.

`id`

(optional) The OCID of a resource.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field by which to sort resolvers.

Allowed values are: 'displayName', 'timeCreated'

`lifecycle_state`

(optional) The state of a resource.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STEERING_POLICIES Function

Gets a list of all steering policies in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`id`

(optional) The OCID of a resource.

`display_name`

(optional) The displayName of a resource.

`display_name_contains`

(optional) The partial displayName of a resource. Will match any resource whose name (case-insensitive) contains the provided value.

`health_check_monitor_id`

(optional) Search by health check monitor OCID. Will match any resource whose health check monitor ID matches the provided value.

`time_created_greater_than_or_equal_to`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created on or after the indicated time.

`time_created_less_than`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created before the indicated time.

`template`

(optional) Search by steering template type. Will match any resource whose template type matches the provided value.

`lifecycle_state`

(optional) The state of a resource.

`sort_by`

(optional) The field by which to sort steering policies. If unspecified, defaults to `timeCreated`.

Allowed values are: 'displayName', 'timeCreated', 'template'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STEERING_POLICY_ATTACHMENTS Function

Lists the steering policy attachments in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`id`

(optional) The OCID of a resource.

`display_name`

(optional) The displayName of a resource.

`steering_policy_id`

(optional) Search by steering policy OCID. Will match any resource whose steering policy ID matches the provided value.

`zone_id`

(optional) Search by zone OCID. Will match any resource whose zone ID matches the provided value.

`domain`

(optional) Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.

`domain_contains`

(optional) Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.

`time_created_greater_than_or_equal_to`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created on or after the indicated time.

`time_created_less_than`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created before the indicated time.

`lifecycle_state`

(optional) The state of a resource.

`sort_by`

(optional) The field by which to sort steering policy attachments. If unspecified, defaults to `timeCreated`.

Allowed values are: 'displayName', 'timeCreated', 'domainName'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TSIG_KEYS Function

Gets a list of all TSIG keys in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`id`

(optional) The OCID of a resource.

`name`

(optional) The name of a resource.

`lifecycle_state`

(optional) The state of a resource.

`sort_by`

(optional) The field by which to sort TSIG keys. If unspecified, defaults to `timeCreated`.

Allowed values are: 'name', 'timeCreated'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIEWS Function

Gets a list of all views within a compartment. The collection can be filtered by display name, id, or lifecycle state. It can be sorted on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include views in the DELETED lifecycleState to be consistent with other operations of the API.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`display_name`

(optional) The displayName of a resource.

`id`

(optional) The OCID of a resource.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field by which to sort views.

Allowed values are: 'displayName', 'timeCreated'

`lifecycle_state`

(optional) The state of a resource.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ZONE_TRANSFER_SERVERS Function

Gets a list of IP addresses of OCI nameservers for inbound and outbound transfer of zones in the specified compartment (which must be the root compartment of a tenancy) that transfer zone data with external master or downstream nameservers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ZONES Function

Gets a list of all zones in the specified compartment. The collection can be filtered by name, time created, scope, associated view, and zone type. Filtering by view is only supported for private zones.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment the resource belongs to.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a page of the collection.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`name`

(optional) A case-sensitive filter for zone names. Will match any zone with a name that equals the provided value.

`name_contains`

(optional) Search by zone name. Will match any zone whose name (case-insensitive) contains the provided value.

`zone_type`

(optional) Search by zone type, `PRIMARY` or `SECONDARY`. Will match any zone whose type equals the provided value.

Allowed values are: 'PRIMARY', 'SECONDARY'

`time_created_greater_than_or_equal_to`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created on or after the indicated time.

`time_created_less_than`

(optional) An[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)timestamp that states all returned resources were created before the indicated time.

`lifecycle_state`

(optional) The state of a resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`sort_by`

(optional) The field by which to sort zones.

Allowed values are: 'name', 'zoneType', 'timeCreated'

`sort_order`

(optional) The order to sort the resources.

Allowed values are: 'ASC', 'DESC'

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`tsig_key_id`

(optional) Search for zones that are associated with a TSIG key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_DOMAIN_RECORDS Function

Updates records in the specified zone at a domain. You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`patch_domain_records_details`

(required) Operations describing how to modify the collection of records.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_RR_SET Function

Updates records in the specified RRSet. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`rtype`

(required) The type of the target RRSet within the target zone.

`patch_rr_set_details`

(required) Operations describing how to modify the collection of records.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_ZONE_RECORDS Function

Updates a collection of records in the specified zone. You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`patch_zone_records_details`

(required) The operations describing how to modify the collection of records.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DOMAIN_RECORDS Function

Replaces records in the specified zone at a domain with the records specified in the request body. If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`update_domain_records_details`

(required) A full list of records for the domain.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RR_SET Function

Replaces records in the specified RRSet. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`domain`

(required) The target fully-qualified domain name (FQDN) within the target zone.

`rtype`

(required) The type of the target RRSet within the target zone.

`update_rr_set_details`

(required) A full list of records for the RRSet.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RESOLVER Function

Updates the specified resolver with your new information.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`update_resolver_details`

(required) New data for the resolver.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RESOLVER_ENDPOINT Function

Updates the specified resolver endpoint with your new information.

Syntax
```

```

Parameters

Parameter Description

`resolver_id`

(required) The OCID of the target resolver.

`resolver_endpoint_name`

(required) The name of the target resolver endpoint.

`update_resolver_endpoint_details`

(required) New data for the resolver endpoint.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STEERING_POLICY Function

Updates the configuration of the specified steering policy.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_id`

(required) The OCID of the target steering policy.

`update_steering_policy_details`

(required) New data for the steering policy.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STEERING_POLICY_ATTACHMENT Function

Updates the specified steering policy attachment with your new information.

Syntax
```

```

Parameters

Parameter Description

`steering_policy_attachment_id`

(required) The OCID of the target steering policy attachment.

`update_steering_policy_attachment_details`

(required) New data for the steering policy attachment.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TSIG_KEY Function

Updates the specified TSIG key.

Syntax
```

```

Parameters

Parameter Description

`tsig_key_id`

(required) The OCID of the target TSIG key.

`update_tsig_key_details`

(required) New data for the TSIG key.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIEW Function

Updates the specified view with your new information.

Syntax
```

```

Parameters

Parameter Description

`view_id`

(required) The OCID of the target view.

`update_view_details`

(required) New data for the view.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ZONE Function

Updates the zone with the specified information. Global secondary zones may have their external masters updated. For more information about secondary zones, see[Manage DNS Service Zone](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm). When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`update_zone_details`

(required) New data for the zone.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ZONE_RECORDS Function

Replaces records in the specified zone with the records specified in the request body. If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

Syntax
```

```

Parameters

Parameter Description

`zone_name_or_id`

(required) The name or OCID of the target zone.

`update_zone_records_details`

(required) A full list of records for the zone.

`if_match`

(optional) The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.

`if_unmodified_since`

(optional) The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value. This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`scope`

(optional) Specifies to operate only on resources that have a matching DNS scope.

Allowed values are: 'GLOBAL', 'PRIVATE'

`view_id`

(optional) The OCID of the view the resource is associated with.

`compartment_id`

(optional) The OCID of the compartment the zone belongs to. This parameter is deprecated and should be omitted.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dns.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [DNS Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-029097E3-5D2D-42A8-9602-06EB93361B61)
- [CHANGE_RESOLVER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-394B9CAE-3812-4265-90CE-EE6D9A07EA88)
- [CHANGE_STEERING_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-C6773514-502D-44A4-AF40-B8AC8541E24C)
- [CHANGE_TSIG_KEY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-A7C2E82C-C24E-414A-9BEF-AD920C99F332)
- [CHANGE_VIEW_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-02E65314-8CA3-476E-B37C-039C024D5891)
- [CHANGE_ZONE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-7B8B519F-888C-4C92-90C5-C83F9981947F)
- [CREATE_RESOLVER_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-C6CE2D32-0A4E-41C6-93C7-4EEC206C3362)
- [CREATE_STEERING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-E96DEEBB-BFBE-4CDC-8EF7-B48DE5A50693)
- [CREATE_STEERING_POLICY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-6D25FD53-9318-4302-BFA1-84E0C0353F27)
- [CREATE_TSIG_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-41BBB9F0-1412-4868-A6E8-28F11A2BBC79)
- [CREATE_VIEW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-EE7CFA00-835D-45A4-9762-A7CF73898E6E)
- [CREATE_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-FDBC1EE9-F479-4D53-845A-6D65B42EE5C0)
- [CREATE_ZONE_FROM_ZONE_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-15C831C5-62B8-45C8-9961-2072972B027B)
- [DELETE_DOMAIN_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-09C2A660-271A-4694-BDC7-7A904B2F8C02)
- [DELETE_RR_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-6D769E14-9CDF-4EBC-90C9-7E2ABAEFE3C4)
- [DELETE_RESOLVER_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-24B6405D-9209-45FE-A17D-B8B7160BBCBE)
- [DELETE_STEERING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-9EFE7D0F-2E19-4905-8B68-74EC45E2F22E)
- [DELETE_STEERING_POLICY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-BEBAFF6D-CDDE-4B36-97F4-F55D68D469A9)
- [DELETE_TSIG_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-2CCA3182-68DE-4743-AE90-2779D81C06F0)
- [DELETE_VIEW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-530AA8D4-0E74-4D35-A4CE-ACC1B5ADCAF1)
- [DELETE_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-59082B3B-5CB6-48D5-8D44-616C8A6FD6D7)
- [GET_DOMAIN_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-CF991F6D-0157-472F-8C96-488A953B4723)
- [GET_RR_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-E603F64A-21FE-4D92-AFD9-C7523365A5BF)
- [GET_RESOLVER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-B0B98189-E3A0-4E12-AEF7-CCFBC0602E24)
- [GET_RESOLVER_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-7EBEBAC3-0E99-4618-A4F4-FDBDE344E927)
- [GET_STEERING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-B748B0E5-6AEB-41E9-9D8F-492763CADE58)
- [GET_STEERING_POLICY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-AD4BCB90-1E62-461E-BC8A-79FAA6F81D7D)
- [GET_TSIG_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-2CC4DEDF-CEDB-424B-9B56-2478063CBA69)
- [GET_VIEW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-ECBB6B8D-1BF6-4304-BD50-0566FB03DF35)
- [GET_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-AD988B8C-F9B9-4381-997B-789C91BF4292)
- [GET_ZONE_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-0618F13E-7143-4E22-96D9-1BEAEC0895E6)
- [GET_ZONE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-C03B708E-BE57-49F3-AD0C-ACDA668A6E93)
- [LIST_RESOLVER_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-170DC29C-392E-437B-8347-1D0A34412D42)
- [LIST_RESOLVERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-899C5E92-81F1-4CAB-97D1-A32131C52C36)
- [LIST_STEERING_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-C1E4604F-4E51-49EF-A64F-60AB21D31DA9)
- [LIST_STEERING_POLICY_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-43ABCC2C-9681-4EA8-8912-A504CF7134C3)
- [LIST_TSIG_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-E12A387B-36D4-43AD-99EC-F9EB2A1F1781)
- [LIST_VIEWS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-D6101AD3-9025-4EDD-A84E-75C05C2DF5B8)
- [LIST_ZONE_TRANSFER_SERVERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-D9A01C3C-A091-432C-A7CF-19769124AA7D)
- [LIST_ZONES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-FD3B48E4-43BD-4FD8-B87D-12E2E74D2800)
- [PATCH_DOMAIN_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-4B17218E-A13C-4B62-8FCC-688876ED0DBB)
- [PATCH_RR_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-D1123080-E9E0-4E19-90C9-EB15D7F828A5)
- [PATCH_ZONE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-5E0E258D-6DA5-44BB-BD6D-F761B2883F2A)
- [UPDATE_DOMAIN_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-151A803A-41B9-4C0C-AF74-A71F977E5D6B)
- [UPDATE_RR_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-960FE66D-FDDC-4BFD-8D7C-D7772C957C10)
- [UPDATE_RESOLVER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-36B3195D-FE04-4FF0-81FC-4D2ABDDCF1C8)
- [UPDATE_RESOLVER_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-13DE1B69-255F-470C-A42B-7173143B345D)
- [UPDATE_STEERING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-5DF19C82-C593-4A74-BEEF-D02F2183C2DA)
- [UPDATE_STEERING_POLICY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-23BA9D4D-C5E8-4939-95F5-6A318DE2E3BD)
- [UPDATE_TSIG_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-0537841A-889C-4FEC-8F1F-28385F77D00B)
- [UPDATE_VIEW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-FCEAE940-EDC5-428A-A56C-B51C86F96670)
- [UPDATE_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-860B56CA-82CA-47C2-837D-9BBBC343D430)
- [UPDATE_ZONE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dns_dns.html#ADSDK-GUID-D9B9F7A7-B01C-4BD3-A099-6E1408C80CA3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
