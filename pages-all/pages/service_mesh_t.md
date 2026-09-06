# Service Mesh Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#dcoc-content-body)

## Service Mesh Common Types

### DBMS_CLOUD_OCI_SERVICE_MESH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_LOGGING_CONFIGURATION_T Type

This configuration determines if logging is enabled and where the logs will be output.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Determines if the logging configuration is enabled.

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_TARGET_T Type

Target of the access policy. This can either be the source or the destination of the traffic.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Traffic type of the target.

Allowed values are: 'ALL_VIRTUAL_SERVICES', 'VIRTUAL_SERVICE', 'EXTERNAL_SERVICE', 'INGRESS_GATEWAY'

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_T Type

Access policy rule.

Syntax
```

```

Fields

Field Description

`action`

(required) Action for the traffic between the source and the destination.

Allowed values are: 'ALLOW'

`source`

(required)

`destination`

(required)

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_access_policy_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_T Type

Access policies enable administrators to restrict the access of certain services.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mesh_id`

(optional) The OCID of the service mesh in which this access policy is created.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`rules`

(optional) List of applicable rules.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_SUMMARY_T Type

Summary of the access policy.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`mesh_id`

(optional) The OCID of the service mesh in which this access policy is created.

`lifecycle_state`

(required) The current state of the access policy.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_access_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_COLLECTION_T Type

Results of an access policy search. Contains both AccessPolicySummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of access policies.

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_TARGET_DETAILS_T Type

Target of the access policy. This can either be the source or the destination of the traffic.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Traffic type of the target.

Allowed values are: 'ALL_VIRTUAL_SERVICES', 'VIRTUAL_SERVICE', 'EXTERNAL_SERVICE', 'INGRESS_GATEWAY'

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_DETAILS_T Type

Access policy rule.

Syntax
```

```

Fields

Field Description

`action`

(required) Action for the traffic between the source and the destination.

Allowed values are: 'ALLOW'

`source`

(required)

`destination`

(required)

### DBMS_CLOUD_OCI_SERVICE_MESH_ALL_VIRTUAL_SERVICES_ACCESS_POLICY_TARGET_T Type

An internal virtual service directs traffic to all virtual services in a mesh using this target type or vice versa.

Syntax
```

```

`dbms_cloud_oci_service_mesh_all_virtual_services_access_policy_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_ALL_VIRTUAL_SERVICES_ACCESS_POLICY_TARGET_DETAILS_T Type

An internal virtual service directs traffic to all virtual services in a mesh using this target type or vice versa.

Syntax
```

```

`dbms_cloud_oci_service_mesh_all_virtual_services_access_policy_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_details_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_CA_BUNDLE_T Type

Resource representing the CA bundle.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of certificate.

Allowed values are: 'OCI_CERTIFICATES', 'LOCAL_FILE'

### DBMS_CLOUD_OCI_SERVICE_MESH_CERTIFICATE_AUTHORITY_T Type

A certificate authority resource to use for creating leaf certificates.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the certificate authority resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_ACCESS_POLICY_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_INGRESS_GATEWAY_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_INGRESS_GATEWAY_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_MESH_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_DEPLOYMENT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_SERVICE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_SERVICE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_access_policy_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_ACCESS_POLICY_DETAILS_T Type

The information about a new access policy.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mesh_id`

(required) The OCID of the service mesh in which this access policy is created.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`rules`

(required) List of applicable rules

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_TLS_CERTIFICATE_T Type

Resource representing the location of the TLS certificate.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of certificate.

Allowed values are: 'OCI_CERTIFICATES', 'LOCAL_FILE'

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_LISTENER_CLIENT_VALIDATION_CONFIG_T Type

Resource representing the TLS configuration used for validating client certificates.

Syntax
```

```

Fields

Field Description

`trusted_ca_bundle`

(optional)

`subject_alternate_names`

(optional) A list of alternate names to verify the subject identity in the certificate presented by the client.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_LISTENER_TLS_CONFIG_T Type

TLS enforcement config for the ingress listener.

Syntax
```

```

Fields

Field Description

`l_mode`

(required) DISABLED: Connection can only be plaintext. PERMISSIVE: Connection can be either plaintext or TLS/mTLS. If the clientValidation.trustedCaBundle property is configured for the listener, mTLS is performed and the client's certificates are validated by the gateway. TLS: Connection can only be TLS. MUTUAL_TLS: Connection can only be MTLS.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'TLS', 'MUTUAL_TLS'

`server_certificate`

(optional)

`client_validation`

(optional)

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_LISTENER_T Type

Listener configuration.

Syntax
```

```

Fields

Field Description

`protocol`

(required) Type of protocol used.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP'

`port`

(required) Port on which ingress gateway is listening.

`tls`

(optional)

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_LISTENER_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_listener_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_T Type

Host for the ingress listener.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name for the host. The name must be unique within the same ingress gateway. This name can be used in the ingress gateway route table resource to attach a route to this host. Example: `MyExampleHost`

`hostnames`

(optional) Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".

`listeners`

(required) The listeners for the ingress gateway.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_MUTUAL_TRANSPORT_LAYER_SECURITY_DETAILS_T Type

Mutual TLS settings used when sending requests to virtual services within the mesh.

Syntax
```

```

Fields

Field Description

`maximum_validity`

(optional) The number of days the mTLS certificate is valid. This value should be less than the Maximum Validity Duration for Certificates (Days) setting on the Certificate Authority associated with this Mesh. The certificate will be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days will be renewed every 30 days.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_host_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_INGRESS_GATEWAY_DETAILS_T Type

