# ODA Management Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#dcoc-content-body)

## ODA Management Functions

Package: DBMS_CLOUD_OCI_ODA_MANAGEMENT

### CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT Function

Starts an asynchronous job to move the specified ODA Private Endpoint into a different compartment. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_oda_private_endpoint_compartment_details`

(required) The compartment to which the Digital Assistant instance should be moved.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONFIGURE_DIGITAL_ASSISTANT_PARAMETERS Function

This will store the provided parameters in the Digital Assistant instance and update any Digital Assistants with matching parameters.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`configure_digital_assistant_parameters_details`

(required) The parameter values to use.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTHENTICATION_PROVIDER Function

Creates a new Authentication Provider

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_authentication_provider_details`

(required) Property values required to create the new Authentication Provider.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CHANNEL Function

Creates a new Channel.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_channel_details`

(required) Property values for creating the new Channel.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DIGITAL_ASSISTANT Function

Creates a new Digital Assistant.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_digital_assistant_details`

(required) Property values for creating the new Digital Assistant.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ODA_PRIVATE_ENDPOINT Function

Starts an asynchronous job to create an ODA Private Endpoint. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`create_oda_private_endpoint_details`

(required) Details for the new ODA Private Endpoint.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function

Starts an asynchronous job to create an ODA Private Endpoint Attachment. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`create_oda_private_endpoint_attachment_details`

(required) Details for the new ODA Private Endpoint Attachment.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function

Starts an asynchronous job to create an ODA Private Endpoint Scan Proxy. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`create_oda_private_endpoint_scan_proxy_details`

(required) Details for the new ODA Private Endpoint Scan Proxy.

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SKILL Function

Creates a new Skill from scratch.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_skill_details`

(required) Property values for creating the Skill.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SKILL_PARAMETER Function

Creates a new Skill Parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`create_skill_parameter_details`

(required) Property values for creating the new Skill Parameter.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TRANSLATOR Function

Creates a new Translator

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_translator_details`

(required) Property values to create the new Translator.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTHENTICATION_PROVIDER Function

Delete the specified Authentication Provider.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`authentication_provider_id`

(required) Unique Authentication Provider identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CHANNEL Function

Delete the specified Channel.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DIGITAL_ASSISTANT Function

Delete the specified Digital Assistant.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ODA_PRIVATE_ENDPOINT Function

Starts an asynchronous job to delete the specified ODA Private Endpoint. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function

Starts an asynchronous job to delete the specified ODA Private Endpoint Attachment. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of ODA Private Endpoint Attachment.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function

Starts an asynchronous job to delete the specified ODA Private Endpoint Scan Proxy. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_scan_proxy_id`

(required) Unique ODA Private Endpoint Scan Proxy identifier.

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SKILL Function

Delete the specified Skill.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SKILL_PARAMETER Function

Delete the specified Skill Parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`parameter_name`

(required) The name of a Skill Parameter.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TRANSLATOR Function

Delete the specified Translator.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`translator_id`

(required) Unique Translator identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_DIGITAL_ASSISTANT Function

Exports the specified Digital Assistant as an archive to Object Storage.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`export_digital_assistant_details`

(required) Where in Object Storage to export the Digital Assistant to.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_SKILL Function

Exports the specified Skill as an archive to Object Storage.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`export_skill_details`

(required) Where in Object Storage to export the Skill to.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTHENTICATION_PROVIDER Function

Gets the specified Authentication Provider.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`authentication_provider_id`

(required) Unique Authentication Provider identifier.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CHANNEL Function

Gets the specified Channel.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DIGITAL_ASSISTANT Function

Gets the specified Digital Assistant.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DIGITAL_ASSISTANT_PARAMETER Function

Gets the specified Digital Assistant Parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`parameter_name`

(required) The name of a Digital Assistant Parameter. This is unique with the Digital Assistant.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ODA_PRIVATE_ENDPOINT Function

Gets the specified ODA Private Endpoint.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function

Gets the specified ODA Private Endpoint Attachment.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of ODA Private Endpoint Attachment.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function

Gets the specified ODA Private Endpoint Scan Proxy.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_scan_proxy_id`

(required) Unique ODA Private Endpoint Scan Proxy identifier.

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SKILL Function

Gets the specified Skill.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SKILL_PARAMETER Function

Gets the specified Skill Parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`parameter_name`

(required) The name of a Skill Parameter.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRANSLATOR Function

Gets the specified Translator.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`translator_id`

