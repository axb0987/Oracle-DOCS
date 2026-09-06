# Web Application Firewall Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html
- Fetched: 2026-09-05 19:22 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#dcoc-content-body)

## Web Application Firewall Common Types

### DBMS_CLOUD_OCI_WAF_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_RULE_T Type

Base schema for WebAppFirewallPolicyRules, including properties common to all of them.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of WebAppFirewallPolicyRule.

Allowed values are: 'ACCESS_CONTROL', 'PROTECTION', 'REQUEST_RATE_LIMITING'

`name`

(required) Rule name. Must be unique within the module.

`condition_language`

(optional) The language used to parse condition from field `condition`. Available languages: * **JMESPATH** an extended JMESPath language syntax.

Allowed values are: 'JMESPATH'

`condition`

(optional) An expression that determines whether or not the rule action should be executed.

`action_name`

(required) References action by name from actions defined in WebAppFirewallPolicy.

### DBMS_CLOUD_OCI_WAF_ACCESS_CONTROL_RULE_T Type

Rule that represents Request/Response Access Control. Only actions of the following types are allowed to be referenced in this rule: * CHECK * ALLOW * RETURN_HTTP_RESPONSE

Syntax
```

```

`dbms_cloud_oci_waf_access_control_rule_t`is a subtype of the`dbms_cloud_oci_waf_web_app_firewall_policy_rule_t`type.

### DBMS_CLOUD_OCI_WAF_ACTION_T Type

An object that represents action and its options. The action can be terminating, if it stops further execution of rules and modules. And non-terminating, if it does not interrupt execution flow.

Syntax
```

```

Fields

Field Description

`l_type`

(required) * **CHECK** is a non-terminating action that does not stop the execution of rules in current module, just emits a log message documenting result of rule execution. * **ALLOW** is a non-terminating action which upon matching rule skips all remaining rules in the current module. * **RETURN_HTTP_RESPONSE** is a terminating action which is executed immediately, returns a defined HTTP response.

Allowed values are: 'CHECK', 'ALLOW', 'RETURN_HTTP_RESPONSE'

`name`

(required) Action name. Can be used to reference the action.

### DBMS_CLOUD_OCI_WAF_ALLOW_ACTION_T Type

An object that represents an action which upon matching rule skips all remaining rules in the current module.

Syntax
```

```

`dbms_cloud_oci_waf_allow_action_t`is a subtype of the`dbms_cloud_oci_waf_action_t`type.

### DBMS_CLOUD_OCI_WAF_CHANGE_NETWORK_ADDRESS_LIST_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAF_CHANGE_RESOURCE_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAF_CHANGE_WEB_APP_FIREWALL_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAF_CHANGE_WEB_APP_FIREWALL_POLICY_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAF_CHECK_ACTION_T Type

An object that represents an action which does not stop the execution of rules in current module, just emits a log message documenting result of rule execution.

Syntax
```

```

`dbms_cloud_oci_waf_check_action_t`is a subtype of the`dbms_cloud_oci_waf_action_t`type.

### DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_T Type

Defines how much a contributing capability contributes towards the action threshold of a collaborative protection capability.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of contributing protection capability.

`display_name`

(required) The display name of contributing protection capability.

`weight`

(required) The weight of contributing protection capability.

### DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_OVERRIDE_T Type

Collaborative capability key and overriding weight.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of collaborative capability for which weight will be overridden.

`weight`

(required) The value of weight to set.

### DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_DETAILS_T Type

The information about new NetworkAddressList.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) NetworkAddressList display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(required) Type of NetworkAddressList.

Allowed values are: 'ADDRESSES', 'VCN_ADDRESSES'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_ADDRESSES_DETAILS_T Type

The information about new NetworkAddressListAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_create_network_address_list_addresses_details_t`is a subtype of the`dbms_cloud_oci_waf_create_network_address_list_details_t`type.

Fields

Field Description

`addresses`

(required) A list of IP address prefixes in CIDR notation. To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_PRIVATE_ADDRESSES_T Type

A pair of VCN OCID and private IP address prefix in CIDR notation.

Syntax
```

```

Fields

Field Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`addresses`

(required) A private IP address or CIDR IP address range.

### DBMS_CLOUD_OCI_WAF_PRIVATE_ADDRESSES_TBL Type

Nested table type of dbms_cloud_oci_waf_private_addresses_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_DETAILS_T Type

The information about new NetworkAddressListVcnAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_create_network_address_list_vcn_addresses_details_t`is a subtype of the`dbms_cloud_oci_waf_create_network_address_list_details_t`type.