The information about a new IngressGateway.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mesh_id`

(required) The OCID of the service mesh in which this ingress gateway is created.

`hosts`

(required) An array of hostnames and their listener configuration that this gateway will bind to.

`access_logging`

(optional)

`mtls`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_REF_T Type

The ingress gateway host to which the route rule attaches. If not specified, the route rule gets attached to all hosts on the ingress gateway.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the ingress gateway host that this route should apply to.

`port`

(optional) The port of the ingress gateway host listener. Leave empty to match all ports for the host.

### DBMS_CLOUD_OCI_SERVICE_MESH_TRAFFIC_RULE_TARGET_DETAILS_T Type

Target of the traffic router rule.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the traffic target.

Allowed values are: 'VIRTUAL_DEPLOYMENT', 'VIRTUAL_SERVICE'

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_DETAILS_T Type

Traffic router target for an ingress gateway.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_service_traffic_rule_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_traffic_rule_target_details_t`type.

Fields

Field Description

`virtual_service_id`

(required) The OCID of the virtual service where the request will be routed.

`port`

(optional) The port on the virtual service to target. Mandatory if the virtual deployments are listening on multiple ports.

`weight`

(optional) Weight of traffic target.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_traffic_rule_target_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming ingress gateway traffic to a virtual service.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of protocol.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP'

`ingress_gateway_host`

(optional)

`destinations`

(required) The destination of the request.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_INGRESS_GATEWAY_ROUTE_TABLE_DETAILS_T Type

The information about a new IngressGatewayRouteTable.

Syntax
```

```

Fields

Field Description

`ingress_gateway_id`

(required) The OCID of the service mesh in which this access policy is created.

`name`

(required) A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`route_rules`

(required) The route rules for the ingress gateway.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_MESH_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type

Sets a minimum level of mTLS authentication for all virtual services within the mesh.

Syntax
```

```

Fields

Field Description

`minimum`

(required) DISABLED: No minimum virtual services within this mesh can use any mTLS authentication mode. PERMISSIVE: Virtual services within this mesh can use either PERMISSIVE or STRICT modes. STRICT: All virtual services within this mesh must use STRICT mode.

### DBMS_CLOUD_OCI_SERVICE_MESH_CERTIFICATE_AUTHORITY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_certificate_authority_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_MESH_DETAILS_T Type

The information about a new Mesh.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information. Example: `My new resource`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`certificate_authorities`

(required) The OCID of the certificate authority resource OCID to use for creating leaf certificates.

`mtls`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_SERVICE_DISCOVERY_CONFIGURATION_T Type

Service Discovery configuration for virtual deployments.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of service discovery.

Allowed values are: 'DNS', 'DISABLED'

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_LISTENER_T Type

Listener configuration for a virtual deployment.

Syntax
```

```

Fields

Field Description

`protocol`

(required) Type of protocol used in virtual deployment.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP', 'HTTP2', 'GRPC'

`port`

(required) Port in which virtual deployment is running.

`request_timeout_in_ms`

(optional) The maximum duration in milliseconds for the deployed service to respond to an incoming request through the listener. If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP/HTTP2 listeners, and disabled (no timeout) for the GRPC listeners. The value 0 (zero) indicates that the timeout is disabled. The timeout cannot be configured for the TCP and TLS_PASSTHROUGH listeners. For streaming responses from the deployed service, consider either keeping the timeout disabled or set a sufficiently high value.

`idle_timeout_in_ms`

(optional) The maximum duration in milliseconds for which the request's stream may be idle. The value 0 (zero) indicates that the timeout is disabled.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_LISTENER_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_deployment_listener_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_DEPLOYMENT_DETAILS_T Type

The information about a new VirtualDeployment.

Syntax
```

```

Fields

Field Description

`virtual_service_id`

(required) The OCID of the service mesh in which this access policy is created.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`service_discovery`

(optional)

`listeners`

(optional) The listeners for the virtual deployment.

`access_logging`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_DEFAULT_VIRTUAL_SERVICE_ROUTING_POLICY_T Type

Routing policy for the virtual service.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the virtual service routing policy.

Allowed values are: 'UNIFORM', 'DENY'

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_MUTUAL_TRANSPORT_LAYER_SECURITY_DETAILS_T Type

The mTLS authentication mode to use when receiving requests from other virtual services or ingress gateways within the mesh.

Syntax
```

```

Fields

Field Description

`maximum_validity`

(optional) The number of days the mTLS certificate is valid. This value should be less than the Maximum Validity Duration for Certificates (Days) setting on the Certificate Authority associated with this Mesh. The certificate will be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days will be renewed every 30 days.

`l_mode`

(required) DISABLED: Connection is not tunneled. PERMISSIVE: Connection can be either plaintext or an mTLS tunnel. STRICT: Connection is an mTLS tunnel. Clients without a valid certificate will be rejected.

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_SERVICE_DETAILS_T Type

The information about the new VirtualService.

Syntax
```

```

Fields

Field Description

`mesh_id`

(required) The OCID of the service mesh in which this virtual service is created.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`default_routing_policy`

(optional)

`hosts`

(optional) The DNS hostnames of the virtual service that is used by its callers. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\". Can be omitted if the virtual service will only have TCP virtual deployments.

`mtls`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_DETAILS_T Type

Traffic router target for a virtual service version.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_deployment_traffic_rule_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_traffic_rule_target_details_t`type.

Fields

Field Description

`virtual_deployment_id`

(required) The OCID of the virtual deployment where the request will be routed.

`port`

(optional) Port on virtual deployment to target. If port is missing, the rule will target all ports on the virtual deployment.

`weight`

(required) Weight of traffic target.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_deployment_traffic_rule_target_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming virtual service traffic to a version.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of protocol.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP'

`destinations`

(required) The destination of the request.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_SERVICE_ROUTE_TABLE_DETAILS_T Type

The information about the new VirtualServiceRouteTable.

Syntax
```