(required) Unique Translator identifier.

`if_none_match`

(optional) The If-None-Match HTTP request header makes the request conditional. For GET methods, the service will return the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. When the condition fails for GET methods, then the service will return HTTP status code 304 (Not Modified).

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_BOT Function

Import a Bot archive from Object Storage.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`import_bot_details`

(required) Properties for where in Object Storage to import the Bot archive from.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTHENTICATION_PROVIDERS Function

Returns a page of Authentication Providers that belong to the specified Digital Assistant instance. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`id`

(optional) Unique Authentication Provider identifier.

`identity_provider`

(optional) List only Authentication Providers for this Identity Provider.

Allowed values are: 'GENERIC', 'OAM', 'GOOGLE', 'MICROSOFT'

`name`

(optional) List only the information for Authentication Providers with this name. Authentication Provider names are unique and may not change. Example: `MyProvider`

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`. The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'name', 'identityProvider'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CHANNELS Function

Returns a page of Channels that belong to the specified Digital Assistant instance. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`id`

(optional) Unique Channel identifier.

`name`

(optional) List only the information for Channels with this name. Channels names are unique and may not change. Example: `MyChannel`

`category`

(optional) List only Channels with this category.

Allowed values are: 'AGENT', 'APPLICATION', 'BOT', 'BOT_AS_AGENT', 'SYSTEM', 'EVENT'

`l_type`

(optional) List only Channels of this type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`. The default sort order for `timeCreated` and `timeUpdated` is descending, and the default sort order for `name` is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'name'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DIGITAL_ASSISTANT_PARAMETERS Function

Returns a page of Parameters that belong to the specified Digital Assistant. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`name`

(optional) List only Parameters with this name.

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `name`. The default sort order is ascending.

Allowed values are: 'name', 'displayName', 'type'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DIGITAL_ASSISTANTS Function

Returns a page of Digital Assistants that belong to the specified Digital Assistant instance. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`id`

(optional) Unique Digital Assistant identifier.

`category`

(optional) List only Bot resources with this category.

`name`

(optional) List only Bot resources with this name. Names are unique and may not change. Example: `MySkill`

`version`

(optional) List only Bot resources with this version. Versions are unique and may not change. Example: `1.0`

`namespace`

(optional) List only Bot resources with this namespace. Namespaces may not change. Example: `MyNamespace`

`platform_version`

(optional) List only Bot resources with this platform version.

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) List only Bot resources with this lifecycle details.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`. The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'name'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ODA_PRIVATE_ENDPOINT_ATTACHMENTS Function

Returns a page of ODA Instances attached to this ODA Private Endpoint. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of ODA Private Endpoint.

`compartment_id`

(required) List the ODA Private Endpoint Attachments that belong to this compartment.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`lifecycle_state`

(optional) List only the ODA Private Endpoint Attachments that are in this lifecycle state.

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ODA_PRIVATE_ENDPOINT_SCAN_PROXIES Function

Returns a page of ODA Private Endpoint Scan Proxies that belong to the specified ODA Private Endpoint. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) List only the ODA Private Endpoint Scan Proxies that are in this lifecycle state.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ODA_PRIVATE_ENDPOINTS Function

Returns a page of ODA Private Endpoints that belong to the specified compartment. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) List the ODA Private Endpoints that belong to this compartment.

`display_name`

(optional) List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change. Example: `My new resource`

`lifecycle_state`

(optional) List only the ODA Private Endpoints that are in this lifecycle state.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SKILL_PARAMETERS Function

Returns a page of Skill Parameters that belong to the specified Skill. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`name`

(optional) List only Parameters with this name.

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `name`. The default sort order is ascending.

Allowed values are: 'name', 'displayName', 'type'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SKILLS Function

Returns a page of Skills that belong to the specified Digital Assistant instance. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`id`

(optional) Unique Skill identifier.

`category`

(optional) List only Bot resources with this category.

`name`

(optional) List only Bot resources with this name. Names are unique and may not change. Example: `MySkill`

`version`

(optional) List only Bot resources with this version. Versions are unique and may not change. Example: `1.0`

`namespace`

(optional) List only Bot resources with this namespace. Namespaces may not change. Example: `MyNamespace`

`platform_version`

(optional) List only Bot resources with this platform version.

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) List only Bot resources with this lifecycle details.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`. The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'name'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRANSLATORS Function

Returns a page of Translators that belong to the specified Digital Assistant instance. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`id`

(optional) Unique Translator identifier.