Fields

Field Description

`vcn_addresses`

(required) A list of private address prefixes, each associated with a particular VCN. To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_DETAILS_T Type

The information about new Web App Firewall.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppFirewall display name, can be renamed.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`web_app_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppFirewallPolicy, which is attached to the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_LOAD_BALANCER_DETAILS_T Type

The information about new WebAppFirewallLoadBalancer.

Syntax
```

```

`dbms_cloud_oci_waf_create_web_app_firewall_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_waf_create_web_app_firewall_details_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppFirewallPolicy is attached to.

### DBMS_CLOUD_OCI_WAF_ACCESS_CONTROL_RULE_TBL Type

Nested table type of dbms_cloud_oci_waf_access_control_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_REQUEST_ACCESS_CONTROL_T Type

Module that allows inspection of HTTP request properties and to return a defined HTTP response. In this module, rules with the name 'Default Action' are not allowed, since this name is reserved for default action logs.

Syntax
```

```

Fields

Field Description

`default_action_name`

(required) References an default Action to take if no AccessControlRule was matched. Allowed action types: * **ALLOW** continues execution of other modules and their rules. * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.

`rules`

(optional) Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.

### DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_CONFIGURATION_T Type

Rate limiting configuration.

Syntax
```

```

Fields

Field Description

`period_in_seconds`

(required) Evaluation period in seconds.

`requests_limit`

(required) Requests allowed per evaluation period.

`action_duration_in_seconds`

(optional) Duration of block action application in seconds when `requestsLimit` is reached. Optional and can be 0 (no block duration).

### DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_waf_request_rate_limiting_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_RULE_T Type

Rule that represents RequestRateLimitingConfigurations. Only actions of the following types are allowed to be referenced in this rule: * CHECK * RETURN_HTTP_RESPONSE

Syntax
```

```

`dbms_cloud_oci_waf_request_rate_limiting_rule_t`is a subtype of the`dbms_cloud_oci_waf_web_app_firewall_policy_rule_t`type.

Fields

Field Description

`configurations`

(required) Rate Limiting Configurations. Each configuration counts requests towards its own `requestsLimit`.

### DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_RULE_TBL Type

Nested table type of dbms_cloud_oci_waf_request_rate_limiting_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_T Type

Module that allows inspection of HTTP connection properties and to limit requests frequency for a given key.

Syntax
```

```

Fields

Field Description

`rules`

(optional) Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_EXCLUSIONS_T Type

Identifies specific HTTP message parameters to exclude from inspection by a protection capability.

Syntax
```

```

Fields

Field Description

`request_cookies`

(optional) List of HTTP request cookie values (by cookie name) to exclude from inspecting. Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and 'cookieValue' will not be inspected.

`args`

(optional) List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting. Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both 'argumentName' and 'argumentValue' will not be inspected.

### DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_OVERRIDE_TBL Type

Nested table type of dbms_cloud_oci_waf_collaborative_capability_weight_override_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_T Type

References an OCI-managed protection capability. Checks if HTTP requests/responses are malicious.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of referenced protection capability.

`version`

(required) Version of referenced protection capability.

`exclusions`

(optional)

`action_name`

(optional) Override action to take if capability was triggered, defined in Protection Rule for this capability. Only actions of type CHECK are allowed.

`collaborative_action_threshold`

(optional) The minimum sum of weights of associated collaborative protection capabilities that have triggered which must be reached in order for _this_ capability to trigger. This field is ignored for non-collaborative capabilities.

`collaborative_weights`

(optional) Explicit weight values to use for associated collaborative protection capabilities.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SETTINGS_T Type

Settings for protection capabilities

Syntax
```

```

Fields

Field Description

`max_number_of_arguments`

(optional) Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.

`max_single_argument_length`

(optional) Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.

`max_total_argument_length`

(optional) Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.

`max_http_request_headers`

(optional) Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.

`max_http_request_header_length`

(optional) Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.

`allowed_http_methods`

(optional) List of allowed HTTP methods. Each value as a RFC7230 formated token string. Used in protection capability 911100: Restrict HTTP Request Methods.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_TBL Type

Nested table type of dbms_cloud_oci_waf_protection_capability_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_PROTECTION_RULE_T Type