```

Fields

Field Description

`virtual_service_id`

(required) The OCID of the service mesh in which this access policy is created.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`route_rules`

(required) The route rules for the virtual service.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_DISABLED_SERVICE_DISCOVERY_CONFIGURATION_T Type

Disabled service discovery configuration for virtual deployments.

Syntax
```

```

`dbms_cloud_oci_service_mesh_disabled_service_discovery_configuration_t`is a subtype of the`dbms_cloud_oci_service_mesh_service_discovery_configuration_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_DNS_SERVICE_DISCOVERY_CONFIGURATION_T Type

DNS-based service discovery configuration for virtual deployments.

Syntax
```

```

`dbms_cloud_oci_service_mesh_dns_service_discovery_configuration_t`is a subtype of the`dbms_cloud_oci_service_mesh_service_discovery_configuration_t`type.

Fields

Field Description

`hostname`

(required) The hostname of the virtual deployments.

### DBMS_CLOUD_OCI_SERVICE_MESH_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_SERVICE_MESH_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_EXTERNAL_SERVICE_ACCESS_POLICY_TARGET_T Type

External service target that internal virtual services direct traffic to.

Syntax
```

```

`dbms_cloud_oci_service_mesh_external_service_access_policy_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_t`type.

Fields

Field Description

`hostnames`

(optional) The hostnames of the external service. Only applicable for HTTP and HTTPS protocols. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\", \"*\". Hostname \"*\" can be used to allow all hosts.

`ip_addresses`

(optional) The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol. All requests matching the given CIDR notation will pass through. In case a wildcard CIDR \"0.0.0.0/0\" is provided, the same port cannot be used for a virtual service communication.

`ports`

(optional) Ports exposed by an external service. If left empty all ports will be allowed.

`protocol`

(optional) Protocol of the external service

Allowed values are: 'HTTP', 'HTTPS', 'TCP'

### DBMS_CLOUD_OCI_SERVICE_MESH_EXTERNAL_SERVICE_ACCESS_POLICY_TARGET_DETAILS_T Type

External service target that internal virtual services direct traffic to.

Syntax
```

```

`dbms_cloud_oci_service_mesh_external_service_access_policy_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_details_t`type.

Fields

Field Description

`hostnames`

(optional) The hostnames of the external service. Only applicable for HTTP and HTTPS protocols. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\", \"*\". Hostname \"*\" can be used to allow all hosts.

`ip_addresses`

(optional) The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol. All requests matching the given CIDR notation will pass through. In case a wildcard CIDR \"0.0.0.0/0\" is provided, the same port cannot be used for a virtual service communication.

`ports`

(optional) Ports exposed by an external service. If left empty all ports will be allowed.

`protocol`

(optional) Protocol of the external service

Allowed values are: 'HTTP', 'HTTPS', 'TCP'

### DBMS_CLOUD_OCI_SERVICE_MESH_TRAFFIC_RULE_TARGET_T Type

Target of the traffic router rule.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the traffic target.

Allowed values are: 'VIRTUAL_DEPLOYMENT', 'VIRTUAL_SERVICE'

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_T Type

Traffic router target for an ingress gateway.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_service_traffic_rule_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_traffic_rule_target_t`type.

Fields

Field Description

`virtual_service_id`

(optional) The OCID of the virtual service where the request will be routed.

`port`

(optional) The port on the virtual service to target. Mandatory if the virtual deployments are listening on multiple ports.

`weight`

(optional) Weight of traffic target.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_traffic_rule_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming ingress gateway traffic to a virtual service.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of protocol.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP'

`ingress_gateway_host`

(optional)

`destinations`

(required) The destination of the request.

### DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming ingress gateway traffic with HTTP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_http_ingress_gateway_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_t`type.

Fields

Field Description

`path`

(optional) Route to match

`path_type`

(optional) Match type for the route

Allowed values are: 'PREFIX'

`is_grpc`

(optional) If true, the rule will check that the content-type header has a application/grpc or one of the various application/grpc+ values.

`is_host_rewrite_enabled`

(optional) If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.

`is_path_rewrite_enabled`

(optional) If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.

`request_timeout_in_ms`

(optional) The maximum duration in milliseconds for the upstream service to respond to a request. If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true. The value 0 (zero) indicates that the timeout is disabled. For streaming responses from the upstream service, consider either keeping the timeout disabled or set a sufficiently high value.

### DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming ingress gateway traffic with HTTP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_http_ingress_gateway_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_details_t`type.

Fields

Field Description

`path`

(optional) Route to match

`path_type`

(optional) Match type for the route

Allowed values are: 'PREFIX'

`is_grpc`

(optional) If true, the rule will check that the content-type header has a application/grpc or one of the various application/grpc+ values.

`is_host_rewrite_enabled`

(optional) If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.

`is_path_rewrite_enabled`

(optional) If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.

`request_timeout_in_ms`

(optional) The maximum duration in milliseconds for the upstream service to respond to a request. If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true. The value 0 (zero) indicates that the timeout is disabled. For streaming responses from the upstream service, consider either keeping the timeout disabled or set a sufficiently high value.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_T Type

Traffic router target for a virtual service version.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_deployment_traffic_rule_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_traffic_rule_target_t`type.

Fields

Field Description

`virtual_deployment_id`

(optional) The OCID of the virtual deployment where the request will be routed.

`port`

(optional) Port on virtual deployment to target. If port is missing, the rule will target all ports on the virtual deployment.

`weight`

(required) Weight of traffic target.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_deployment_traffic_rule_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming virtual service traffic to a version.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of protocol.

Allowed values are: 'HTTP', 'TLS_PASSTHROUGH', 'TCP'

`destinations`

(required) The destination of the request.

### DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming Virtual Service traffic with HTTP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_http_virtual_service_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_t`type.