`l_type`

(optional) List only Translators of this type.

Allowed values are: 'GOOGLE', 'MICROSOFT'

`name`

(optional) List only Translators with this name. Translator names are unique and may not change. Example: `MyTranslator`

`lifecycle_state`

(optional) List only the resources that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`. The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'name', 'type'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_DIGITAL_ASSISTANT Function

Publish a draft Digital Assistant. Once published the Digital Assistant cannot be modified.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_SKILL Function

Publish a draft Skill. Once published it cannot be modified.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_CHANNEL_KEYS Function

This will generate new keys for any generated keys in the Channel (eg. secretKey, verifyToken). If a Channel has no generated keys then no changes will be made. Ensure that you take note of the newly generated keys in the response as they will not be returned again.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_CHANNEL Function

Starts a Channel so that it will begin accepting messages.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_CHANNEL Function

Stops a Channel so that it will no longer accept messages.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTHENTICATION_PROVIDER Function

Updates the specified Authentication Provider with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`authentication_provider_id`

(required) Unique Authentication Provider identifier.

`update_authentication_provider_details`

(required) Property values to update the Authentication Provider.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CHANNEL Function

Updates the specified Channel with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`channel_id`

(required) Unique Channel identifier.

`update_channel_details`

(required) Property values to update the Channel.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DIGITAL_ASSISTANT Function

Updates the specified Digital Assistant with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`update_digital_assistant_details`

(required) Property values to update the Digital Assistant.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DIGITAL_ASSISTANT_PARAMETER Function

Updates the specified Digital Assistant Parameter with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`digital_assistant_id`

(required) Unique Digital Assistant identifier.

`parameter_name`

(required) The name of a Digital Assistant Parameter. This is unique with the Digital Assistant.

`update_digital_assistant_parameter_details`

(required) Property values to update the Digital Assistant Parameter.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ODA_PRIVATE_ENDPOINT Function

Starts an asynchronous job to update the specified ODA Private Endpoint with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_private_endpoint_id`