Rule that represents Request/Response Protection. Only actions of the following types are allowed to be referenced in this rule: * CHECK * RETURN_HTTP_RESPONSE

Syntax
```

```

`dbms_cloud_oci_waf_protection_rule_t`is a subtype of the`dbms_cloud_oci_waf_web_app_firewall_policy_rule_t`type.

Fields

Field Description

`protection_capabilities`

(required) An ordered list that references OCI-managed protection capabilities. Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order is decided at runtime for improved performance. The array cannot contain entries with the same pair of capability key and version more than once.

`protection_capability_settings`

(optional)

`is_body_inspection_enabled`

(optional) Enables/disables body inspection for this protection rule. Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will be available at a later date.

### DBMS_CLOUD_OCI_WAF_PROTECTION_RULE_TBL Type

Nested table type of dbms_cloud_oci_waf_protection_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_REQUEST_PROTECTION_T Type

Module that allows to enable OCI-managed protection capabilities for incoming HTTP requests.

Syntax
```

```

Fields

Field Description

`rules`

(optional) Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection Capabilities of REQUEST_PROTECTION_CAPABILITY type.

`body_inspection_size_limit_in_bytes`

(optional) Maximum size of inspected HTTP message body in bytes. Actions to take if this limit is exceeded are defined in `bodyInspectionSizeLimitExceededActionName`. Body inspection maximum size allowed is defined with per-tenancy limit: 8192 bytes.

`body_inspection_size_limit_exceeded_action_name`

(optional) References action by name from actions defined in WebAppFirewallPolicy. Executed if HTTP message body size exceeds limit set in field `bodyInspectionSizeLimitInBytes`. If this field is `null` HTTP message body will inspected up to `bodyInspectionSizeLimitInBytes` and the rest will not be inspected by Protection Capabilities. Allowed action types: * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.

### DBMS_CLOUD_OCI_WAF_RESPONSE_ACCESS_CONTROL_T Type

Module that allows inspection of HTTP response properties and to return a defined HTTP response.

Syntax
```

```

Fields

Field Description

`rules`

(optional) Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.

### DBMS_CLOUD_OCI_WAF_RESPONSE_PROTECTION_T Type

Module that allows to enable OCI-managed protection capabilities for HTTP responses.

Syntax
```

```

Fields

Field Description

`rules`

(optional) Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection capabilities of RESPONSE_PROTECTION_CAPABILITY type.

### DBMS_CLOUD_OCI_WAF_ACTION_TBL Type

Nested table type of dbms_cloud_oci_waf_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_POLICY_DETAILS_T Type

The information about new WebAppFirewallPolicy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppFirewallPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`actions`

(optional) Predefined actions for use in multiple different rules. Not all actions are supported in every module. Some actions terminate further execution of modules and rules in a module and some do not. Actions names must be unique within this array.

`request_access_control`

(optional)

`request_rate_limiting`

(optional)

`request_protection`

(optional)

`response_access_control`

(optional)

`response_protection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_ERROR_T Type

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

### DBMS_CLOUD_OCI_WAF_HTTP_RESPONSE_BODY_T Type

Type of returned HTTP response body.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of HttpResponseBody.

Allowed values are: 'STATIC_TEXT'

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_T Type

IP addresses that can be used between different WebAppFirewallPolicies.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the NetworkAddressList.

`display_name`

(required) NetworkAddressList display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the NetworkAddressList was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the NetworkAddressList was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the NetworkAddressList.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`l_type`

(required) Type of NetworkAddressList.

Allowed values are: 'ADDRESSES', 'VCN_ADDRESSES'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_ADDRESSES_T Type

A NetworkAddressList that contains addresses.

Syntax
```

```

`dbms_cloud_oci_waf_network_address_list_addresses_t`is a subtype of the`dbms_cloud_oci_waf_network_address_list_t`type.

Fields

Field Description

`addresses`

(required) A list of IP address prefixes in CIDR notation. To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_SUMMARY_T Type

Summary of NetworkAddressList.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the NetworkAddressList.

`display_name`

(required) NetworkAddressList display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the NetworkAddressList was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the NetworkAddressList was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the NetworkAddress List.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`l_type`

(required) Type of NetworkAddressList.

Allowed values are: 'ADDRESSES', 'VCN_ADDRESSES'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_ADDRESSES_SUMMARY_T Type

Summary of NetworkAddressListAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_network_address_list_addresses_summary_t`is a subtype of the`dbms_cloud_oci_waf_network_address_list_summary_t`type.

