# Network Firewall Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#dcoc-content-body)

## Network Firewall Functions

Package: DBMS_CLOUD_OCI_NF_NETWORK_FIREWALL

### APPLY_NETWORK_FIREWALL_POLICY Function

Applies the candidate version of the NetworkFirewallPolicy resource. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`apply_network_firewall_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_ADDRESS_LISTS Function

Creates a new Address Lists at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_address_lists_details`

(required) Request Details to create the Address Lists for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_APPLICATION_GROUPS Function

Creates a new Application Group at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_application_groups_details`

(required) Request Details to create the Application Group for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_APPLICATIONS Function

Creates new Applications at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_applications_details`

(required) Request Details to create the Applications for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_DECRYPTION_PROFILES Function

Creates new Decryption Profiles at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_decryption_profiles_details`

(required) Request Details to create the Decryption Profile for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_DECRYPTION_RULES Function

Creates Decryption Rules at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_decryption_rules_details`

(required) Request Details to create the Decryption Rule for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_MAPPED_SECRETS Function

Creates new Mapped Secrets at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_mapped_secrets_details`

(required) Request Details to create the Mapped Secret for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_SECURITY_RULES Function

Creates a new Security Rule at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_security_rules_details`

(required) Request Details to create the Security Rule for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_SERVICE_LISTS Function

Creates a new Service List at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_service_lists_details`

(required) Request Details to create the Service List for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_SERVICES Function

Creates new Services at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_services_details`

(required) Request Details to create the Services for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_UPLOAD_URL_LISTS Function

Creates a new Url Lists at bulk for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`bulk_upload_url_lists_details`

(required) Request Details to create the Url Lists for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancel work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NETWORK_FIREWALL_COMPARTMENT Function

Moves a NetworkFirewall resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`change_network_firewall_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NETWORK_FIREWALL_POLICY_COMPARTMENT Function

Moves a NetworkFirewallPolicy resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`change_network_firewall_policy_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CLONE_NETWORK_FIREWALL_POLICY Function

Moves a NetworkFirewallPolicy resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`clone_network_firewall_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ADDRESS_LIST Function

Creates a new Address List for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_address_list_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION Function

Creates a new Application for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_application_details`

(required) Request Details to create the Application for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION_GROUP Function

Creates a new ApplicationGroup for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_application_group_details`

(required) Request Details to create the ApplicationGroup for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DECRYPTION_PROFILE Function

Creates a new Decryption Profile for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_decryption_profile_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DECRYPTION_RULE Function

Creates a new Decryption Rule for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_decryption_rule_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MAPPED_SECRET Function

Creates a new Mapped Secret for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_mapped_secret_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NETWORK_FIREWALL Function

Creates a new NetworkFirewall.

Syntax
```

```

Parameters

Parameter Description

`create_network_firewall_details`

(required) Details for the new NetworkFirewall.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NETWORK_FIREWALL_POLICY Function

Creates a new Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`create_network_firewall_policy_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SECURITY_RULE Function

Creates a new Security Rule for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_security_rule_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE Function

Creates a new Service for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_service_details`

(required) Request Details to create the Service for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_LIST Function

Creates a new ServiceList for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_service_list_details`

(required) Request Details to create the ServiceList for the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_URL_LIST Function

Creates a new Url List for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`create_url_list_details`

(required) Request Details to create the Network Firewall Policy Resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ADDRESS_LIST Function

Deletes a Address List resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`address_list_name`

(required) Unique identifier for address lists.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION Function

Deletes a Application resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_name`

(required) Unique identifier for Applications.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION_GROUP Function

Deletes a ApplicationGroup resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_group_name`

(required) Unique name identifier for Application Lists in the scope of Network Firewall Policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DECRYPTION_PROFILE Function

Deletes a Decryption Profile resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_profile_name`

(required) Unique identifier for Decryption Profiles.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DECRYPTION_RULE Function

Deletes a Decryption Rule resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_rule_name`

(required) Unique identifier for Decryption Rules in the network firewall policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MAPPED_SECRET Function

Deletes a Mapped Secret resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`mapped_secret_name`

(required) Unique identifier for Mapped Secrets.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NETWORK_FIREWALL Function

Deletes a NetworkFirewall resource by identifier

Syntax
```

```

Parameters

Parameter Description

`network_firewall_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NETWORK_FIREWALL_POLICY Function

Deletes a NetworkFirewallPolicy resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SECURITY_RULE Function

Deletes a Security Rule resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`security_rule_name`

(required) Unique identifier for Security Rules in the network firewall policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE Function

Deletes a Service resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_name`

(required) Unique identifier for Services.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_LIST Function