Fields

Field Description

`path`

(optional) Route to match

`path_type`

(optional) Match type for the route

Allowed values are: 'PREFIX'

`is_grpc`

(optional) If true, the rule will check that the content-type header has a application/grpc or one of the various application/grpc+ values.

`request_timeout_in_ms`

(optional) The maximum duration in milliseconds for the target service to respond to a request. If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true. The value 0 (zero) indicates that the timeout is disabled. For streaming responses from the target service, consider either keeping the timeout disabled or set a sufficiently high value.

### DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming Virtual Service traffic with HTTP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_http_virtual_service_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_details_t`type.

Fields

Field Description

`path`

(optional) Route to match

`path_type`

(optional) Match type for the route

Allowed values are: 'PREFIX'

`is_grpc`

(optional) If true, the rule will check that the content-type header has a application/grpc or one of the various application/grpc+ values.

`request_timeout_in_ms`

(optional) The maximum duration in milliseconds for the target service to respond to a request. If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true. The value 0 (zero) indicates that the timeout is disabled. For streaming responses from the target service, consider either keeping the timeout disabled or set a sufficiently high value.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type

Mutual TLS settings used when sending requests to virtual services within the mesh.

Syntax
```

```

Fields

Field Description

`certificate_id`

(required) The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.

`maximum_validity`

(optional) The number of days the mTLS certificate is valid. This value should be less than the Maximum Validity Duration for Certificates (Days) setting on the Certificate Authority associated with this Mesh. The certificate will be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days will be renewed every 30 days.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_T Type

An ingress gateway allows resources that are outside of a mesh to communicate to resources that are inside the mesh. It sits on the edge of a service mesh receiving incoming HTTP/TCP connections to the mesh.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mesh_id`

(required) The OCID of the service mesh in which this ingress gateway is created.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`hosts`

(optional) Array of hostnames and their listener configuration that this gateway will bind to.

`mtls`

(optional)

`access_logging`

(optional)

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ACCESS_POLICY_TARGET_T Type

Ingress gateway target that virtual services in mesh receive traffic from.

Syntax
```

```

`dbms_cloud_oci_service_mesh_ingress_gateway_access_policy_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_t`type.

Fields

Field Description

`ingress_gateway_id`

(optional) The OCID of the ingress gateway resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ACCESS_POLICY_TARGET_DETAILS_T Type

Ingress gateway target that virtual services in mesh receive traffic from.

Syntax
```

```

`dbms_cloud_oci_service_mesh_ingress_gateway_access_policy_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_details_t`type.

Fields

Field Description

`ingress_gateway_id`

(required) The OCID of the ingress gateway resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_SUMMARY_T Type

Summary of the IngressGateway.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`mesh_id`

(required) The OCID of the service mesh in which this ingress gateway is created.

`lifecycle_state`

(required) The current state of the IngressGateway.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_COLLECTION_T Type

Results of an ingressGateway search. Contains both IngressGatewaySummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of IngressGateway objects.

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_T Type

This resource represents a customer-managed ingress gateway route table in the Service Mesh.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`ingress_gateway_id`

(required) The OCID of the ingress gateway.

`name`

(required) A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. A lower value means a higher priority. The routes are declared based on the priority.

`route_rules`

(optional) The route rules for the ingress gateway.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_SUMMARY_T Type

Summary of the IngressGatewayRouteTable.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`ingress_gateway_id`

(required) The OCID of the ingress gateway.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the ingress gateway.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_ingress_gateway_route_table_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_COLLECTION_T Type

Results of a serviceMesh search. Contains both IngressGatewayRouteTableSummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ingress gateway route tables.

### DBMS_CLOUD_OCI_SERVICE_MESH_LOCAL_FILE_CA_BUNDLE_T Type

CA Bundle from the filesystem.

Syntax
```

```

`dbms_cloud_oci_service_mesh_local_file_ca_bundle_t`is a subtype of the`dbms_cloud_oci_service_mesh_ca_bundle_t`type.

Fields

Field Description

`secret_name`

(optional) Name of the secret. For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt. For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt

### DBMS_CLOUD_OCI_SERVICE_MESH_LOCAL_FILE_TLS_CERTIFICATE_T Type

TLS certificate from the filesystem.

Syntax
```

```

`dbms_cloud_oci_service_mesh_local_file_tls_certificate_t`is a subtype of the`dbms_cloud_oci_service_mesh_tls_certificate_t`type.

Fields

Field Description

`secret_name`

(optional) Name of the secret. For Kubernetes this is the name of the Kubernetes secret of type tls. For other platforms the secrets must be mounted at: /etc/oci/secrets/${secretName}/tls.{key,crt}

### DBMS_CLOUD_OCI_SERVICE_MESH_MESH_T Type

The mesh resource is the top-level container that represents the logical boundary of application traffic between the services and deployments that reside within it. A mesh also provides a unit of access control.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information. Example: `My new resource`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`certificate_authorities`

(optional) A list of certificate authority resources to use for creating leaf certificates for mTLS authentication. Currently we only support one certificate authority, but this may expand in future releases. Request with more than one certificate authority will be rejected.

`mtls`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_MESH_SUMMARY_T Type

Summary of the Mesh.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information. Example: `My new resource`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mtls`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Mesh.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_MESH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_mesh_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_MESH_COLLECTION_T Type

Results of a Mesh search. Contains both MeshSummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Mesh objects.

### DBMS_CLOUD_OCI_SERVICE_MESH_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type

Mutual TLS settings used when communicating with other virtual services or ingress gateways within the mesh.

Syntax
```

```

Fields

Field Description

`certificate_id`

(required) The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.

`maximum_validity`