Fields

Field Description

`addresses`

(required) A list of IP address prefixes in CIDR notation. To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waf_network_address_list_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_COLLECTION_T Type

Contains NetworkAddressListSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of NetworkAddressListSummary objects.

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_T Type

A NetworkAddressList that contains VCN addresses.

Syntax
```

```

`dbms_cloud_oci_waf_network_address_list_vcn_addresses_t`is a subtype of the`dbms_cloud_oci_waf_network_address_list_t`type.

Fields

Field Description

`vcn_addresses`

(required) A list of private address prefixes, each associated with a particular VCN. To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_SUMMARY_T Type

Summary of NetworkAddressListVcnAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_network_address_list_vcn_addresses_summary_t`is a subtype of the`dbms_cloud_oci_waf_network_address_list_summary_t`type.

Fields

Field Description

`vcn_addresses`

(required) A list of private address prefixes, each associated with a particular VCN. To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_TBL Type

Nested table type of dbms_cloud_oci_waf_collaborative_capability_weight_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SUMMARY_T Type

A summary of available OCI-managed protection capabilities in WebAppFirewallPolicy. Protection capabilies checks HTTP requests/responses if they are malicious.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of protection capability.

`display_name`

(required) The display name of protection capability.

`description`

(required) The description of protection capability.

`version`

(required) The version of protection capability.

`is_latest_version`

(required) The field that shows if this is the latest version of protection capability.

`group_tags`

(optional) The list of unique names protection capability group tags that are associated with this capability. Example: [\"PCI\", \"Recommended\"]

`l_type`

(required) The type of protection capability. * **REQUEST_PROTECTION_CAPABILITY** can only be used in `requestProtection` module of WebAppFirewallPolicy. * **RESPONSE_PROTECTION_CAPABILITY** can only be used in `responseProtection` module of WebAppFirewallPolicy.

Allowed values are: 'REQUEST_PROTECTION_CAPABILITY', 'RESPONSE_PROTECTION_CAPABILITY'

`collaborative_action_threshold`

(optional) The default collaborative action threshold for OCI-managed collaborative protection capability. Collaborative protection capabilities are made of several simple, non-collaborative protection capabilities (referred to as `contributing capabilities` later on) which have weights assigned to them. These weights can be found in the `collaborativeWeights` array. For incoming/outgoing HTTP messages, all contributing capabilities are executed and the sum of all triggered contributing capabilities weights is calculated. Only if this sum is greater than or equal to `collaborativeActionThreshold` is the incoming/outgoing HTTP message marked as malicious. This field is ignored for non-collaborative capabilities.

`collaborative_weights`

(optional) The weights of contributing capabilities. Defines how much each contributing capability contributes towards the action threshold of a collaborative protection capability. This field is ignored for non-collaborative capabilities.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waf_protection_capability_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_COLLECTION_T Type

Result of a protection capabilities search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of protection capabilities.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_SUMMARY_T Type

Object representing protection cabapility group tag and its metadata.

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name of protection capability group tag.

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waf_protection_capability_group_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_COLLECTION_T Type

Result of a protection capabilities group tags search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of protection capabilities group tags.

### DBMS_CLOUD_OCI_WAF_RESPONSE_HEADER_T Type

A header field to add to a response.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the header field.

`value`

(required) The value of the header field.

### DBMS_CLOUD_OCI_WAF_RESPONSE_HEADER_TBL Type

Nested table type of dbms_cloud_oci_waf_response_header_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_RETURN_HTTP_RESPONSE_ACTION_T Type

An object that represents an action which returns a defined HTTP response.

Syntax
```