Deletes a ServiceList resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_list_name`

(required) Unique name identifier for Service Lists in the scope of Network Firewall Policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_URL_LIST Function

Deletes a Url List resource with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`url_list_name`

(required) Unique name identifier for url lists in the scope of Network Firewall Policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ADDRESS_LIST Function

Get Address List by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`address_list_name`

(required) Unique identifier for address lists.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION Function

Get Application by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_name`

(required) Unique identifier for Applications.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION_GROUP Function

Get ApplicationGroup by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_group_name`

(required) Unique name identifier for Application Lists in the scope of Network Firewall Policy.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DECRYPTION_PROFILE Function

Get Decryption Profile by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_profile_name`

(required) Unique identifier for Decryption Profiles.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DECRYPTION_RULE Function

Get Decryption Rule by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_rule_name`

(required) Unique identifier for Decryption Rules in the network firewall policy.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MAPPED_SECRET Function

Get Mapped Secret by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`mapped_secret_name`

(required) Unique identifier for Mapped Secrets.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_FIREWALL Function

Gets a NetworkFirewall by identifier

Syntax
```

```

Parameters

Parameter Description

`network_firewall_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_FIREWALL_POLICY Function

Gets a NetworkFirewallPolicy given the network firewall policy identifier.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_RULE Function

Get Security Rule by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`security_rule_name`

(required) Unique identifier for Security Rules in the network firewall policy.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE Function

Get Service by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_name`

(required) Unique identifier for Services.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_LIST Function

Get ServiceList by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_list_name`

(required) Unique name identifier for Service Lists in the scope of Network Firewall Policy.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_URL_LIST Function

Get Url List by the given name in the context of network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`url_list_name`

(required) Unique name identifier for url lists in the scope of Network Firewall Policy.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDRESS_LISTS Function

Returns a list of Network Firewall Policies.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATION_GROUPS Function

Returns a list of ApplicationGroups for the policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATIONS Function

Returns a list of Applications for the policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DECRYPTION_PROFILES Function

Returns a list of Decryption Profile for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DECRYPTION_RULES Function

Returns a list of Decryption Rule for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`decryption_rule_priority_order`

(optional) Unique priority order for Decryption Rules in the network firewall policy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MAPPED_SECRETS Function

Returns a list of Mapped Secret for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_FIREWALL_POLICIES Function

Returns a list of Network Firewall Policies.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return only resources with a lifecycleState matching the given value.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_FIREWALLS Function

Returns a list of NetworkFirewalls.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`network_firewall_policy_id`

(optional) A filter to return only resources that match the entire networkFirewallPolicyId given.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`availability_domain`

(optional) A filter to return only resources that are present within the specified availability domain. To get a list of availability domains for a tenancy, use`LIST_AVAILABILITY_DOMAINS`Function operation. Example: `kIdk:PHX-AD-1`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return only resources with a lifecycleState matching the given value.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_RULES Function

Returns a list of Security Rule for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`security_rule_priority_order`

(optional) Unique priority order for Security Rules in the network firewall policy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_LISTS Function

Returns a list of ServiceLists for the policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICES Function

Returns a list of Services for the policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_URL_LISTS Function

Returns a list of URL lists for the Network Firewall Policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`work_request_id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MIGRATE_NETWORK_FIREWALL_POLICY Function

Moves a NetworkFirewallPolicy resource from one version to latest version. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ADDRESS_LIST Function

Updates the Address list with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`address_list_name`

(required) Unique identifier for address lists.

`update_address_list_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPLICATION Function

Updates the Application with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_name`

(required) Unique identifier for Applications.

`update_application_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPLICATION_GROUP Function

Updates the ApplicationGroup with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`application_group_name`

(required) Unique name identifier for Application Lists in the scope of Network Firewall Policy.

`update_application_group_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DECRYPTION_PROFILE Function

Updates the Decryption Profile with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_profile_name`

(required) Unique identifier for Decryption Profiles.

`update_decryption_profile_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DECRYPTION_RULE Function

Updates the Decryption Rule with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`decryption_rule_name`

(required) Unique identifier for Decryption Rules in the network firewall policy.

`update_decryption_rule_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MAPPED_SECRET Function

Updates the Mapped Secret with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`mapped_secret_name`

(required) Unique identifier for Mapped Secrets.

`update_mapped_secret_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_FIREWALL Function

Updates the NetworkFirewall

Syntax
```

```

Parameters

Parameter Description

`network_firewall_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`update_network_firewall_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_FIREWALL_POLICY Function

Updates the NetworkFirewallPolicy

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`update_network_firewall_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_RULE Function

Updates the Security Rule with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`security_rule_name`

(required) Unique identifier for Security Rules in the network firewall policy.