(optional) The number of days the mTLS certificate is valid. This value should be less than the Maximum Validity Duration for Certificates (Days) setting on the Certificate Authority associated with this Mesh. The certificate will be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days will be renewed every 30 days.

`l_mode`

(required) DISABLED: Connection is not tunneled. PERMISSIVE: Connection can be either plaintext or an mTLS tunnel. STRICT: Connection is an mTLS tunnel. Clients without a valid certificate will be rejected.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'STRICT'

### DBMS_CLOUD_OCI_SERVICE_MESH_OCI_CA_BUNDLE_T Type

CA Bundle from OCI Certificates service.

Syntax
```

```

`dbms_cloud_oci_service_mesh_oci_ca_bundle_t`is a subtype of the`dbms_cloud_oci_service_mesh_ca_bundle_t`type.

Fields

Field Description

`ca_bundle_id`

(optional) The OCID of the CA Bundle resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_OCI_TLS_CERTIFICATE_T Type

TLS certificate from OCI Certificates service.

Syntax
```

```

`dbms_cloud_oci_service_mesh_oci_tls_certificate_t`is a subtype of the`dbms_cloud_oci_service_mesh_tls_certificate_t`type.

Fields

Field Description

`certificate_id`

(optional) The OCID of the leaf certificate resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_PROXY_DETAILS_T Type

Details of the proxy such as version of the proxy image.

Syntax
```

```

Fields

Field Description

`proxy_image`

(required) Proxy container image version to be deployed.

### DBMS_CLOUD_OCI_SERVICE_MESH_TCP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming ingress gateway traffic with TCP protocol.

Syntax
```

```

`dbms_cloud_oci_service_mesh_tcp_ingress_gateway_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TCP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming ingress gateway traffic with TCP protocol.

Syntax
```

```

`dbms_cloud_oci_service_mesh_tcp_ingress_gateway_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_details_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TCP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming Virtual Service traffic with TCP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_tcp_virtual_service_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TCP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming Virtual Service traffic with TCP protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_tcp_virtual_service_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_details_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming ingress gateway traffic with TCP protocol.

Syntax
```

```

`dbms_cloud_oci_service_mesh_tls_passthrough_ingress_gateway_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming ingress gateway traffic with TCP protocol.

Syntax
```

```

`dbms_cloud_oci_service_mesh_tls_passthrough_ingress_gateway_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_ingress_gateway_traffic_route_rule_details_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type

Rule for routing incoming Virtual Service traffic with TLS_PASSTHROUGH protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_tls_passthrough_virtual_service_traffic_route_rule_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type

Rule for routing incoming Virtual Service traffic with TLS_PASSTHROUGH protocol

Syntax
```

```

`dbms_cloud_oci_service_mesh_tls_passthrough_virtual_service_traffic_route_rule_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_details_t`type.

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_ACCESS_POLICY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`rules`

(optional) List of applicable rules.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_INGRESS_GATEWAY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`hosts`

(optional) An array of hostnames and their listener configuration that this gateway will bind to.

`access_logging`

(optional)

`mtls`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_INGRESS_GATEWAY_ROUTE_TABLE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`route_rules`

(optional) The route rules for the ingress gateway.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_MESH_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information. Example: `My new resource`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`mtls`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_DEPLOYMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`service_discovery`

(optional)

`listeners`

(optional) The listeners for the virtual deployment.

`access_logging`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_SERVICE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`default_routing_policy`

(optional)

`hosts`

(optional) The DNS hostnames of the virtual service that is used by its callers. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\". Can be omitted if the virtual service will only have TCP virtual deployments.

`mtls`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`route_rules`

(optional) The route rules for the virtual service.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_T Type

This resource represents a customer-managed virtual service deployment in the Service Mesh.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`virtual_service_id`

(required) The OCID of the virtual service in which this virtual deployment is created.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`service_discovery`

(optional)

`listeners`

(optional) The listeners for the virtual deployment

`access_logging`

(optional)

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_SUMMARY_T Type

Summary of the VirtualDeployment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`virtual_service_id`

(required) The OCID of the virtual service in which this virtual deployment is created.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the virtual deployment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_deployment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_COLLECTION_T Type

Results of a mesh search. Contains both VirtualDeploymentSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of virtual deployments.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_T Type

This resource represents a customer-managed service in the Service Mesh. Each virtual service declares multiple running versions of the service and maps to a group of instances/pods running a specific version of the actual service.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`mesh_id`

(required) The OCID of the service mesh in which this virtual service is created.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`default_routing_policy`

(optional)

`hosts`

(optional) The DNS hostnames of the virtual service that is used by its callers. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\". Can be omitted if the virtual service will only have TCP virtual deployments.

`mtls`

(optional)

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ACCESS_POLICY_TARGET_T Type

Virtual service target which communicates with other virtual services in a mesh.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_service_access_policy_target_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_t`type.

Fields

Field Description

`virtual_service_id`

(optional) The OCID of the virtual service resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ACCESS_POLICY_TARGET_DETAILS_T Type

Virtual service target which communicates with other virtual services in a mesh.

Syntax
```

```

`dbms_cloud_oci_service_mesh_virtual_service_access_policy_target_details_t`is a subtype of the`dbms_cloud_oci_service_mesh_access_policy_target_details_t`type.

Fields

Field Description

`virtual_service_id`

(required) The OCID of the virtual service resource.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_SUMMARY_T Type

Summary of the VirtualService.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`mesh_id`

(required) The OCID of the service mesh in which this access policy is created.

`name`

(required) A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the virtual service.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_COLLECTION_T Type

Results of a mesh search. Contains both VirtualServiceSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of virtual services.

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_traffic_route_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_T Type

This resource represents a customer-managed service route table in the Service Mesh.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`virtual_service_id`

(required) The OCID of the virtual service in which this virtual service route table is created.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`route_rules`

(optional) The route rules for the virtual service.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_SUMMARY_T Type

Summary of the VirtualServiceRouteTable.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`virtual_service_id`

(required) The OCID of the virtual service in which this virtual service route table is created.

`name`

(required) A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information. Example: `My unique resource name`

`description`

(optional) Description of the resource. It can be changed after creation. Avoid entering confidential information. Example: `This is my new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`priority`