```

`dbms_cloud_oci_waf_return_http_response_action_t`is a subtype of the`dbms_cloud_oci_waf_action_t`type.

Fields

Field Description

`code`

(required) Response code. The following response codes are valid values for this property: * 2xx 200 OK 201 Created 202 Accepted 206 Partial Content * 3xx 300 Multiple Choices 301 Moved Permanently 302 Found 303 See Other 307 Temporary Redirect * 4xx 400 Bad Request 401 Unauthorized 403 Forbidden 404 Not Found 405 Method Not Allowed 408 Request Timeout 409 Conflict 411 Length Required 412 Precondition Failed 413 Payload Too Large 414 URI Too Long 415 Unsupported Media Type 416 Range Not Satisfiable 422 Unprocessable Entity 429 Too Many Requests 494 Request Header Too Large 495 Cert Error 496 No Cert 497 HTTP to HTTPS * 5xx 500 Internal Server Error 501 Not Implemented 502 Bad Gateway 503 Service Unavailable 504 Gateway Timeout 507 Insufficient Storage Example: `200`

`headers`

(optional) Adds headers defined in this array for HTTP response. Hop-by-hop headers are not allowed to be set: * Connection * Keep-Alive * Proxy-Authenticate * Proxy-Authorization * TE * Trailer * Transfer-Encoding * Upgrade

`body`

(optional)

### DBMS_CLOUD_OCI_WAF_STATIC_TEXT_HTTP_RESPONSE_BODY_T Type

Allows returning static text as HTTP response body. Example: { \"type\": \"STATIC_TEXT\", \"text\": \"{\\\\"code\\\": 403,\\\\"message\\\":\\\"Unauthorised\\\"\}\" }

Syntax
```

```

`dbms_cloud_oci_waf_static_text_http_response_body_t`is a subtype of the`dbms_cloud_oci_waf_http_response_body_t`type.

Fields

Field Description

`text`

(required) Static response body text.

### DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) NetworkAddressList display name, can be renamed.

`l_type`

(required) Type of NetworkAddressList.

Allowed values are: 'ADDRESSES', 'VCN_ADDRESSES'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_ADDRESSES_DETAILS_T Type

The information to be updated for NetworkAddressListAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_update_network_address_list_addresses_details_t`is a subtype of the`dbms_cloud_oci_waf_update_network_address_list_details_t`type.

Fields

Field Description

`addresses`

(optional) A list of IP address prefixes in CIDR notation. To specify all addresses, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_DETAILS_T Type

The information to be updated for NetworkAddressListVcnAddresses.

Syntax
```

```

`dbms_cloud_oci_waf_update_network_address_list_vcn_addresses_details_t`is a subtype of the`dbms_cloud_oci_waf_update_network_address_list_details_t`type.

Fields

Field Description

`vcn_addresses`

(optional) A list of private address prefixes, each associated with a particular VCN. To specify all addresses in a VCN, use \"0.0.0.0/0\" for IPv4 and \"::/0\" for IPv6.

### DBMS_CLOUD_OCI_WAF_UPDATE_WEB_APP_FIREWALL_DETAILS_T Type

The information to be updated for WebAppFirewall.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppFirewall display name, can be renamed.

`web_app_firewall_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppFirewallPolicy, which is attached to the resource. This update guarantees that the resource always has WebAppFirewallPolicy attached at any time.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_UPDATE_WEB_APP_FIREWALL_POLICY_DETAILS_T Type

The information to be updated. When updating WebAppFirewallPolicy, shallow merge is used for all top-level fields, meaning that top-level fields with defined values are completely overwritten and top-level fields without defined values are unchanged.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppFirewallPolicy display name, can be renamed.

`actions`

(optional) Predefined actions for use in multiple different rules. Not all actions are supported in every module. Some actions terminate further execution of modules and rules in a module and some do not. Actions names must be unique within this array.

`request_access_control`

(optional)

`request_rate_limiting`

(optional)

`request_protection`

(optional)

`response_access_control`

(optional)

`response_protection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_T Type

A resource connecting a WebAppFirewallPolicy to a backend of particular type, applying that policy's coverage to the backend.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppFirewall.

`display_name`

(required) WebAppFirewall display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`web_app_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppFirewallPolicy, which is attached to the resource.

`time_created`

(required) The time the WebAppFirewall was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppFirewall was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppFirewall.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_SUMMARY_T Type

Summary of the WebAppFirewall.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppFirewall.

`display_name`

(required) WebAppFirewall display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`web_app_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppFirewallPolicy, which is attached to the resource.

`time_created`

(required) The time the WebAppFirewall was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppFirewall was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppFirewall.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waf_web_app_firewall_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_COLLECTION_T Type

Result of a WebAppFirewall list operation.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WebAppFirewalls.

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_LOAD_BALANCER_T Type

WebAppFirewall to a LoadBalancer resource.

Syntax
```

```