`update_security_rule_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SERVICE Function

Updates the Service with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_name`

(required) Unique identifier for Services.

`update_service_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SERVICE_LIST Function

Updates the ServiceList with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`service_list_name`

(required) Unique name identifier for Service Lists in the scope of Network Firewall Policy.

`update_service_list_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_URL_LIST Function

Updates the Url list with the given name in the network firewall policy.

Syntax
```

```

Parameters

Parameter Description

`network_firewall_policy_id`

(required) Unique Network Firewall Policy identifier

`url_list_name`

(required) Unique name identifier for url lists in the scope of Network Firewall Policy.

`update_url_list_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-firewall.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Network Firewall Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-C783A5E9-E6BC-434F-8123-61450D7EAFC6)
- [APPLY_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-E1195C0E-B76A-4A90-AB0C-C3B8F8CF2587)
- [BULK_UPLOAD_ADDRESS_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-8BEF3C07-803E-4746-8C77-4DC0D872D5CD)
- [BULK_UPLOAD_APPLICATION_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-1A0D856F-AFDD-4011-8E94-C3AB3BED7032)
- [BULK_UPLOAD_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-D879673A-71C1-411F-8885-D518EEAEEC05)
- [BULK_UPLOAD_DECRYPTION_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-80D543E4-CCC2-4BC1-A9E3-D309CE2D34A0)
- [BULK_UPLOAD_DECRYPTION_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-F68AA63F-B80A-42E8-A43B-6D4F2F4F87B5)
- [BULK_UPLOAD_MAPPED_SECRETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-2AFE13E3-8335-48B8-B5BD-48AF97B8E0A9)
- [BULK_UPLOAD_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-4CFD0CD6-E6F8-4109-9719-195433A480A5)
- [BULK_UPLOAD_SERVICE_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-18581E7D-606C-472B-BA81-51CC95C08C6C)
- [BULK_UPLOAD_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-855E8C6D-8EB9-46C9-BE43-238BF5CD662C)
- [BULK_UPLOAD_URL_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-8C035352-A532-4392-A0F1-C82634628BF3)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-3C2EDCAC-A0C9-47E1-A74C-16C13D9837DF)
- [CHANGE_NETWORK_FIREWALL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-9C9C8158-4C50-4582-A043-1BCEEE70AE23)
- [CHANGE_NETWORK_FIREWALL_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-56327BD5-D482-41FB-A3F0-9D25561F2AB2)
- [CLONE_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-BED9843A-64AC-43D8-BA9C-718AE299A1F7)
- [CREATE_ADDRESS_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-0B802311-BF68-4695-A8EC-59E369780305)
- [CREATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-3ED1CB82-EE59-4BC4-A12E-BDFA79770A1C)
- [CREATE_APPLICATION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-ED243ED9-F1A3-49CE-A82F-9C237224E359)
- [CREATE_DECRYPTION_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-A88501DC-3010-4115-AD84-EF4D511DD3A3)
- [CREATE_DECRYPTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-8A5A9567-66B2-45F9-9EA9-860882E4F8FB)
- [CREATE_MAPPED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-3E996815-21D3-40D3-BE58-F4B076485FFC)
- [CREATE_NETWORK_FIREWALL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-52270F6D-6FC6-4C4C-B7FC-8A9B465DDA36)
- [CREATE_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-BA6BF87F-DC65-468B-A7AB-1EABD6FF3763)
- [CREATE_SECURITY_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-5A15F2C3-3F44-4974-8B20-B581FC629817)
- [CREATE_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-C6BBCA0C-1762-42DE-B490-E059829A8D95)
- [CREATE_SERVICE_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7326FB71-9E33-4FE4-A24E-26D517249503)
- [CREATE_URL_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-C7705E6F-C5B9-45D2-ACBA-C94F8936E581)
- [DELETE_ADDRESS_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-E4134B95-E36C-4EAF-AB46-3FC9B801964D)
- [DELETE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-DB7869B4-AE22-447A-9986-4E837FEF6381)
- [DELETE_APPLICATION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-2919622E-1EE1-47F5-9063-7267F445DA93)
- [DELETE_DECRYPTION_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-89668EF9-4116-488F-8DB6-71FCBF9897E7)
- [DELETE_DECRYPTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-958D59FC-052D-417B-9FFE-8B1C0BEA1C17)
- [DELETE_MAPPED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-01C48CD8-D85D-4CF6-B8F8-9C67C82DDF1F)
- [DELETE_NETWORK_FIREWALL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7983FEB0-AD53-4BC5-9D3E-81004FBAD438)
- [DELETE_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-3EB88674-C893-402D-A777-7F721638547E)
- [DELETE_SECURITY_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-F1F73B71-5005-4ACB-BD58-F7AAD0F7130A)
- [DELETE_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-5B3A1E98-7F27-43CA-B298-91AFBA4ABEB0)
- [DELETE_SERVICE_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-31508D7B-7D9F-4BDB-88E8-02CA52E3D8B3)
- [DELETE_URL_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-AAF838A9-8CDA-4E85-AC54-4C52C24160BD)
- [GET_ADDRESS_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-D96D6A80-0E87-4E64-8EA6-98D03FF4527F)
- [GET_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-AC4E575A-D625-423C-B93A-B50AB454936A)
- [GET_APPLICATION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-5B92A8DA-6F4A-45B9-8CE0-CE9AF873968C)
- [GET_DECRYPTION_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-E8746FA8-C0F8-47AA-824A-9A1155DAD425)
- [GET_DECRYPTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-AD4E3056-6317-4DB0-8BE3-449297333D40)
- [GET_MAPPED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-1CEF215F-EC14-4E7E-8417-119A381AF960)
- [GET_NETWORK_FIREWALL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7BE93D60-D841-458D-8858-B054CB6E9FE9)
- [GET_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-A7AF6692-B335-4A16-8273-4BF8CB3926C3)
- [GET_SECURITY_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-75F843A0-10B0-4669-A5AB-23640AEE89A5)
- [GET_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-C73B2EE9-EFB5-427B-A517-A4D10A8FBDD8)
- [GET_SERVICE_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-32D9D7A7-D75D-4C2F-BA7E-90C6B97C93FD)
- [GET_URL_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-ED8FAAD2-B298-4C96-A777-A8CDED8FD141)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-09FB07D2-21EA-4BC8-92DF-14288641471F)
- [LIST_ADDRESS_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-481CF3FB-0F7B-4C23-BD73-A9401A353CC1)
- [LIST_APPLICATION_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-41B481DC-AF4E-4128-9BDA-6AD018302950)
- [LIST_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-139D875D-CD48-4939-946B-0119BD34C8A3)
- [LIST_DECRYPTION_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7726DB06-509B-4A2F-A082-1AE4B17409C3)
- [LIST_DECRYPTION_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-956F4445-5AED-4D33-A05F-FD476B5D941D)
- [LIST_MAPPED_SECRETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-9007B6B9-73E4-4170-AF42-2D4C7F15A853)
- [LIST_NETWORK_FIREWALL_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-688806FC-9AE9-489E-8398-4C2BD9DF161E)
- [LIST_NETWORK_FIREWALLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-2FDED9A5-8611-463C-B961-5BE15D8C868C)
- [LIST_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-EE2298D8-060B-461F-A3DD-6F4F10E0F413)
- [LIST_SERVICE_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-D480E093-0B94-48F5-9C34-1F2B352917AD)
- [LIST_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-5007CB51-B05B-412A-B121-87F53242037B)
- [LIST_URL_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-0CBEA427-F815-4A38-91D0-D07D4EB7F90A)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-300C55CA-1E19-4F87-AD01-F55E9233FC3B)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-F83AB21C-CA27-4833-BF8B-7957C7EF807E)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-738B444B-8CE8-4219-ADB5-2DAB7D85B309)
- [MIGRATE_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-00C6165A-BB93-4DD6-A811-90F52DB43509)
- [UPDATE_ADDRESS_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7658DAC7-3400-4DCE-89E1-4BEB782C0868)
- [UPDATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-D9439AD8-46FC-4F54-B385-A0DFB8EC4F19)
- [UPDATE_APPLICATION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-6437069A-0522-431B-A328-0D008679B179)
- [UPDATE_DECRYPTION_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-3858B58C-3F56-4C10-8608-EA067DA03F6E)
- [UPDATE_DECRYPTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-50A0AB65-B81E-47B1-BF65-16C7245F9C55)
- [UPDATE_MAPPED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-DF4E84C4-F3A9-461A-AD3D-794D5D8D43E3)
- [UPDATE_NETWORK_FIREWALL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7A1A373C-C662-436F-8014-035791F7D505)
- [UPDATE_NETWORK_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-68D2079E-8FCC-41BD-A539-5512CBF8B3F8)
- [UPDATE_SECURITY_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-F2E72CFB-CA17-499F-808B-F6EBBE299A8F)
- [UPDATE_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-F660C500-525E-4BC3-BC15-2E2A91C36F81)
- [UPDATE_SERVICE_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-7EE9D888-9E5E-410A-B311-DEC1C9700DB8)
- [UPDATE_URL_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nf_network_firewall.html#ADSDK-GUID-DA092213-FFFC-4460-B3FB-AF5C3FF7942D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