(optional) The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.

`time_created`

(required) The time when this resource was created in an RFC3339 formatted datetime string.

`time_updated`

(required) The time when this resource was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the virtual service.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_virtual_service_route_table_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_COLLECTION_T Type

Results of a mesh search. Contains both VirtualServiceRouteTableSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of virtual service route tables.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until work is complete for that resource at which point it transitions to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_MESH', 'UPDATE_MESH', 'DELETE_MESH', 'MOVE_MESH', 'CREATE_ACCESS_POLICY', 'UPDATE_ACCESS_POLICY', 'DELETE_ACCESS_POLICY', 'MOVE_ACCESS_POLICY', 'CREATE_VIRTUAL_SERVICE', 'UPDATE_VIRTUAL_SERVICE', 'DELETE_VIRTUAL_SERVICE', 'MOVE_VIRTUAL_SERVICE', 'CREATE_VIRTUAL_SERVICE_ROUTE_TABLE', 'UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE', 'DELETE_VIRTUAL_SERVICE_ROUTE_TABLE', 'MOVE_VIRTUAL_SERVICE_ROUTE_TABLE', 'CREATE_VIRTUAL_DEPLOYMENT', 'UPDATE_VIRTUAL_DEPLOYMENT', 'DELETE_VIRTUAL_DEPLOYMENT', 'MOVE_VIRTUAL_DEPLOYMENT', 'CREATE_INGRESS_GATEWAY', 'UPDATE_INGRESS_GATEWAY', 'DELETE_INGRESS_GATEWAY', 'MOVE_INGRESS_GATEWAY', 'CREATE_INGRESS_GATEWAY_ROUTE_TABLE', 'UPDATE_INGRESS_GATEWAY_ROUTE_TABLE', 'DELETE_INGRESS_GATEWAY_ROUTE_TABLE', 'MOVE_INGRESS_GATEWAY_ROUTE_TABLE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'WAITING', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_MESH', 'UPDATE_MESH', 'DELETE_MESH', 'MOVE_MESH', 'CREATE_ACCESS_POLICY', 'UPDATE_ACCESS_POLICY', 'DELETE_ACCESS_POLICY', 'MOVE_ACCESS_POLICY', 'CREATE_VIRTUAL_SERVICE', 'UPDATE_VIRTUAL_SERVICE', 'DELETE_VIRTUAL_SERVICE', 'MOVE_VIRTUAL_SERVICE', 'CREATE_VIRTUAL_SERVICE_ROUTE_TABLE', 'UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE', 'DELETE_VIRTUAL_SERVICE_ROUTE_TABLE', 'MOVE_VIRTUAL_SERVICE_ROUTE_TABLE', 'CREATE_VIRTUAL_DEPLOYMENT', 'UPDATE_VIRTUAL_DEPLOYMENT', 'DELETE_VIRTUAL_DEPLOYMENT', 'MOVE_VIRTUAL_DEPLOYMENT', 'CREATE_INGRESS_GATEWAY', 'UPDATE_INGRESS_GATEWAY', 'DELETE_INGRESS_GATEWAY', 'MOVE_INGRESS_GATEWAY', 'CREATE_INGRESS_GATEWAY_ROUTE_TABLE', 'UPDATE_INGRESS_GATEWAY_ROUTE_TABLE', 'DELETE_INGRESS_GATEWAY_ROUTE_TABLE', 'MOVE_INGRESS_GATEWAY_ROUTE_TABLE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'WAITING', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestSummary objects.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occurred in an RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestError objects.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written in an RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_service_mesh_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both WorkRequestLogEntry items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestLogEntry objects.