`dbms_cloud_oci_waf_web_app_firewall_load_balancer_t`is a subtype of the`dbms_cloud_oci_waf_web_app_firewall_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppFirewallPolicy is attached to.

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_LOAD_BALANCER_SUMMARY_T Type

Summary of the WebAppFirewallLoadBalancer.

Syntax
```

```

`dbms_cloud_oci_waf_web_app_firewall_load_balancer_summary_t`is a subtype of the`dbms_cloud_oci_waf_web_app_firewall_summary_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppFirewallPolicy is attached to.

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_T Type

The details of WebAppFirewallPolicy. A policy is comprised of rules, which allows executing inspections of incoming/outgoing HTTP message parameters and execution of actions, based on results of rules execution. In policy, rules are grouped into modules by their functionality. Modules can be further divided by the type of HTTP messages they handle: Modules that inspect incoming HTTP request. These modules are executed in the order they are enumerated here: * requestAccessControl * requestRateLimiting * requestProtection Modules that inspect outgoing HTTP responses. These modules are executed in the order they are enumerated here: * responseAccessControl * responseProtection

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppFirewallPolicy.

`display_name`

(required) WebAppFirewallPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppFirewallPolicy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`actions`

(optional) Predefined actions for use in multiple different rules. Not all actions are supported in every module. Some actions terminate further execution of modules and rules in a module and some do not. Actions names must be unique within this array.

`request_access_control`

(optional)

`request_rate_limiting`

(optional)

`request_protection`

(optional)

`response_access_control`

(optional)

`response_protection`

(optional)

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_SUMMARY_T Type

Summary of the WebAppFirewallPolicy.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppFirewallPolicy.

`display_name`

(required) WebAppFirewallPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppFirewallPolicy.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waf_web_app_firewall_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_COLLECTION_T Type

Contains WebAppFirewallPolicySummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of WebAppFirewallPolicySummary objects.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a WorkRequest.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the WorkRequest affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the WorkRequest. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource the WorkRequest affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_waf_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_T Type

A description of WorkRequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the WorkRequest

Allowed values are: 'CREATE_WAF_POLICY', 'UPDATE_WAF_POLICY', 'DELETE_WAF_POLICY', 'MOVE_WAF_POLICY', 'CREATE_NETWORK_ADDRESS_LIST', 'UPDATE_NETWORK_ADDRESS_LIST', 'DELETE_NETWORK_ADDRESS_LIST', 'MOVE_NETWORK_ADDRESS_LIST', 'CREATE_WEB_APP_FIREWALL', 'UPDATE_WEB_APP_FIREWALL', 'DELETE_WEB_APP_FIREWALL', 'MOVE_WEB_APP_FIREWALL'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WorkRequest.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the WorkRequest. WorkRequests should be scoped to the same compartment as the resource the work request affects.

`resources`

(required) The resources affected by this WorkRequest.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_waf_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_COLLECTION_T Type

Result of a WorkRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequests.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_T Type

An error encountered while executing a WorkRequest.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on https://docs.cloud.oracle.com/Content/API/References/apierrors.htm.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_waf_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_COLLECTION_T Type

Result of a WorkRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestError objects.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a WorkRequest.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_waf_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Result of a WorkRequestLog search. Contains both WorkRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestLogEntries.