(required) Unique ODA Private Endpoint identifier which is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_oda_private_endpoint_details`

(required) The information to update.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SKILL Function

Updates the specified Skill with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`update_skill_details`

(required) Property values to update the Skill.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SKILL_PARAMETER Function

Updates the specified Skill Parameter with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`skill_id`

(required) Unique Skill identifier.

`parameter_name`

(required) The name of a Skill Parameter.

`update_skill_parameter_details`

(required) Property values to update the Skill Parameter.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TRANSLATOR Function

Updates the specified Translator with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`translator_id`

(required) Unique Translator identifier.

`update_translator_details`

(required) Property values to update the Translator.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [ODA Management Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-89A36A5C-601F-4C14-8CA1-54A3A41E4E7B)
- [CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-BDAAEA4E-8535-480E-BC73-04D172FF591D)
- [CONFIGURE_DIGITAL_ASSISTANT_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A6D38D32-0FC6-4A31-9A88-EA7AB53ACC9A)
- [CREATE_AUTHENTICATION_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-5D888E6D-5D4F-4D0A-8942-B04DBCBE0651)
- [CREATE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-91AC932C-9F7E-4C3F-90C3-3901401D64F6)
- [CREATE_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-5C9AE10C-F8F5-4BAE-A659-51A8C2AFF652)
- [CREATE_ODA_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-5DB8AF4F-E425-4593-9CCA-05A6EDB46D4D)
- [CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-800BFAA4-4A6A-4E76-9386-6966D0811ACE)
- [CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3E34C9BE-5B47-4702-BD02-A0E275CCD634)
- [CREATE_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-5ABB5C9E-D4CF-43B9-9384-3229FB5391DA)
- [CREATE_SKILL_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-0BA42482-7517-4A01-AC41-7C1FAC4CDF49)
- [CREATE_TRANSLATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-8FC32543-D518-4525-B295-3AD04840A6CC)
- [DELETE_AUTHENTICATION_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-51B5CC30-3693-4663-A68C-501C1E877D88)
- [DELETE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-17E59DE4-0B57-4FA2-9F2E-0FA0F8F3EC8A)
- [DELETE_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-048F894A-E6AF-4BD4-90E9-E4D0AEF3D771)
- [DELETE_ODA_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-956C044E-018C-4BFC-8714-34BB81B28E98)
- [DELETE_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-12086207-8E34-416C-8EEA-DCE9699ED7CE)
- [DELETE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-07C63117-7335-4E69-AAED-13BAF69C2684)
- [DELETE_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-D0249D66-9404-4862-8B7D-6280F47EF2CB)
- [DELETE_SKILL_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3A6642B6-4D31-4956-BFFA-46197FC77B49)
- [DELETE_TRANSLATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-4DB4F330-CA6C-43A0-B1C4-4B60B0749B0A)
- [EXPORT_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3A15F6D4-AE15-42E6-8063-0C1730483750)
- [EXPORT_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-BBBCE64F-FC90-49F1-B5CA-BE1D2F90466F)
- [GET_AUTHENTICATION_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A1FF4C98-393E-438B-BF8C-7FB3746B71C3)
- [GET_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-F3E52F18-78EB-41DF-ACB2-51F8C15CF5A8)
- [GET_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-EF0B4295-F62D-4D26-A17D-83B810FE5F34)
- [GET_DIGITAL_ASSISTANT_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-D309903E-9F56-40AB-9F36-73227E0F6B00)
- [GET_ODA_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-505FFA0A-022F-4894-A58C-7B128E211100)
- [GET_ODA_PRIVATE_ENDPOINT_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-6B9A10C2-097F-46EC-AA16-5EE2DADE5F79)
- [GET_ODA_PRIVATE_ENDPOINT_SCAN_PROXY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-7EB00FD5-0E44-44F2-873C-0E81F246ED81)
- [GET_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-4E132AA8-3D08-4BB8-A507-4FA00FC11AD5)
- [GET_SKILL_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-DEA96BA4-4C2A-456C-B64E-00712F3D8C3F)
- [GET_TRANSLATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3EB7D9BC-C9FF-46B6-BC7C-34D058E35114)
- [IMPORT_BOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-5715A94C-3FFE-45CB-9A49-D2EADF885AB6)
- [LIST_AUTHENTICATION_PROVIDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-FB30E3A2-A8B5-4FA2-8F22-6156333A3FA8)
- [LIST_CHANNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3DE20B8E-2123-483E-B667-05F026FC54C2)
- [LIST_DIGITAL_ASSISTANT_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-02D86712-8747-475E-A170-0EC43DC2BAD7)
- [LIST_DIGITAL_ASSISTANTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-146661E1-3185-4BC9-9C8F-D27B15197E04)
- [LIST_ODA_PRIVATE_ENDPOINT_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-FB9CA856-2D08-44FA-A34D-215D7EAD3087)
- [LIST_ODA_PRIVATE_ENDPOINT_SCAN_PROXIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-48E78435-001C-451B-9514-182F4E72A808)
- [LIST_ODA_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-05F1E8D0-D0FF-4884-8CCD-5D951F421070)
- [LIST_SKILL_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-95E63CF3-C29F-447C-BB4D-279C12F7F29A)
- [LIST_SKILLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A754095C-321B-4A12-A461-07EA66768050)
- [LIST_TRANSLATORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-58DADEB5-EB58-46A1-8123-904EDCE470AF)
- [PUBLISH_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-35985ECB-9D3B-4EF8-BC80-2065088DCCB5)
- [PUBLISH_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-551BDF94-12D9-4B2B-AB35-8E4CA59B3AAB)
- [ROTATE_CHANNEL_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-DECD2DC2-90F5-4FD7-94FE-2619FBE20F3E)
- [START_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A7868E84-499F-4C7F-8CFA-CD3658C7E492)
- [STOP_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A2769181-724A-4A8B-93FC-0D0592840F7A)
- [UPDATE_AUTHENTICATION_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-ED32BBD6-8899-445E-A9AA-7FF2468D863D)
- [UPDATE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3B6E2E4E-7B95-460C-BB17-7AE93487AD07)
- [UPDATE_DIGITAL_ASSISTANT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-3D9A4667-DF50-4035-A36D-A2629599CA73)
- [UPDATE_DIGITAL_ASSISTANT_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-78D4A4C6-3E79-46FB-922A-EE35E5BA28AB)
- [UPDATE_ODA_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-A149F26A-E67C-4713-8301-3FADCE43EDE7)
- [UPDATE_SKILL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-6753E295-3987-4DA2-998C-C47A387AC561)
- [UPDATE_SKILL_PARAMETER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-0F764149-85EA-46E6-9B95-798712D4ABC8)
- [UPDATE_TRANSLATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_management.html#ADSDK-GUID-67D04FD0-F39D-4F5D-9ED6-ACAA410DD7E8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