- [Service Mesh Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-BA88F9DC-964B-4157-9EF0-68275FD8D5F8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4A0F7C23-F47F-46D3-B581-835B7ED53164)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_LOGGING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D9F1C3B2-F8BB-4416-B1B2-B180A81CF04E)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0BE65ADF-1891-4356-8A50-F1F37C2677B0)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E5B0DA00-D10B-455D-AE2C-372ED1F0F5C2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-9CAA6216-BCA9-4C54-9D59-540FFC580E47)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E41F9F6F-C893-49C4-A3CE-3C4FAC4362CC)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-87B17ED3-FA3D-490E-B410-AF436EACC662)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-281CCC22-098B-4969-915E-B9E1D6417430)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-84DC7842-8FA3-462B-95A1-0A28A512EE60)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-68134883-03BD-4138-95C2-E8E5CBCC4E10)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-C0043DB6-DCFF-470F-B82F-EC8042A4C846)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ALL_VIRTUAL_SERVICES_ACCESS_POLICY_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E4DE8022-2F15-400C-9D30-6A8880F74627)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ALL_VIRTUAL_SERVICES_ACCESS_POLICY_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-6BBD3A1C-FBF0-43B8-A1C6-9816258DBBE7)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-5AC6F522-6C52-482B-994F-DE40226A2873)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CERTIFICATE_AUTHORITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-3E641F6B-6D84-4AFA-8D4A-4072C8486E94)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_ACCESS_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-85AC6FE8-86A5-4F40-98DC-57CB86805D1E)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_INGRESS_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A8D44DD1-F902-4A9F-B776-29F438469504)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_INGRESS_GATEWAY_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-1DB12E80-D1A9-4364-B02C-60DB177B175C)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_MESH_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-2C3A29BB-9F7C-442A-A818-AE8DA7BFEEF3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_DEPLOYMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-72B97869-03C1-4E1B-80C9-4E6F007FBCF9)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_SERVICE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-C648028A-3327-49B2-BE6C-1D06ADF9FFEE)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CHANGE_VIRTUAL_SERVICE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-CC46DEB8-F2FE-4568-B50A-36330CCED292)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ACCESS_POLICY_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D982857E-804B-426A-BE2C-ED4517E6C27C)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_ACCESS_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-9D75D78D-80A7-40CE-8023-0FD690DB1BEF)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TLS_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0D4F17BF-A046-47F3-8FF6-F8AC36FFA905)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_LISTENER_CLIENT_VALIDATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4E3455FE-14A8-439A-95DE-51227ED107A8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_LISTENER_TLS_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-23B1646A-7C51-4512-A9CA-EDED6A8B891D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DA5FC9E3-2DFA-417E-9592-D858EE614D8A)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_LISTENER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DC0716E4-65E8-4F50-8CBC-9215250800B0)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-9FBCBA97-C995-4280-B08C-CEE5129EBE9B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_MUTUAL_TRANSPORT_LAYER_SECURITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-99D76A75-B222-4580-84BA-61642139923A)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-95783107-9944-453C-99F2-36415A7763B2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_INGRESS_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-1F53977B-6827-4726-BC99-478ABB748289)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_HOST_REF_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-9C91BDC1-B8A2-4BB5-8A09-9F37F6FECEA0)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TRAFFIC_RULE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-08DCF02F-D263-47E7-9C3C-0F3448D24D02)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4F9A5C5B-38A8-4BD1-931D-5FEFFDED59D8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-24F5B638-F947-457D-85AF-C345F298A133)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-F9ACBAD7-AA29-4A0A-84F5-12006431C414)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-18556AB4-E917-4E61-B27C-DE341952A7FB)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_INGRESS_GATEWAY_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-80F7F3F2-695D-49CB-AF8F-5034DCFF290B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MESH_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0E2915AF-1D49-4E46-B56D-20365FAB7B05)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CERTIFICATE_AUTHORITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D2C2093C-DFF2-4D07-ADD6-D3B70CCA4C47)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_MESH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-3E8880AE-FF9E-443E-95CC-0C5089A5516D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_SERVICE_DISCOVERY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-9D1F2F5D-0018-4BEA-999D-6503596F9326)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-29C3BD19-CFE4-4224-BE06-06E0BEB8092D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_LISTENER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DF357B28-F8B6-4F6C-9711-0E356429669A)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AB4EF01C-95D6-496A-9DF2-EC967FEA443B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_DEFAULT_VIRTUAL_SERVICE_ROUTING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-55DD7459-39A0-4BB3-A35B-1546BB9C6287)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_MUTUAL_TRANSPORT_LAYER_SECURITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-C319EEE3-7691-4B23-A2F3-E4E36183958C)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-F66E70E9-5C41-4576-9B2C-D5806977C0B8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4F623136-4C4B-4EB9-A0DC-B1A2BDF02CB3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-92A28C40-7FFA-4954-825E-B19CD7D6D188)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-302D1A95-B30B-4140-A8F5-FAC6351B48AD)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-FA0CFCA2-C762-4ED3-9D82-6FFD606C3DC0)
- [DBMS_CLOUD_OCI_SERVICE_MESH_CREATE_VIRTUAL_SERVICE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-26CF2CD3-F27C-4E5D-ACB3-A89299DB2356)
- [DBMS_CLOUD_OCI_SERVICE_MESH_DISABLED_SERVICE_DISCOVERY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A0E6E499-2A95-469F-9BDE-5D777E8CA570)
- [DBMS_CLOUD_OCI_SERVICE_MESH_DNS_SERVICE_DISCOVERY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-B0783381-252D-4393-9460-9D959EE13BCF)
- [DBMS_CLOUD_OCI_SERVICE_MESH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-8B6DFF58-F577-48AA-9CC3-A282B7036B11)
- [DBMS_CLOUD_OCI_SERVICE_MESH_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A4A95B77-09E9-4F79-8C2C-ED757256CC90)
- [DBMS_CLOUD_OCI_SERVICE_MESH_EXTERNAL_SERVICE_ACCESS_POLICY_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-6A6837F8-62BB-42AC-BCA2-3043957B4F89)
- [DBMS_CLOUD_OCI_SERVICE_MESH_EXTERNAL_SERVICE_ACCESS_POLICY_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-58401813-08F7-40F8-A720-E31796B9D80B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TRAFFIC_RULE_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AC918932-26CB-4492-87C1-57AD4536B1B3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-514C2445-E554-494D-9770-2A899C030ED2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_RULE_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-82798969-12EE-44E0-BF53-415DD29D9AD2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-6726E85F-E895-4619-A099-85982AEEBA43)
- [DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DAF8ECCD-6588-405E-AC76-D83C2F7A53C2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-2D2E5398-AA97-4293-83A0-B0DA13FEA8D7)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4722E140-27C7-4B5F-BB1C-DA2D18BBAB2C)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_TRAFFIC_RULE_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-38B056B4-2DC7-48F5-A9B4-087E870CC6D2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0F051710-5BBC-4272-99C2-F503B3865C51)
- [DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-BCFF5973-28F5-42B9-A0DC-5EB0F62D618D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_HTTP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DCA6F12C-3FC8-482F-BC88-225846F4E8DF)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A8881140-2D4B-4CE3-9F08-564B3C502440)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-CE49C00C-8451-4166-8002-A1CD8B57114D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ACCESS_POLICY_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DA5DD719-6658-4934-B176-BC9E9B12DCF7)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ACCESS_POLICY_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-8B8E4B96-8737-4033-B411-C94ED0DAD425)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-6E30BAFC-27A3-450A-BD82-DC5581AB7038)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D0D7A936-8D99-4B3D-9130-C6C60510BB2A)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4F526CF4-653D-4622-8B8D-3A398F78B3B6)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AB3EC90D-D446-45E2-A9C6-45C1670BB206)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A00EFB4B-C7EC-4D8E-8D38-5A88392DE722)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DF3387AC-90EF-4C71-9D84-C303675D66EA)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-7D9CB816-5B59-4964-BD8F-B11B566A4AF7)
- [DBMS_CLOUD_OCI_SERVICE_MESH_INGRESS_GATEWAY_ROUTE_TABLE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-BE630581-DB77-4FC9-A114-D8A824D82FD3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_LOCAL_FILE_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-15AD6ED4-1163-4327-B836-E70C84319B8B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_LOCAL_FILE_TLS_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-24C4E0E1-A733-40B6-B3A5-EB747294AE64)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MESH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-7A421474-C4F0-4D34-BE8D-320B84B7EFF7)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MESH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D39D241F-55A9-4589-A966-DCAB6A2D9430)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MESH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-98A66A91-703F-48C2-AE1A-6814093DBC90)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MESH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-78541F57-868A-4EF4-BB6E-638DFA8086FE)
- [DBMS_CLOUD_OCI_SERVICE_MESH_MUTUAL_TRANSPORT_LAYER_SECURITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D8121D2D-EAF1-4A53-A679-8161E1AA5AF8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_OCI_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AC4A22B0-C77C-4F1E-B031-A03FF11747E8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_OCI_TLS_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AA67B2FD-FF7A-4320-92B2-BD293CA5BD7A)
- [DBMS_CLOUD_OCI_SERVICE_MESH_PROXY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-2AFF7600-F059-4475-9B1F-B4B6DEE4E107)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TCP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-B6E86453-A4BD-4E55-B364-10A00C559100)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TCP_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A0CDFC18-AECD-45BF-91A4-55D600BAAAAD)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TCP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E5A703F8-7965-4E3D-8002-C085EE1182B6)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TCP_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-983E8D67-BE95-4E96-9EFE-A271A09E2D23)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-5978846F-3800-49AE-9603-12A5E916B9DB)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_INGRESS_GATEWAY_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-CE59E83D-E4E9-4E1F-A89B-D4E09E3E531D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-EADA8434-D367-4CEF-8311-7C8B3F3B7941)
- [DBMS_CLOUD_OCI_SERVICE_MESH_TLS_PASSTHROUGH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-FCB75636-B10E-4522-920B-5F4EE7D8D8F2)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_ACCESS_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-265964D6-0B47-4B1B-A9C1-148A9FAF4720)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_INGRESS_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-7982D57D-4616-4C69-88AF-02B442C2905E)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_INGRESS_GATEWAY_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-F3A80A81-7AF5-4667-947E-D1593DCD30C8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_MESH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-798035AD-4BA2-4460-A976-85F3C6230DB6)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-82F1688E-ED84-4C4D-828B-F00C6B24DFDD)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-EAAFEA96-5223-42BF-8C5B-2B8B8ABD8236)
- [DBMS_CLOUD_OCI_SERVICE_MESH_UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-BDBA7981-F815-41AA-9DC0-128F0F47C76E)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-47AB07D7-3A0D-4225-94CC-EBCDB729CD97)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-955111E1-073F-45A5-90BF-C1DFB66DF598)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-8AC11034-15C8-48C3-B52A-19E7C3AEB3E0)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_DEPLOYMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-ECF5345D-3D65-4486-A684-E57A9FEA4DA1)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0EA3E026-262B-4D33-BC37-1B7C7DC60829)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ACCESS_POLICY_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-DDC904F3-F1E8-4E92-AAAA-2157F9B59C79)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ACCESS_POLICY_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-0ABEA62C-F650-45EF-9483-7823D22EEEF1)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-854C7A0F-ADFA-4BE3-8038-1E808696143B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-B396B4C7-C4A6-4FC2-B02B-F0E53935B0E5)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-F885F051-E9EB-4D2D-B737-336B2FE58F5D)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_TRAFFIC_ROUTE_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-5584F01E-126A-4843-B5DC-791FB24E509F)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-112A00F1-F7F3-400D-BDCD-5B9456A0D1F6)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-4FECA69C-C18F-4626-8233-340282EF4B49)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-CF341DE6-0521-4B58-B8E5-9D7902806195)
- [DBMS_CLOUD_OCI_SERVICE_MESH_VIRTUAL_SERVICE_ROUTE_TABLE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-F27F555A-EB63-475A-B0B1-3F6D36A59260)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-ED515722-4886-4594-8FDF-9753B8DDFE4B)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-ADAB31C4-F9C7-46A1-A9F4-23B5338057DB)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-AC27651A-1DB9-4039-9E0C-969B305273B8)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-A0A3DB9D-9C89-4AD6-BFF2-2D4073AD7C3C)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-FA4FBFF1-619B-4949-AFB9-5D49FB89ACD4)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-C1FEDF10-0510-4149-89C7-EFD0FD8A63BA)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-2E2CD4F0-FF04-46CC-B36D-1AFD34905A77)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E2BB3D46-1CFB-47DD-B131-53B23ADC39AF)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-2423053A-1B4E-48F7-B208-CA1E661F2BB3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-12580FE0-7A1A-4E0C-8DB4-4B6347CFC8F3)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-E67A3B3C-021E-4670-9B13-50C0A25AC322)
- [DBMS_CLOUD_OCI_SERVICE_MESH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_mesh_t.html#ADSDK-GUID-D798202F-7CC5-492A-B777-E94C4B57EE0C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