- [Web Application Firewall Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-5A69F224-C0E7-4F52-9163-B879D70F01F0)
- [DBMS_CLOUD_OCI_WAF_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-8D75C8F2-5D81-4FD3-B85C-BB73EF1327B3)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-BF04446B-24EC-4319-B92F-5E1B3F71DF1A)
- [DBMS_CLOUD_OCI_WAF_ACCESS_CONTROL_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-55100A2D-26E4-4BB7-B116-459382837C15)
- [DBMS_CLOUD_OCI_WAF_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-4813E4ED-8252-4613-AB97-4FDA0A2F2DEF)
- [DBMS_CLOUD_OCI_WAF_ALLOW_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-03643BF7-F863-4944-9138-FF626DA2DB6E)
- [DBMS_CLOUD_OCI_WAF_CHANGE_NETWORK_ADDRESS_LIST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-3A0659C6-1869-496F-8D06-84C94C88B029)
- [DBMS_CLOUD_OCI_WAF_CHANGE_RESOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-3CF1D1EB-96DE-48A6-969F-945135F34338)
- [DBMS_CLOUD_OCI_WAF_CHANGE_WEB_APP_FIREWALL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-1B0654DF-188E-416E-B256-933467E98554)
- [DBMS_CLOUD_OCI_WAF_CHANGE_WEB_APP_FIREWALL_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-F2AAAAA5-18C2-4E45-813B-5EAB6B1F4268)
- [DBMS_CLOUD_OCI_WAF_CHECK_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-AA63521A-2ED3-457E-A14A-71EA9EF594D5)
- [DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-8852299D-2110-4508-8C52-0BA97B8C3045)
- [DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_OVERRIDE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-639BBE9A-6B07-4007-BDE3-68114F8385F8)
- [DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-3D3C40B6-6BFD-421B-8FEF-51200F4E6EAA)
- [DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_ADDRESSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-56B46EEF-AD9D-40D5-AD0C-6DE80D5D1BE1)
- [DBMS_CLOUD_OCI_WAF_PRIVATE_ADDRESSES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-B019F5BD-83C3-45B0-8AD0-5CB0D0191D7A)
- [DBMS_CLOUD_OCI_WAF_PRIVATE_ADDRESSES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-A4D795A2-4DC3-4409-89A6-5BEE2160EAF6)
- [DBMS_CLOUD_OCI_WAF_CREATE_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-DBF6263B-8AFC-4144-A364-743D0DB69E4F)
- [DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-0C32776D-8696-43C3-B824-0038865EFD96)
- [DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-973F2882-B5FE-4F26-B461-E9EA46F2CE07)
- [DBMS_CLOUD_OCI_WAF_ACCESS_CONTROL_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-1263F72F-2D80-4A9F-B4C6-77CFF47585E5)
- [DBMS_CLOUD_OCI_WAF_REQUEST_ACCESS_CONTROL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-E1A54D5B-9262-406F-927F-95BB394CA12A)
- [DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-117D8D13-DEB7-4C68-85BF-851AF67BE4DC)
- [DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-CB5C8D19-7A8F-426C-B05B-3249758D30BE)
- [DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-123A82AD-F493-4E1D-B1E2-3F8F8AE978B9)
- [DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-EB2508F1-B666-44BE-BA96-6298ACAE9921)
- [DBMS_CLOUD_OCI_WAF_REQUEST_RATE_LIMITING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-FED17AD2-0335-47C4-B766-878C48742838)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_EXCLUSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-E3E32E3E-B452-42C6-8FB9-5D4BD03ABA1F)
- [DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_OVERRIDE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-E59B10DB-1F3F-4776-98D8-8AD95C95302F)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-600931FB-74BE-4E77-9BC1-F9B24284177F)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-4FF1C763-06E1-461F-B476-5C1ADDB41932)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-473913E7-78FA-40F5-A3CE-E2DE0F088B5E)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-84269D8A-9238-450E-B9F9-DCE1077DCDC5)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-09DBFF1E-C458-4441-9E2D-4CC06941AB50)
- [DBMS_CLOUD_OCI_WAF_REQUEST_PROTECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-42C97568-DB67-4626-8889-EEC79D83B1E7)
- [DBMS_CLOUD_OCI_WAF_RESPONSE_ACCESS_CONTROL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-F840620E-BE24-4D10-B9E0-97B53CD52634)
- [DBMS_CLOUD_OCI_WAF_RESPONSE_PROTECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C0B2B8D3-177C-48AE-81CD-55EBB6062C0A)
- [DBMS_CLOUD_OCI_WAF_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-F612D7A9-B2F1-43C4-B891-41C02FB9B525)
- [DBMS_CLOUD_OCI_WAF_CREATE_WEB_APP_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C897816A-21DA-442F-9B52-0DBF5DAF851B)
- [DBMS_CLOUD_OCI_WAF_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-878E85B4-A102-461D-9E2F-287801651D66)
- [DBMS_CLOUD_OCI_WAF_HTTP_RESPONSE_BODY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-D7FDA654-A1F9-4421-8B11-3037107E91F3)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-B6081792-93AE-4392-A734-6F62115B4D0D)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_ADDRESSES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-FE0275BA-421A-4D56-A7AA-806325B5B716)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C39A473A-C5CB-4CF7-A0AC-9A1283D15E52)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_ADDRESSES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-41B1E6CB-088B-47B7-BC6C-32559E2FFD80)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-645A3A1F-8B8F-4FE1-A561-4AFF9B364D2B)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C05F483D-A839-4B78-A4F4-688D32B064F9)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-D1738BCA-B9D5-4279-9CB5-E945AED0262E)
- [DBMS_CLOUD_OCI_WAF_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-BE9F424C-8FD0-4613-8E5D-E7E7662F200C)
- [DBMS_CLOUD_OCI_WAF_COLLABORATIVE_CAPABILITY_WEIGHT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-F96126E0-FC2A-4892-9100-B189491B80B8)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-0C0E1F2A-8F78-4327-82A2-0C7B7C05166D)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-E436C2A9-8E3D-4BDC-8D30-A48EE5EED4A6)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-959AA6FB-160B-453C-A5FE-BAB3620BBC6A)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-A0899BC1-9FF1-4A73-9A2F-1410E2C08C67)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-9F5BB204-58FE-420A-BD61-E0D9E92305BC)
- [DBMS_CLOUD_OCI_WAF_PROTECTION_CAPABILITY_GROUP_TAG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-5D09CDDC-7064-4C06-B012-62C65F2C68F2)
- [DBMS_CLOUD_OCI_WAF_RESPONSE_HEADER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-DA88FED8-6CFB-46C1-A7C4-8FC80CBF1CEC)
- [DBMS_CLOUD_OCI_WAF_RESPONSE_HEADER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-62727653-D1B8-4060-A600-776A5F3DB99B)
- [DBMS_CLOUD_OCI_WAF_RETURN_HTTP_RESPONSE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-4A4868F1-E717-4A72-B0DF-9883CBE18687)
- [DBMS_CLOUD_OCI_WAF_STATIC_TEXT_HTTP_RESPONSE_BODY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-1722A7AE-F271-4615-A33B-BD2C5F9E4D11)
- [DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C95F1731-2831-44A7-8306-559AC78F02A0)
- [DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_ADDRESSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-CE8B638C-5F31-4244-B821-26F597A60D66)
- [DBMS_CLOUD_OCI_WAF_UPDATE_NETWORK_ADDRESS_LIST_VCN_ADDRESSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-AB7585B6-F2A7-4E51-8BF3-5CD9A9C6761C)
- [DBMS_CLOUD_OCI_WAF_UPDATE_WEB_APP_FIREWALL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-258B9D72-F388-4D8F-8F9B-3E57D2CFE2A3)
- [DBMS_CLOUD_OCI_WAF_UPDATE_WEB_APP_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-D44D5A16-971F-448B-95BB-8E169D555149)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-EC4DFEE7-5EEB-471A-B7F4-1D1CDD3EC861)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C5DF435B-C1F0-4985-AB87-42C1DACA59D1)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-89AEB85C-EC6D-4693-A5A5-F0991E7EFC04)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-8F92E584-8435-424A-A83D-69135CE10625)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-E464ED36-2E49-4D04-B534-ADA4381BCCDD)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_LOAD_BALANCER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-92E7A541-730F-4101-96B8-DAD41B54EC86)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-74DE2C68-4F2E-4456-B8F5-EC0704DF9577)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-EC7E9EB0-8129-4300-BB03-F9AE403B40FF)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-88FFDD2A-4886-4E9D-AC62-E8C4F3F0FD3E)
- [DBMS_CLOUD_OCI_WAF_WEB_APP_FIREWALL_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-00240A09-64D7-4087-816C-BA4B4B7AF309)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-D3486F7D-DA00-494D-97C7-0DE54503BD95)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-9DE36F4B-2C3B-45B4-8931-B72E1E6DB004)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-B4DA2602-0A9A-4344-802D-6AC036CD52A0)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C7BF7BF9-EA7B-49C9-9CD1-A9C17AD13206)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-652E8ED9-1692-4DD8-AB91-EC301C10B198)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-A7620B9A-8BA0-440B-B12D-B761E4F94D9A)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-42630EC1-324D-4E9D-91A9-F6B944A28C98)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-56F9C08D-A19C-4FFB-9988-FA6EFA0772C5)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-C890A29B-E9A5-4022-9672-991ABA1EA291)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-0472CA03-49E6-4A72-A233-CA0418D86CB2)
- [DBMS_CLOUD_OCI_WAF_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waf_t.html#ADSDK-GUID-ECC85A98-610F-4A0C-808B-C95C8EBD2449)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
