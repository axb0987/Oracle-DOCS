# API Gateway Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#dcoc-content-body)

## API Gateway Common Types

### DBMS_CLOUD_OCI_APIGATEWAY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_ACCESS_LOG_POLICY_T Type

Configures the logging policies for the access logs of an API Deployment.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Enables pushing of access logs to the legacy OCI Object Storage log archival bucket. Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to 'access' in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket. Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.

### DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_TOKEN_CLAIM_T Type

An individual JWT claim.

Syntax
```

```

Fields

Field Description

`key`

(required) Name of the claim.

`l_values`

(optional) The list of acceptable values for a given claim. If this value is \"null\" or empty and \"isRequired\" set to \"true\", then the presence of this claim in the JWT is validated.

`is_required`

(optional) Whether the claim is required to be present in the JWT or not. If set to \"false\", the claim values will be matched only if the claim is present in the JWT.

### DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_TOKEN_CLAIM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_json_web_token_claim_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_ADDITIONAL_VALIDATION_POLICY_T Type

Additional JWT validation checks.

Syntax
```

```

Fields

Field Description

`issuers`

(optional) A list of parties that could have issued the token.

`audiences`

(optional) The list of intended recipients for the token.

`verify_claims`

(optional) A list of claims which should be validated to consider the token valid.

### DBMS_CLOUD_OCI_APIGATEWAY_ROUTE_AUTHORIZATION_POLICY_T Type

If authentication has been performed, validate whether the request scope (if any) applies to this route. If no RouteAuthorizationPolicy is defined for a route, a policy with a type of AUTHENTICATION_ONLY is applied.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Indicates how authorization should be applied. For a type of ANY_OF, an \"allowedScope\" property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an authenticated API must have the \"isAnonymousAccessAllowed\" property set to \"true\" in the authentication policy.

Allowed values are: 'ANONYMOUS', 'ANY_OF', 'AUTHENTICATION_ONLY'

### DBMS_CLOUD_OCI_APIGATEWAY_ANONYMOUS_ROUTE_AUTHORIZATION_POLICY_T Type

For a type of ANONYMOUS, an authenticated API must have the \"isAnonymousAccessAllowed\" property set to \"true\" in the authentication policy.

Syntax
```

```

`dbms_cloud_oci_apigateway_anonymous_route_authorization_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_route_authorization_policy_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_ANY_OF_ROUTE_AUTHORIZATION_POLICY_T Type

If authentication has been performed, validate whether the request scope (if any) applies to this route.

Syntax
```

```

`dbms_cloud_oci_apigateway_any_of_route_authorization_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_route_authorization_policy_t`type.

Fields

Field Description

`allowed_scope`

(required) A user whose scope includes any of these access ranges is allowed on this route. Access ranges are case-sensitive.

### DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_SELECTION_KEY_T Type

Base policy for defining how to match the context variable in an incoming request with selection keys when dynamically routing and dynamically authenticating requests.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Type of the selection key.

Allowed values are: 'ANY_OF', 'WILDCARD'

`is_default`

(optional) Specifies whether to use the route or authentication server associated with this selection key as the default. The default is used if the value of a context variable in an incoming request does not match any of the other selection key values when dynamically routing and dynamically authenticating requests.

`name`

(required) Name assigned to the branch.

### DBMS_CLOUD_OCI_APIGATEWAY_ANY_OF_SELECTION_KEY_T Type

When dynamically routing and dynamically authenticating requests, the route or authentication server associated with a set of selection keys is used if the context variable in an incoming request exactly matches one of the keys in the set.

Syntax
```

```

`dbms_cloud_oci_apigateway_any_of_selection_key_t`is a subtype of the`dbms_cloud_oci_apigateway_dynamic_selection_key_t`type.

Fields

Field Description

`l_values`

(optional) The set of selection keys to match with the context variable in an incoming request. If the context variable exactly matches one of the keys in the set, the request is sent to the route or authentication server associated with the set.

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_RESULT_T Type

The result of single validation.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the validation.

`result`

(required) Result of the validation.

Allowed values are: 'ERROR', 'WARNING', 'OK', 'FAILED'

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_RESULT_TBL Type

Nested table type of dbms_cloud_oci_apigateway_api_validation_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_API_T Type

An API is simple container for an API Specification. For more information, see[API Gateway Concepts](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the API.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current lifecycleState in more detail. For ACTIVE state it describes if the document has been validated and the possible values are: - 'New' for just updated API Specifications - 'Validating' for a document which is being validated. - 'Valid' the document has been validated without any errors or warnings - 'Warning' the document has been validated and contains warnings - 'Error' the document has been validated and contains errors - 'Failed' the document validation failed - 'Canceled' the document validation was canceled For other states it may provide more details like actionable information.

`specification_type`

(optional) Type of API Specification file.

`validation_results`

(optional) Status of each feature available from the API.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_API_SUMMARY_T Type

A summary of the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the API.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current lifecycleState in more detail. For ACTIVE state it describes if the document has been validated and the possible values are: - 'New' for just updated API Specifications - 'Validating' for a document which is being validated. - 'Valid' the document has been validated without any errors or warnings - 'Warning' the document has been validated and contains warnings - 'Error' the document has been validated and contains errors - 'Failed' the document validation failed - 'Canceled' the document validation was canceled For other states it may provide more details like actionable information.

`specification_type`

(optional) Type of API Specification file.

`validation_results`

(optional) Status of each feature available from the API.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_API_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_api_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_API_COLLECTION_T Type

Collection of API summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) API summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_POLICY_T Type

Information on how to authenticate incoming requests.

Syntax
```

```

Fields

Field Description

`is_anonymous_access_allowed`

(optional) Whether an unauthenticated user may access the API. Must be \"true\" to enable ANONYMOUS route authorization.

`l_type`

(required) Type of the authentication policy to use.

Allowed values are: 'CUSTOM_AUTHENTICATION', 'JWT_AUTHENTICATION', 'TOKEN_AUTHENTICATION'

### DBMS_CLOUD_OCI_APIGATEWAY_RATE_LIMITING_POLICY_T Type

Limit the number of requests that should be handled for the specified window using a specfic key.

Syntax
```

```

Fields

Field Description

`rate_in_requests_per_second`

(required) The maximum number of requests per second to allow.

`rate_key`

(required) The key used to group requests together.

Allowed values are: 'CLIENT_IP', 'TOTAL'

### DBMS_CLOUD_OCI_APIGATEWAY_CORS_POLICY_T Type

Enable CORS (Cross-Origin-Resource-Sharing) request handling.

Syntax
```

```

Fields

Field Description

`allowed_origins`

(required) The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the scheme, full hostname, and port if necessary.

`allowed_methods`

(optional) The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the Access-Control-Allow-Methods header. '*' will allow all methods.

`allowed_headers`

(optional) The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header. '*' will allow all headers.

`exposed_headers`

(optional) The list of headers that the client will be allowed to see from the response as indicated by the Access-Control-Expose-Headers header. '*' will expose all headers.

`is_allow_credentials_enabled`

(optional) Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.

`max_age_in_seconds`

(optional) The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age if greater than 0.

### DBMS_CLOUD_OCI_APIGATEWAY_MUTUAL_TLS_DETAILS_T Type

Properties used to configure client mTLS verification when API Consumer makes connection to the gateway.

Syntax
```

```

Fields

Field Description

`is_verified_certificate_required`

(optional) Determines whether to enable client verification when API Consumer makes connection to the gateway.

`allowed_sans`

(optional) Allowed list of CN or SAN which will be used for verification of certificate.

### DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLANS_POLICY_T Type

Usage plan policies for this deployment

Syntax
```

```

Fields

Field Description

`token_locations`

(required) A list of context variables specifying where API tokens may be located in a request. Example locations: - \"request.headers[token]\" - \"request.query[token]\" - \"request.auth[Token]\" - \"request.path[TOKEN]\"

### DBMS_CLOUD_OCI_APIGATEWAY_SELECTION_SOURCE_POLICY_T Type

The type of selector to use when dynamically routing and dynamically authenticating requests.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Selection source to use.

Allowed values are: 'SINGLE'

### DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_SERVER_POLICY_T Type

Policy for the details regarding each authentication server under dynamic authentication. We specify the value of selectors for which this authentication server must be selected for a request under keys. We specify the configuration details of authentication server under authenticationServerDetail.

Syntax
```

```

Fields

Field Description

`key`

(required)

`authentication_server_detail`

(required)

### DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_SERVER_POLICY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_authentication_server_policy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_AUTHENTICATION_POLICY_T Type

Policy on how to authenticate requests when multiple authentication options are configured for a deployment. For an incoming request, the value of selector specified under selectionSource will be matched against the keys specified for each authentication server. The authentication server whose key matches the value of selector will be used for authentication.

Syntax
```

```

Fields

Field Description

`selection_source`

(required)

`authentication_servers`

(required) List of authentication servers to choose from during dynamic authentication.

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_REQUEST_POLICIES_T Type

Global behavior applied to all requests received by the API.

Syntax
```

```

Fields

Field Description

`authentication`

(optional)

`rate_limiting`

(optional)

`cors`

(optional)

`mutual_tls`

(optional)

`usage_plans`

(optional)

`dynamic_authentication`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_EXECUTION_LOG_POLICY_T Type

Configures the logging policies for the execution logs of an API Deployment.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket. Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket. Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.

`log_level`

(optional) Specifies the log level used to control logging output of execution logs. Enabling logging at a given level also enables logging at all higher levels.

Allowed values are: 'INFO', 'WARN', 'ERROR'

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_LOGGING_POLICIES_T Type

Policies controlling the pushing of logs to OCI Public Logging.

Syntax
```

```

Fields

Field Description

`access_log`

(optional)

`execution_log`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_ITEM_T Type

Query parameter validation properties.

Syntax
```

```

Fields

Field Description

`required`

(optional) Determines if the parameter is required in the request.

`name`

(required) Parameter name.

### DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_query_parameter_validation_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_REQUEST_POLICY_T Type

Validate the URL query parameters on the incoming API requests on a specific route.

Syntax
```

```

Fields

Field Description

`parameters`

(optional)

`validation_mode`

(optional) Validation behavior mode. In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend. In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path. `DISABLED` type turns the validation off.

Allowed values are: 'ENFORCING', 'PERMISSIVE', 'DISABLED'

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_ITEM_T Type

Header validation properties.

Syntax
```

```

Fields

Field Description

`required`

(optional) Determines if the header is required in the request.

`name`

(required) Parameter name.

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_header_validation_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_REQUEST_POLICY_T Type

Validate the HTTP headers on the incoming API requests on a specific route.

Syntax
```

```

Fields

Field Description

`headers`

(optional)

`validation_mode`

(optional) Validation behavior mode. In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend. In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path. `DISABLED` type turns the validation off.

Allowed values are: 'ENFORCING', 'PERMISSIVE', 'DISABLED'

### DBMS_CLOUD_OCI_APIGATEWAY_CONTENT_VALIDATION_T Type

Content validation properties.

Syntax
```

```

Fields

Field Description

`validation_type`

(required) Validation type defines the content validation method. Make the validation to first parse the body as the respective format.

Allowed values are: 'NONE'

### DBMS_CLOUD_OCI_APIGATEWAY_BODY_VALIDATION_REQUEST_POLICY_T Type

Validate the payload body of the incoming API requests on a specific route.

Syntax
```

```

Fields

Field Description

`required`

(optional) Determines if the request body is required in the request.

`content`

(required) The content of the request body. The key is a[media type range](https://tools.ietf.org/html/rfc7231#appendix-D)subset restricted to the following schema key ::= ( / ( \"*\" \"/\" \"*\" ) / ( type \"/\" \"*\" ) / ( type \"/\" subtype ) ) For requests that match multiple keys, only the most specific key is applicable. e.g. `text/plain` overrides `text/*`

`validation_mode`

(optional) Validation behavior mode. In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend. In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path. `DISABLED` type turns the validation off.

Allowed values are: 'ENFORCING', 'PERMISSIVE', 'DISABLED'

### DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_ITEM_T Type

Set will add a new header if it was not in the original request. If the header already exists on the request, you can choose to override, append, or skip it.

Syntax
```

```

Fields

Field Description

`name`

(required) The case-insensitive name of the header. This name must be unique across transformation policies.

`l_values`

(required) A list of new values. Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.

`if_exists`

(optional) If a header with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.

Allowed values are: 'OVERWRITE', 'APPEND', 'SKIP'

### DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_set_header_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_T Type

Set HTTP headers as they pass through the gateway.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of headers.

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_ITEM_T Type

The value will be a copy of the original value of the source header and will not be affected by any other transformation policies applied to that header.

Syntax
```

```

Fields

Field Description

`l_from`

(required) The original case-insensitive name of the header. This name must be unique across transformation policies.

`l_to`

(required) The new name of the header. This name must be unique across transformation policies.

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_rename_header_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_T Type

Rename HTTP headers as they pass through the gateway.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of headers.

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_ITEM_T Type

A header to drop (with BLOCK) or pass through (with ALLOW).

Syntax
```

```

Fields

Field Description

`name`

(required) The case-insensitive name of the header. This name must be unique across transformation policies.

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_filter_header_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_T Type

Filter HTTP headers as they pass through the gateway. The gateway applies filters after other transformations, so any headers set or renamed must also be listed here when using an ALLOW type policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) BLOCK drops any headers that are in the list of items, so it acts as an exclusion list. ALLOW permits only the headers in the list and removes all others, so it acts as an inclusion list.

Allowed values are: 'ALLOW', 'BLOCK'

`items`

(required) The list of headers.

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_TRANSFORMATION_POLICY_T Type

A set of transformations to apply to HTTP headers that pass through the gateway.

Syntax
```

```

Fields

Field Description

`set_headers`

(optional)

`rename_headers`

(optional)

`filter_headers`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_ITEM_T Type

Set will add a new query parameter if it was not in the original request. If the parameter already exists on the request, you can choose to override, append, or skip it.

Syntax
```

```

Fields

Field Description

`name`

(required) The case-sensitive name of the query parameter. This name must be unique across transformation policies.

`l_values`

(required) A list of new values. Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.

`if_exists`

(optional) If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.

Allowed values are: 'OVERWRITE', 'APPEND', 'SKIP'

### DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_set_query_parameter_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_T Type

Set parameters on the query string as they pass through the gateway.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of query parameters.

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_ITEM_T Type

The value will be a copy of the original value of the source parameter and will not be affected by any other transformation policies applied to that parameter.

Syntax
```

```

Fields

Field Description

`l_from`

(required) The original case-sensitive name of the query parameter. This name must be unique across transformation policies.

`l_to`

(required) The new name of the query parameter. This name must be unique across transformation policies.

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_rename_query_parameter_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_T Type

Rename parameters on the query string as they pass through the gateway.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of query parameters.

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_ITEM_T Type

A query parameter to drop (with BLOCK) or pass through (with ALLOW).

Syntax
```

```

Fields

Field Description

`name`

(required) The case-sensitive name of the query parameter.

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_ITEM_TBL Type

Nested table type of dbms_cloud_oci_apigateway_filter_query_parameter_policy_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_T Type

Filter parameters from the query string as they pass through the gateway. The gateway applies filters after other transformations, so any parameters set or renamed must also be listed here when using an ALLOW type policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list. ALLOW permits only the parameters in the list and removes all others, so it acts as an inclusion list.

Allowed values are: 'ALLOW', 'BLOCK'

`items`

(required) The list of query parameters.

### DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_TRANSFORMATION_POLICY_T Type

A set of transformations to apply to query parameters that pass through the gateway.

Syntax
```

```

Fields

Field Description

`set_query_parameters`

(optional)

`rename_query_parameters`

(optional)

`filter_query_parameters`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_LOOKUP_POLICY_T Type

Base policy for Response Cache lookup.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Response Cache Store Policy.

Allowed values are: 'SIMPLE_LOOKUP_POLICY'

`is_enabled`

(optional) Whether this policy is currently enabled.

`is_private_caching_enabled`

(optional) Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your cache key additions to get the level of isolation across authenticated requests that you require. When false, any request with an Authorization header will not be stored in the Response Cache. If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_REQUEST_POLICIES_T Type

Behavior applied to any requests received by the API on this route.

Syntax
```

```

Fields

Field Description

`authorization`

(optional)

`cors`

(optional)

`query_parameter_validations`

(optional)

`header_validations`

(optional)

`body_validation`

(optional)

`header_transformations`

(optional)

`query_parameter_transformations`

(optional)

`response_cache_lookup`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_STORE_POLICY_T Type

Base policy for how a response from a backend is cached in the Response Cache.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Response Cache Store Policy.

Allowed values are: 'FIXED_TTL_STORE_POLICY'

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_RESPONSE_POLICIES_T Type

Behavior applied to any responses sent by the API for requests on this route.

Syntax
```

```

Fields

Field Description

`header_transformations`

(optional)

`response_cache_store`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_BACKEND_T Type

The backend to forward requests to.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the API backend.

Allowed values are: 'ORACLE_FUNCTIONS_BACKEND', 'HTTP_BACKEND', 'STOCK_RESPONSE_BACKEND', 'DYNAMIC_ROUTING_BACKEND', 'OAUTH2_LOGOUT_BACKEND'

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_T Type

A single route that forwards requests to a particular backend and may contain some additional policies.

Syntax
```

```

Fields

Field Description

`path`

(required) A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers to allow wildcard and parameterized matching.

`methods`

(optional) A list of allowed methods on this route.

Allowed values are: 'ANY', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'

`request_policies`

(optional)

`response_policies`

(optional)

`logging_policies`

(optional)

`backend`

(required)

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_TBL Type

Nested table type of dbms_cloud_oci_apigateway_api_specification_route_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_T Type

The logical configuration of the API exposed by a deployment.

Syntax
```

```

Fields

Field Description

`request_policies`

(optional)

`logging_policies`

(optional)

`routes`

(optional) A list of routes that this API exposes.

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAIL_T Type

Detail of a single error or warning.

Syntax
```

```

Fields

Field Description

`msg`

(optional) Description of the warning/error.

`severity`

(optional) Severity of the issue.

Allowed values are: 'INFO', 'WARNING', 'ERROR'

`src`

(optional) Position of the issue in the specification file (line, column).

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_apigateway_api_validation_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAILS_T Type

Detail of an error or warning.

Syntax
```

```

Fields

Field Description

`details`

(optional) Details of validation.

`name`

(required) Name of the validation.

`result`

(required) Result of the validation.

Allowed values are: 'ERROR', 'WARNING', 'OK', 'FAILED'

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_apigateway_api_validation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATIONS_T Type

The result of validations conducted on the API.

Syntax
```

```

Fields

Field Description

`validations`

(required) API validation results.

### DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_ONLY_ROUTE_AUTHORIZATION_POLICY_T Type

Only authentication is performed for the request and authorization is skipped.

Syntax
```

```

`dbms_cloud_oci_apigateway_authentication_only_route_authorization_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_route_authorization_policy_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_CA_BUNDLE_T Type

Reference to the CA bundle that should be used on the gateway

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the CA bundle

Allowed values are: 'CA_BUNDLE', 'CERTIFICATE_AUTHORITY'

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_T Type

A certificate contains information to be installed on a gateway to secure the traffic going through it. For more information, see[API Gateway Concepts](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`subject_names`

(required) The entity to be secured by the certificate and additional host names.

`time_not_valid_after`

(required) The date and time the certificate will expire.

`certificate`

(required) The data of the leaf certificate in pem format.

`intermediate_certificates`

(optional) The intermediate certificate data associated with the certificate in pem format.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the certificate.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_SUMMARY_T Type

A summary of the certificate.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`subject_names`

(required) The entity to be secured by the certificate and additional host names.

`time_not_valid_after`

(required) The date and time the certificate will expire.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the certificate.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_certificate_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_COLLECTION_T Type

Collection of certificate summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Certificate summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATES_CA_BUNDLE_T Type

CA bundle from Certificates Service that should be used on the gateway for TLS validation

Syntax
```

```

`dbms_cloud_oci_apigateway_certificates_ca_bundle_t`is a subtype of the`dbms_cloud_oci_apigateway_ca_bundle_t`type.

Fields

Field Description

`ca_bundle_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

### DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATES_CERTIFICATE_AUTHORITY_T Type

Certificate Authority from Certificates Service that should be used on the gateway for TLS validation

Syntax
```

```

`dbms_cloud_oci_apigateway_certificates_certificate_authority_t`is a subtype of the`dbms_cloud_oci_apigateway_ca_bundle_t`type.

Fields

Field Description

`certificate_authority_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_API_COMPARTMENT_DETAILS_T Type

The new compartment details for the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_CERTIFICATE_COMPARTMENT_DETAILS_T Type

The new compartment details for the certificate.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_DEPLOYMENT_COMPARTMENT_DETAILS_T Type

The new compartment details for the deployment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_GATEWAY_COMPARTMENT_DETAILS_T Type

The new compartment details for the gateway.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_SUBSCRIBER_COMPARTMENT_DETAILS_T Type

The new compartment details for the subscriber.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_USAGE_PLAN_COMPARTMENT_DETAILS_T Type

The new compartment details for the usage plan.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

### DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_T Type

A Client.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the client. Must be unique within a subscriber.

`token`

(required) The token for the client. Must be unique within a tenancy.

### DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_APP_DETAILS_T Type

Client App Credential details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) To specify where the Client App details should be taken from.

Allowed values are: 'VALIDATION_BLOCK', 'CUSTOM'

### DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_SUMMARY_T Type

A summary of a client.

Syntax
```

```

Fields

Field Description

`name`

(required) The client name.

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_API_DETAILS_T Type

Information about the new API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`content`

(optional) API Specification content in json or yaml format

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_CERTIFICATE_DETAILS_T Type

Information about a new certificate.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`private_key`

(required) The private key associated with the certificate in pem format.

`certificate`

(required) The data of the leaf certificate in pem format.

`intermediate_certificates`

(optional) The intermediate certificate data associated with the certificate in pem format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_DEPLOYMENT_DETAILS_T Type

Information about a new deployment.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`path_prefix`

(required) A path on which to deploy all routes contained in the API deployment specification. For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

`specification`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_DETAILS_T Type

Base Gateway response cache.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Response Cache.

Allowed values are: 'EXTERNAL_RESP_CACHE', 'NONE'

### DBMS_CLOUD_OCI_APIGATEWAY_CA_BUNDLE_TBL Type

Nested table type of dbms_cloud_oci_apigateway_ca_bundle_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_GATEWAY_DETAILS_T Type

Information about the new gateway.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`endpoint_type`

(required) Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be accessible on a private IP address on the subnet. Example: `PUBLIC` or `PRIVATE`

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet in which related resources are created.

`network_security_group_ids`

(optional) An array of Network Security Groups OCIDs associated with this API Gateway.

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`response_cache_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`ca_bundles`

(optional) An array of CA bundles that should be used on the Gateway for TLS validation.

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_SDK_DETAILS_T Type

Information about the new SDK.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`target_language`

(required) The string representing the target programming language for generating the SDK.

`api_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of API resource

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`parameters`

(optional) Additional optional configurations that can be passed to generate SDK Api. The applicable parameters are listed under \"parameters\" when \"/sdkLanguageTypes\" is called. Example: `{\"configName\": \"configValue\"}`

### DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_TBL Type

Nested table type of dbms_cloud_oci_apigateway_client_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_SUBSCRIBER_DETAILS_T Type

Information about a new subscriber.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`clients`

(required) The clients belonging to this subscriber.

`usage_plans`

(required) An array of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of usage plan resources.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_RATE_LIMIT_T Type

Rate-limiting policy for a usage plan.

Syntax
```

```

Fields

Field Description

`value`

(required) The number of requests that can be made per time period.

`unit`

(required) The unit of time over which rate limits are calculated. Example: `SECOND`

Allowed values are: 'SECOND'

### DBMS_CLOUD_OCI_APIGATEWAY_QUOTA_T Type

Quota policy for a usage plan.

Syntax
```

```

Fields

Field Description

`value`

(required) The number of requests that can be made per time period.

`unit`

(required) The unit of time over which quotas are calculated. Example: `MINUTE` or `MONTH`

Allowed values are: 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH'

`reset_policy`

(required) The policy that controls when quotas will reset. Example: `CALENDAR`

Allowed values are: 'CALENDAR'

`operation_on_breach`

(required) What the usage plan will do when a quota is breached: `REJECT` will allow no further requests `ALLOW` will continue to allow further requests

Allowed values are: 'REJECT', 'ALLOW'

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TARGET_T Type

An entitlement target, describing which deployment the entitlement should be applied to.

Syntax
```

```

Fields

Field Description

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a deployment resource.

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TARGET_TBL Type

Nested table type of dbms_cloud_oci_apigateway_entitlement_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_T Type

A usage plan entitlement, comprising of rate limits, quotas and the deployments they are applied to.

Syntax
```

```

Fields

Field Description

`name`

(required) An entitlement name, unique within a usage plan.

`description`

(optional) A user-friendly description. To provide some insight about the resource. Avoid entering confidential information.

`rate_limit`

(optional)

`quota`

(optional)

`targets`

(optional) A collection of targeted deployments that the entitlement will be applied to.

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TBL Type

Nested table type of dbms_cloud_oci_apigateway_entitlement_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_CREATE_USAGE_PLAN_DETAILS_T Type

Information about a new usage plan.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`entitlements`

(required) A collection of entitlements to assign to the newly created usage plan.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_FAILURE_POLICY_T Type

Policy for defining behaviour on validation failure.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Validation failure Policy.

Allowed values are: 'MODIFY_RESPONSE', 'OAUTH2'

### DBMS_CLOUD_OCI_APIGATEWAY_CUSTOM_AUTHENTICATION_POLICY_T Type

Use a function to validate a custom header or query parameter sent with the request authentication. A valid policy must specify either tokenHeader or tokenQueryParam.

Syntax
```

```

`dbms_cloud_oci_apigateway_custom_authentication_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_authentication_policy_t`type.

Fields

Field Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Functions function resource.

`token_header`

(optional) The name of the header containing the authentication token.

`token_query_param`

(optional) The name of the query parameter containing the authentication token.

`parameters`

(optional) A map where key is a user defined string and value is a context expressions whose values will be sent to the custom auth function. Values should contain an expression. Example: `{\"foo\": \"request.header[abc]\"}`

`cache_key`

(optional) A list of keys from \"parameters\" attribute value whose values will be added to the cache key.

`validation_failure_policy`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_CUSTOM_CLIENT_APP_DETAILS_T Type

Client App Credentials to be provided again.

Syntax
```

```

`dbms_cloud_oci_apigateway_custom_client_app_details_t`is a subtype of the`dbms_cloud_oci_apigateway_client_app_details_t`type.

Fields

Field Description

`client_id`

(required) Client ID for the OAuth2/OIDC app.

`client_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Vault Service secret resource.

`client_secret_version_number`

(required) The version number of the client secret to use.

### DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_T Type

A deployment deploys an API on a gateway. Avoid entering confidential information. For more information, see[API Gateway Concepts](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`path_prefix`

(required) A path on which to deploy all routes contained in the API deployment specification. For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

`endpoint`

(required) The endpoint to access this deployment on the gateway.

`specification`

(required)

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the deployment.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_SUMMARY_T Type

A summary of the deployment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`path_prefix`

(required) The path on which all routes contained in the API deployment specification are deployed. For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

`endpoint`

(required) The endpoint to access this deployment on the gateway.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the deployment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_deployment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_COLLECTION_T Type

Collection of deployment summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Deployment summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_SOURCE_URI_DETAILS_T Type

Auth endpoint details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the Uri detail.

Allowed values are: 'DISCOVERY_URI', 'VALIDATION_BLOCK'

### DBMS_CLOUD_OCI_APIGATEWAY_DISCOVERY_URI_SOURCE_URI_DETAILS_T Type

Discovery Uri information.

Syntax
```

```

`dbms_cloud_oci_apigateway_discovery_uri_source_uri_details_t`is a subtype of the`dbms_cloud_oci_apigateway_source_uri_details_t`type.

Fields

Field Description

`uri`

(required) The discovery URI for the auth server.

### DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_TYPE_ROUTING_BACKEND_T Type

Policy for the details regarding each routing backend under dynamic routing. We specify the value of selectors for which this routing backend must be selected for a request under keys. We specify the configuration details of routing backend under backend.

Syntax
```

```

Fields

Field Description

`key`

(required)

`backend`

(required)

### DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_TYPE_ROUTING_BACKEND_TBL Type

Nested table type of dbms_cloud_oci_apigateway_dynamic_routing_type_routing_backend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_BACKEND_T Type

Send the request to the backend dynamically selected based on the incoming request's context.

Syntax
```

```

`dbms_cloud_oci_apigateway_dynamic_routing_backend_t`is a subtype of the`dbms_cloud_oci_apigateway_api_specification_route_backend_t`type.

Fields

Field Description

`selection_source`

(required)

`routing_backends`

(required) List of backends to chose from for Dynamic Routing.

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_SUMMARY_T Type

A summary of an entitlement included in a usage plan.

Syntax
```

```

Fields

Field Description

`name`

(required) An entitlement name, unique within a usage plan.

`description`

(optional) A user-friendly description. To provide some insight about the resource. Avoid entering confidential information.

`rate_limit`

(optional)

`quota`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_ERROR_T Type

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

### DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_RESP_SERVER_T Type

Details of a RESP based cache store server

Syntax
```

```

Fields

Field Description

`host`

(required) Hostname or IP address (IPv4 only) where the cache store is running.

`port`

(required) The port the cache store is exposed on.

### DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_RESP_SERVER_TBL Type

Nested table type of dbms_cloud_oci_apigateway_response_cache_resp_server_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_EXTERNAL_RESP_CACHE_T Type

Connection details for an external RESP based cache store for Response Caching.

Syntax
```

```

`dbms_cloud_oci_apigateway_external_resp_cache_t`is a subtype of the`dbms_cloud_oci_apigateway_response_cache_details_t`type.

Fields

Field Description

`servers`

(required) The set of cache store members to connect to. At present only a single server is supported.

`authentication_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Vault Service secret resource.

`authentication_secret_version_number`

(required) The version number of the authentication secret to use.

`is_ssl_enabled`

(optional) Defines if the connection should be over SSL.

`is_ssl_verify_disabled`

(optional) Defines whether or not to uphold SSL verification.

`connect_timeout_in_ms`

(optional) Defines the timeout for establishing a connection with the Response Cache.

`read_timeout_in_ms`

(optional) Defines the timeout for reading data from the Response Cache.

`send_timeout_in_ms`

(optional) Defines the timeout for transmitting data to the Response Cache.

### DBMS_CLOUD_OCI_APIGATEWAY_FIXED_TTL_RESPONSE_CACHE_STORE_POLICY_T Type

How a response from a backend is cached in the Response Cache.

Syntax
```

```

`dbms_cloud_oci_apigateway_fixed_ttl_response_cache_store_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_response_cache_store_policy_t`type.

Fields

Field Description

`time_to_live_in_seconds`

(required) Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.

### DBMS_CLOUD_OCI_APIGATEWAY_IP_ADDRESS_T Type

IP address associated with the gateway.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) An IP address.

### DBMS_CLOUD_OCI_APIGATEWAY_IP_ADDRESS_TBL Type

Nested table type of dbms_cloud_oci_apigateway_ip_address_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_T Type

A gateway is a virtual network appliance in a regional subnet. A gateway routes inbound traffic to back-end services including public, private, and partner HTTP APIs, as well as Oracle Functions. Avoid entering confidential information. For more information, see[API Gateway Concepts](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`endpoint_type`

(required) Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be accessible on a private IP address on the subnet. Example: `PUBLIC` or `PRIVATE`

Allowed values are: 'PUBLIC', 'PRIVATE'

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet in which related resources are created.

`network_security_group_ids`

(optional) An array of Network Security Groups OCIDs associated with this API Gateway.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the gateway.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`hostname`

(optional) The hostname for APIs deployed on the gateway.

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`ip_addresses`

(optional) An array of IP addresses associated with the gateway.

`response_cache_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`ca_bundles`

(optional) An array of CA bundles that should be used on the Gateway for TLS validation.

### DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_SUMMARY_T Type

A summary of the gateway.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`endpoint_type`

(required) Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be accessible on a private IP address on the subnet. Example: `PUBLIC` or `PRIVATE`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet in which related resources are created.

`network_security_group_ids`

(optional) An array of Network Security Groups OCIDs associated with this API Gateway.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the gateway.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`hostname`

(optional) The hostname for the APIs deployed on the gateway.

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_gateway_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_COLLECTION_T Type

Collection of gateway summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Gateway summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_HTTP_BACKEND_T Type

Send the request to an HTTP backend.

Syntax
```

```

`dbms_cloud_oci_apigateway_http_backend_t`is a subtype of the`dbms_cloud_oci_apigateway_api_specification_route_backend_t`type.

Fields

Field Description

`url`

(required)

`connect_timeout_in_seconds`

(optional) Defines a timeout for establishing a connection with a proxied server.

`read_timeout_in_seconds`

(optional) Defines a timeout for reading a response from the proxied server.

`send_timeout_in_seconds`

(optional) Defines a timeout for transmitting a request to the proxied server.

`is_ssl_verify_disabled`

(optional) Defines whether or not to uphold SSL verification.

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_FIELD_SPECIFICATION_T Type

Header in key/value pair.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the header.

`value`

(optional) Value of the header.

### DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_T Type

A static public key which is used to verify the JWT signature.

Syntax
```

```

Fields

Field Description

`kid`

(required) A unique key ID. This key will be used to verify the signature of a JWT with matching \"kid\".

`format`

(required) The format of the public key.

Allowed values are: 'JSON_WEB_KEY', 'PEM'

### DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_KEY_T Type

A JSON Web Key that represents the public key used for verifying the JWT signature.

Syntax
```

```

`dbms_cloud_oci_apigateway_json_web_key_t`is a subtype of the`dbms_cloud_oci_apigateway_static_public_key_t`type.

Fields

Field Description

`kty`

(required) The key type.

Allowed values are: 'RSA'

`use`

(optional) The intended use of the public key.

Allowed values are: 'sig'

`key_ops`

(optional) The operations for which this key is to be used.

Allowed values are: 'verify'

`alg`

(required) The algorithm intended for use with this key.

`n`

(required) The base64 url encoded modulus of the RSA public key represented by this key.

`e`

(required) The base64 url encoded exponent of the RSA public key represented by this key.

### DBMS_CLOUD_OCI_APIGATEWAY_PUBLIC_KEY_SET_T Type

A set of Public Keys that will be used to verify the JWT signature.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the public key set.

Allowed values are: 'STATIC_KEYS', 'REMOTE_JWKS'

### DBMS_CLOUD_OCI_APIGATEWAY_JWT_AUTHENTICATION_POLICY_T Type

Validate a JWT token present in the header or query parameter. A valid policy must specify either tokenHeader or tokenQueryParam.

Syntax
```

```

`dbms_cloud_oci_apigateway_jwt_authentication_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_authentication_policy_t`type.

Fields

Field Description

`token_header`

(optional) The name of the header containing the authentication token.

`token_query_param`

(optional) The name of the query parameter containing the authentication token.

`token_auth_scheme`

(optional) The authentication scheme that is to be used when authenticating the token. This must to be provided if \"tokenHeader\" is specified.

`max_clock_skew_in_seconds`

(optional) The maximum expected time difference between the system clocks of the token issuer and the API Gateway.

`issuers`

(required) A list of parties that could have issued the token.

`audiences`

(required) The list of intended recipients for the token.

`verify_claims`

(optional) A list of claims which should be validated to consider the token valid.

`public_keys`

(required)

### DBMS_CLOUD_OCI_APIGATEWAY_MODIFY_RESPONSE_VALIDATION_FAILURE_POLICY_T Type

Policy to specify how to modify the response code, body and headers.

Syntax
```

```

`dbms_cloud_oci_apigateway_modify_response_validation_failure_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_validation_failure_policy_t`type.

Fields

Field Description

`response_code`

(optional) HTTP response code, can include context variables.

`response_message`

(optional) HTTP response message.

`response_header_transformations`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_NO_CACHE_T Type

Configures the gateway with no caching. Cache lookup and store policies will not be supported.

Syntax
```

```

`dbms_cloud_oci_apigateway_no_cache_t`is a subtype of the`dbms_cloud_oci_apigateway_response_cache_details_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_NO_CONTENT_VALIDATION_T Type

No content validation properties.

Syntax
```

```

`dbms_cloud_oci_apigateway_no_content_validation_t`is a subtype of the`dbms_cloud_oci_apigateway_content_validation_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_O_AUTH2_LOGOUT_BACKEND_T Type

Backend which when called triggers OAuth2 logout.

Syntax
```

```

`dbms_cloud_oci_apigateway_o_auth2_logout_backend_t`is a subtype of the`dbms_cloud_oci_apigateway_api_specification_route_backend_t`type.

Fields

Field Description

`allowed_post_logout_uris`

(optional)

`post_logout_state`

(optional) Defines a state that should be shared on redirecting to postLogout URL.

### DBMS_CLOUD_OCI_APIGATEWAY_O_AUTH2_RESPONSE_VALIDATION_FAILURE_POLICY_T Type

Policy to specify OAuth2 flow configuration.

Syntax
```

```

`dbms_cloud_oci_apigateway_o_auth2_response_validation_failure_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_validation_failure_policy_t`type.

Fields

Field Description

`client_details`

(required)

`source_uri_details`

(required)

`scopes`

(required) List of scopes.

`max_expiry_duration_in_hours`

(optional) The duration for which the OAuth2 success token should be cached before it is fetched again.

`use_cookies_for_session`

(optional) Defines whether or not to use cookies for session maintenance.

`use_cookies_for_intermediate_steps`

(optional) Defines whether or not to use cookies for OAuth2 intermediate steps.

`use_pkce`

(optional) Defines whether or not to support PKCE.

`response_type`

(required) Response Type.

Allowed values are: 'CODE'

`fallback_redirect_path`

(optional) The path to be used as fallback after OAuth2.

`logout_path`

(optional) The path to be used as logout.

### DBMS_CLOUD_OCI_APIGATEWAY_ORACLE_FUNCTION_BACKEND_T Type

Send the request to an Oracle Functions function.

Syntax
```

```

`dbms_cloud_oci_apigateway_oracle_function_backend_t`is a subtype of the`dbms_cloud_oci_apigateway_api_specification_route_backend_t`type.

Fields

Field Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Functions function resource.

### DBMS_CLOUD_OCI_APIGATEWAY_PEM_ENCODED_PUBLIC_KEY_T Type

A PEM-encoded public key used for verifying the JWT signature.

Syntax
```

```

`dbms_cloud_oci_apigateway_pem_encoded_public_key_t`is a subtype of the`dbms_cloud_oci_apigateway_static_public_key_t`type.

Fields

Field Description

`key`

(required) The content of the PEM-encoded public key.

### DBMS_CLOUD_OCI_APIGATEWAY_REMOTE_JSON_WEB_KEY_SET_T Type

A set of public keys that is retrieved at run-time from a remote location to verify the JWT signature. The set should only contain JWK-formatted keys.

Syntax
```

```

`dbms_cloud_oci_apigateway_remote_json_web_key_set_t`is a subtype of the`dbms_cloud_oci_apigateway_public_key_set_t`type.

Fields

Field Description

`uri`

(required) The uri from which to retrieve the key. It must be accessible without authentication.

`is_ssl_verify_disabled`

(optional) Defines whether or not to uphold SSL verification.

`max_cache_duration_in_hours`

(optional) The duration for which the JWKS should be cached before it is fetched again.

### DBMS_CLOUD_OCI_APIGATEWAY_REQUEST_PARAMETER_VALIDATION_T Type

Common parameter validation properties.

Syntax
```

```

Fields

Field Description

`name`

(required) Parameter name.

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_T Type

Information about the SDK.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`api_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of API resource

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(optional) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`target_language`

(required) The string representing the target programming language for generating the SDK.

`artifact_url`

(optional) File location for generated SDK.

`time_artifact_url_expires_at`

(optional) Expiry of artifact url.

`lifecycle_state`

(optional) The current state of the SDK. - The SDK will be in CREATING state if the SDK creation is in progress. - The SDK will be in ACTIVE state if create is successful. - The SDK will be in FAILED state if the create, or delete fails. - The SDK will be in DELETING state if the deletion in in progress. - The SDK will be in DELETED state if the delete is successful.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`parameters`

(optional) Additional optional configurations passed. The applicable config keys are listed under \"parameters\" when \"/sdkLanguageTypes\" is called. Example: `{\"configName\": \"configValue\"}`

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_SUMMARY_T Type

A summary of the SDK.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time this resource was last updated. An RFC3339 formatted datetime string.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`target_language`

(required) The string representing the target programming language for generating the SDK.

`lifecycle_state`

(optional) The current state of the SDK.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_sdk_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_COLLECTION_T Type

Collection of the existing SDKs.

Syntax
```

```

Fields

Field Description

`items`

(required) SDK summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_ALLOWED_VALUE_T Type

Allowed value object.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the allowed value.

`description`

(optional) Description for the allowed value.

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_ALLOWED_VALUE_TBL Type

Nested table type of dbms_cloud_oci_apigateway_sdk_language_optional_parameters_allowed_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_T Type

List of additional applicable parameters for any given target language.

Syntax
```

```

Fields

Field Description

`param_name`

(required) Name of the parameter.

`display_name`

(optional) Display name of the parameter.

`description`

(optional) Description for the parameter.

`is_required`

(optional) Information on whether the parameter is required or not.

`max_size`

(optional) Maximum size as input value for this parameter.

`input_type`

(optional) The input type for this param. - Input type is ENUM when only specific list of input strings are allowed. - Input type is EMAIL when input type is an email ID. - Input type is URI when input type is an URI. - Input type is STRING in all other cases.

Allowed values are: 'ENUM', 'EMAIL', 'URI', 'STRING'

`allowed_values`

(optional) List of allowed input values. Example: `[{\"name\": \"name1\", \"description\": \"description1\"}, ...]`

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_TBL Type

Nested table type of dbms_cloud_oci_apigateway_sdk_language_optional_parameters_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_SUMMARY_T Type

SDK target language details.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the programming language.

`display_name`

(optional) Display name of the target programming language.

`version`

(required) Version string of the programming language defined in name.

`description`

(optional) Additional details.

`parameters`

(optional) List of optional configurations that can be used while generating SDK for the given target language.

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_sdk_language_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_COLLECTION_T Type

Collection of available SDK target languages.

Syntax
```

```

Fields

Field Description

`items`

(required) SDK target language details.

### DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPES_T Type

SDK target language details.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the programming language.

`display_name`

(optional) Display name of the target programming language.

`version`

(required) Version string of the programming language defined in name.

`description`

(optional) Additional details.

`parameters`

(optional) List of optional configurations that can be used while generating SDK for the given target language.

### DBMS_CLOUD_OCI_APIGATEWAY_SIMPLE_LOOKUP_POLICY_T Type

Provides ability to vary the cache key using context expressions.

Syntax
```

```

`dbms_cloud_oci_apigateway_simple_lookup_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_response_cache_lookup_policy_t`type.

Fields

Field Description

`cache_key_additions`

(optional) A list of context expressions whose values will be added to the base cache key. Values should contain an expression enclosed within ${} delimiters. Only the request context is available.

### DBMS_CLOUD_OCI_APIGATEWAY_SINGLE_SELECTION_SOURCE_POLICY_T Type

The single context variable in an incoming request to match against specified selection keys when dynamically routing and dynamically authenticating requests.

Syntax
```

```

`dbms_cloud_oci_apigateway_single_selection_source_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_selection_source_policy_t`type.

Fields

Field Description

`selector`

(required) String describing the context variable used as selector.

### DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_static_public_key_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_SET_T Type

A set of static public keys that will be used to verify the JWT signature.

Syntax
```

```

`dbms_cloud_oci_apigateway_static_public_key_set_t`is a subtype of the`dbms_cloud_oci_apigateway_public_key_set_t`type.

Fields

Field Description

`keys`

(optional) The set of static public keys.

### DBMS_CLOUD_OCI_APIGATEWAY_HEADER_FIELD_SPECIFICATION_TBL Type

Nested table type of dbms_cloud_oci_apigateway_header_field_specification_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_STOCK_RESPONSE_BACKEND_T Type

Send the request to a mock backend.

Syntax
```

```

`dbms_cloud_oci_apigateway_stock_response_backend_t`is a subtype of the`dbms_cloud_oci_apigateway_api_specification_route_backend_t`type.

Fields

Field Description

`body`

(optional) The body of the stock response from the mock backend.

`status`

(required) The status code of the stock response from the mock backend.

`headers`

(optional) The headers of the stock response from the mock backend.

### DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_T Type

A subscriber, which encapsulates a number of clients and usage plans that they are subscribed to.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`clients`

(required) The clients belonging to this subscriber.

`usage_plans`

(required) An array of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of usage plan resources.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the subscriber.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_client_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_SUMMARY_T Type

A summary of a subscriber.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`clients`

(required) The clients belonging to this subscriber.

`usage_plans`

(required) An array of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of usage plan resources.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the subscriber.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_subscriber_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_COLLECTION_T Type

Collection of subscriber summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Subscriber summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_VALIDATION_POLICY_T Type

Authentication Policies for the Token Authentication types.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the token validation policy.

Allowed values are: 'STATIC_KEYS', 'REMOTE_JWKS', 'REMOTE_DISCOVERY'

`additional_validation_policy`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_POLICY_T Type

Validate a token present in the header or query parameter. A valid policy must specify either tokenHeader or tokenQueryParam.

Syntax
```

```

`dbms_cloud_oci_apigateway_token_authentication_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_authentication_policy_t`type.

Fields

Field Description

`token_header`

(optional) The name of the header containing the authentication token.

`token_query_param`

(optional) The name of the query parameter containing the authentication token.

`token_auth_scheme`

(optional) The authentication scheme that is to be used when authenticating the token. This must to be provided if \"tokenHeader\" is specified.

`max_clock_skew_in_seconds`

(optional) The maximum expected time difference between the system clocks of the token issuer and the API Gateway.

`validation_policy`

(required)

`validation_failure_policy`

(optional)

### DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_REMOTE_DISCOVERY_VALIDATION_POLICY_T Type

Instrospect Url based validation retrieved at run-time from a remote location to verify the provided token.

Syntax
```

```

`dbms_cloud_oci_apigateway_token_authentication_remote_discovery_validation_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_token_authentication_validation_policy_t`type.

Fields

Field Description

`client_details`

(required)

`source_uri_details`

(required)

`is_ssl_verify_disabled`

(optional) Defines whether or not to uphold SSL verification.

`max_cache_duration_in_hours`

(optional) The duration for which the introspect URL response should be cached before it is fetched again.

### DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_REMOTE_JWKS_VALIDATION_POLICY_T Type

A set of public keys that is retrieved at run-time from a remote location to verify the JWT signature. The set should only contain JWK-formatted keys.

Syntax
```

```

`dbms_cloud_oci_apigateway_token_authentication_remote_jwks_validation_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_token_authentication_validation_policy_t`type.

Fields

Field Description

`uri`

(required) The uri from which to retrieve the key. It must be accessible without authentication.

`is_ssl_verify_disabled`

(optional) Defines whether or not to uphold SSL verification.

`max_cache_duration_in_hours`

(optional) The duration for which the JWKS should be cached before it is fetched again.

### DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_STATIC_KEYS_VALIDATION_POLICY_T Type

A set of static public keys that will be used to verify the JWT signature.

Syntax
```

```

`dbms_cloud_oci_apigateway_token_authentication_static_keys_validation_policy_t`is a subtype of the`dbms_cloud_oci_apigateway_token_authentication_validation_policy_t`type.

Fields

Field Description

`keys`

(optional) The set of static public keys.

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_API_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`content`

(optional) API Specification content in json or yaml format

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_CERTIFICATE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_DEPLOYMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`specification`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_GATEWAY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`network_security_group_ids`

(optional) An array of Network Security Groups OCIDs associated with this API Gateway.

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`response_cache_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`ca_bundles`

(optional) An array of CA bundles that should be used on the Gateway for TLS validation.

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_SDK_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_SUBSCRIBER_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`clients`

(optional) The clients belonging to the subscriber.

`usage_plans`

(optional) An array of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of usage plan resources.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_USAGE_PLAN_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`entitlements`

(optional) A collection of entitlements to update the current usage plan with.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_T Type

A usage plan controls access of subscribers to deployments, controlling rate limits and quotas for usage.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a usage plan resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`entitlements`

(required) A collection of entitlements currently assigned to the usage plan.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the usage plan.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_entitlement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_SUMMARY_T Type

A summary of the usage plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a usage plan resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. Example: `My new resource`

`entitlements`

(required) A collection of entitlements applied by the usage plan.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`time_created`

(required) The time this resource was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this resource was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the usage plan.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_usage_plan_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_COLLECTION_T Type

Collection of usage plan summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Usage plan summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_BLOCK_CLIENT_APP_DETAILS_T Type

Client App Credentials to be used from validation block.

Syntax
```

```

`dbms_cloud_oci_apigateway_validation_block_client_app_details_t`is a subtype of the`dbms_cloud_oci_apigateway_client_app_details_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_BLOCK_SOURCE_URI_DETAILS_T Type

Source Uri information to be used from validation block.

Syntax
```

```

`dbms_cloud_oci_apigateway_validation_block_source_uri_details_t`is a subtype of the`dbms_cloud_oci_apigateway_source_uri_details_t`type.

### DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_REQUEST_POLICY_T Type

Top-level validation policy mixin (not directly used).

Syntax
```

```

Fields

Field Description

`validation_mode`

(optional) Validation behavior mode. In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend. In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path. `DISABLED` type turns the validation off.

Allowed values are: 'ENFORCING', 'PERMISSIVE', 'DISABLED'

### DBMS_CLOUD_OCI_APIGATEWAY_WILDCARD_SELECTION_KEY_T Type

When dynamically routing and dynamically authenticating requests, the route or authentication server associated with a selection key containing a wildcard is used if the context variable in an incoming request matches that key.

Syntax
```

```

`dbms_cloud_oci_apigateway_wildcard_selection_key_t`is a subtype of the`dbms_cloud_oci_apigateway_dynamic_selection_key_t`type.

Fields

Field Description

`expression`

(required) A selection key string containing a wildcard to match with the context variable in an incoming request. If the context variable matches the string, the request is sent to the route or authentication server associated with the selection key. Valid wildcards are '*' (zero or more characters) and '+' (one or more characters). The string can only contain one wildcard, and the wildcard must be at the start or the end of the string.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource; at which point, it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path on which the user can perform a GET operation to access the resource metadata.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_apigateway_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_GATEWAY', 'UPDATE_GATEWAY', 'DELETE_GATEWAY', 'CREATE_DEPLOYMENT', 'UPDATE_DEPLOYMENT', 'DELETE_DEPLOYMENT', 'CREATE_CERTIFICATE', 'UPDATE_CERTIFICATE', 'DELETE_CERTIFICATE', 'CREATE_API', 'UPDATE_API', 'DELETE_API', 'VALIDATE_API', 'CREATE_SDK', 'DELETE_SDK', 'CREATE_USAGE_PLAN', 'UPDATE_USAGE_PLAN', 'DELETE_USAGE_PLAN', 'CREATE_SUBSCRIBER', 'UPDATE_SUBSCRIBER', 'DELETE_SUBSCRIBER'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

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

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_SUMMARY_T Type

A summary of the work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

`status`

(required) The status of the work request.

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the resource is created.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apigateway_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_COLLECTION_T Type

Collection of work request summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request summaries.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. See &lt;a href=\"/Content/API/References/apierrors.htm\"&gt;API Errors&lt;/a&gt;.

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_apigateway_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_COLLECTION_T Type

Collection of work request errors.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request errors.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_TBL Type

Nested table type of dbms_cloud_oci_apigateway_work_request_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_COLLECTION_T Type

Collection of work request logs.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request logs.

- [API Gateway Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A8915597-2E3F-4AD3-8B08-5FC003372DDC)
- [DBMS_CLOUD_OCI_APIGATEWAY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B9FD6921-EE3D-442B-9FD3-8443496D2920)
- [DBMS_CLOUD_OCI_APIGATEWAY_ACCESS_LOG_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-F991648F-55BE-4F11-9F18-B87013C718B6)
- [DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_TOKEN_CLAIM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B214E45A-C3C2-4A17-BFA1-9A6D209023D4)
- [DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_TOKEN_CLAIM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-AFA702A8-C308-49FA-A6E4-204201310E13)
- [DBMS_CLOUD_OCI_APIGATEWAY_ADDITIONAL_VALIDATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D706DE32-8A5C-41C6-BA76-6325A6CA5D0C)
- [DBMS_CLOUD_OCI_APIGATEWAY_ROUTE_AUTHORIZATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C69980E7-28BA-4C59-BFFF-4FA92E57697E)
- [DBMS_CLOUD_OCI_APIGATEWAY_ANONYMOUS_ROUTE_AUTHORIZATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-78E11F31-159C-4131-9DA5-2A2F6C5B1615)
- [DBMS_CLOUD_OCI_APIGATEWAY_ANY_OF_ROUTE_AUTHORIZATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-0A80B64C-5D65-43DE-9681-E0250E36EB53)
- [DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_SELECTION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-40E0EFAB-BB1D-42C0-ADDF-A7137BB26E64)
- [DBMS_CLOUD_OCI_APIGATEWAY_ANY_OF_SELECTION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3A83D45C-C3CA-4A87-8F67-E926E9357D09)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1CBB3F80-6AFD-4861-9D0D-58EE2EB26BCE)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B70195D3-7DA0-4E8F-84BB-52E7E09713B4)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A822A938-1A1D-45D5-A716-1963BD19EB7A)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-185F6566-0E31-4A6F-A0E5-B236EDA12143)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B6930CC4-5A11-4CC3-A9AB-AFBD8BAFFF87)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-DBF79194-BDF7-45E4-9BE4-62B59F8AE4AC)
- [DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4D92B95C-0DA1-4401-AD75-66B60E142560)
- [DBMS_CLOUD_OCI_APIGATEWAY_RATE_LIMITING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D73313C1-8D7D-420E-B461-F56162D1CD8C)
- [DBMS_CLOUD_OCI_APIGATEWAY_CORS_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-0DB72904-9463-486B-A8E0-EE335C351DC4)
- [DBMS_CLOUD_OCI_APIGATEWAY_MUTUAL_TLS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-431A99B0-FD4D-46E7-91BA-ADB5655DD4B2)
- [DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLANS_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-58FE4DD2-8992-4DA8-B085-38A6EE2D4FF4)
- [DBMS_CLOUD_OCI_APIGATEWAY_SELECTION_SOURCE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-97C198F2-50E1-4929-9A72-A0F11F00B1E8)
- [DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_SERVER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A7E2801C-A18B-4C2C-8815-480FA4B56218)
- [DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_SERVER_POLICY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1CD502F1-7F5B-42C1-9D49-19F2BE771F1B)
- [DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4246A62A-82D4-494F-A914-8A000CEC5D8D)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_REQUEST_POLICIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-009964D4-A77D-49DD-97FD-6F3DD1143031)
- [DBMS_CLOUD_OCI_APIGATEWAY_EXECUTION_LOG_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-950C8E5A-433D-46B3-90B0-AF6834CDA9EB)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_LOGGING_POLICIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D1CB6FB9-3D0F-490A-AC51-0A71CB0FA62E)
- [DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-CA55C42A-11CF-4E32-9AAD-89831A6A609A)
- [DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BFD79063-D7E7-4E97-ACF9-250D35215136)
- [DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_VALIDATION_REQUEST_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-86012347-B244-41B1-8D37-19BA454B0256)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-50CBA1F3-0F1E-470F-838F-4EC45C1512D3)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-7A867670-6A92-42D5-A5D5-2C2EA7CC21AD)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_VALIDATION_REQUEST_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9D3BF869-C231-4AAE-80FA-38E4817027ED)
- [DBMS_CLOUD_OCI_APIGATEWAY_CONTENT_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-13395681-F761-48F3-9E63-B1AA69790D51)
- [DBMS_CLOUD_OCI_APIGATEWAY_BODY_VALIDATION_REQUEST_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C7B211CD-F9F3-4F45-A194-77D96DA9E8DC)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-99143489-884C-4E61-AD41-26993648875A)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-85E1C9C5-79C6-4CCF-908F-5CA587DDBB11)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_HEADER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-82D62D09-A535-4CB8-889A-71AB15A3401B)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-59B272E4-F0C0-4362-88C3-4FB8C1BDD5B9)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-97A1A61B-FB0F-4D9A-98D4-6867E64C1171)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_HEADER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-47FFB88C-E601-455B-AE6F-FF877241AD9D)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C1A8F26B-B2C0-4806-ADB7-2AA3E847427F)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E273C349-3B7E-4D93-A5AA-2074EA143974)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_HEADER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B8E35B77-04D7-4C57-9971-5D31B5C9BD4B)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_TRANSFORMATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9A6B4A8E-8FF3-4A99-A763-64ED3A5BB7E0)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-762A8AFB-7644-48F8-B115-575A8FD474D0)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-888E22E7-6741-451E-A36B-81BF3054D71A)
- [DBMS_CLOUD_OCI_APIGATEWAY_SET_QUERY_PARAMETER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-29B91F15-EFDA-440B-90A8-BAE54BF41310)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-742E69F4-DA05-4329-9D1C-B23BE2A4B254)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FFCFD53A-22C1-47EA-9E4D-E3DB3FBD912D)
- [DBMS_CLOUD_OCI_APIGATEWAY_RENAME_QUERY_PARAMETER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-54D8F6DC-A61D-464C-86F1-B86C27A44E9C)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-966C07BF-BE5E-463C-A548-A26B6B71BB10)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-6325CFA5-6261-472B-A783-9C3F79A2C9B1)
- [DBMS_CLOUD_OCI_APIGATEWAY_FILTER_QUERY_PARAMETER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3758973E-E173-4131-9B7F-B016D6941C15)
- [DBMS_CLOUD_OCI_APIGATEWAY_QUERY_PARAMETER_TRANSFORMATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-43E9EB57-666F-410C-AB07-B57484CA8492)
- [DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_LOOKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-F10F9D9A-E3C8-42DA-A92C-A262F250FD67)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_REQUEST_POLICIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-0CCF3302-86B0-40AC-85A0-3587A48A200A)
- [DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_STORE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D5A7A04F-3913-476B-B203-7F07F11EF47E)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_RESPONSE_POLICIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-82DB4DC7-1DB9-4947-87F1-EC3CC3B7C2F0)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-8128C2F4-4F2B-4F06-BB50-32D2EA65E974)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4DB9828F-42AA-4A58-9E8C-07EDCFE16EAC)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_ROUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-ACCE1AE0-2FE0-460B-8584-65A8552E7C19)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_SPECIFICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-33125D57-BEB5-493E-82E5-E152183AAEE5)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9274B89E-9600-43E3-8E3C-009F3723B028)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FE7C700F-045B-407B-BA45-8CEAC5B4726B)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FFCAE41C-EAA7-406D-B3D8-D87F622E7EE8)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C5A56874-336C-457C-847D-69AFB6E2F2B0)
- [DBMS_CLOUD_OCI_APIGATEWAY_API_VALIDATIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-72F80014-4A10-41AD-9665-003D6D7AB388)
- [DBMS_CLOUD_OCI_APIGATEWAY_AUTHENTICATION_ONLY_ROUTE_AUTHORIZATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B7379FB1-EE57-41D6-8AF6-485E9CBCBEB7)
- [DBMS_CLOUD_OCI_APIGATEWAY_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E24DB575-8F0C-4D3F-9469-2DB7ED494652)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-96B7EEEB-9E6D-4E9D-8CE4-854DFA6CA3F4)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-2063316E-61EE-43FE-BFB0-FF8BAF9354C1)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-2AEC05F4-1887-4150-B71E-BC536BBCBDB9)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-89D3B066-E166-48BE-A654-447EF3A27AFA)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATES_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-7BFF760B-4604-4647-9E78-9C7E1B2BACDD)
- [DBMS_CLOUD_OCI_APIGATEWAY_CERTIFICATES_CERTIFICATE_AUTHORITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-F993F136-2E55-40C2-8139-54170EE37781)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_API_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A9DD0C8F-5C50-498F-9127-61324FE9A595)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_CERTIFICATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-608BC500-2E11-4F73-8215-76407249B448)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_DEPLOYMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-71761B1B-4A34-45E4-B25C-A80A49CEB227)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D7A9F847-5BB8-4D07-9F36-0CE6A5C3AA86)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_SUBSCRIBER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-11A9532C-D1F7-44B2-8166-71D6C323CA74)
- [DBMS_CLOUD_OCI_APIGATEWAY_CHANGE_USAGE_PLAN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-801B8D6A-318D-49FA-9519-3D34698E7329)
- [DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-EF2845E3-966F-41F8-9339-E62E9012EE9A)
- [DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_APP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3E34E1A8-0503-4224-849A-40ABD7731F51)
- [DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-15EBD2FC-E1E9-4A8F-A42A-BB7B910CB3B7)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_API_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FDB43CF1-3478-4722-9CA7-D164491C108F)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-632E8245-6D10-4A83-BD48-6FD37404BA2D)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BF65C24B-D304-4320-9B7E-4506B358E1EB)
- [DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-12615ABE-EB67-453B-B791-4BFEA46CD694)
- [DBMS_CLOUD_OCI_APIGATEWAY_CA_BUNDLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-EEDF1483-34E1-43CC-9229-ABEFFEC7CEA6)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-824A7EB2-0E6A-4A17-826A-9BD52B9E7FB0)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_SDK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-599DBE74-0BC8-4F15-AB98-591625E7B82F)
- [DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4B8B5AE0-D814-4B65-976E-CE5AD63B51E5)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_SUBSCRIBER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-7A3D9DA3-736F-4DF3-948E-A81E4F077488)
- [DBMS_CLOUD_OCI_APIGATEWAY_RATE_LIMIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-EAF5765F-B15B-4FE9-9A90-4D248DAC0D6A)
- [DBMS_CLOUD_OCI_APIGATEWAY_QUOTA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A9ACAFD9-E5C3-45E4-B032-B5AFB715AFC0)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-7837B692-4144-4C7F-8091-B1BA21F13CF1)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1C83DCAB-BE99-4840-928F-33B36AFBFF31)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-8EF152CB-8D18-4BC8-9D4E-84A11DF96659)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E39836D6-34A6-450B-AD62-5ECCAC1D07D1)
- [DBMS_CLOUD_OCI_APIGATEWAY_CREATE_USAGE_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-458838EE-B44E-4FAB-BD1D-5F69F7C23367)
- [DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_FAILURE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-328F56A3-F1A2-4098-A86E-12AAE880B699)
- [DBMS_CLOUD_OCI_APIGATEWAY_CUSTOM_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A0E7DC03-8D50-4B71-B1AE-B13730D9D576)
- [DBMS_CLOUD_OCI_APIGATEWAY_CUSTOM_CLIENT_APP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-55F64F3E-EF9B-4516-9682-D55C4C080C67)
- [DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FAF3B218-67BE-43C1-B04D-E093B8B38695)
- [DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-363F37F8-1535-4F70-8002-7B141464101A)
- [DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-96F31FB7-D742-4134-927C-DFFC4A94D35A)
- [DBMS_CLOUD_OCI_APIGATEWAY_DEPLOYMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-8332BA0A-D2FE-4A00-B477-B20745678BAF)
- [DBMS_CLOUD_OCI_APIGATEWAY_SOURCE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-16D15F18-E1B6-435C-A241-CA9960AB2FAB)
- [DBMS_CLOUD_OCI_APIGATEWAY_DISCOVERY_URI_SOURCE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-6543A01F-7599-4014-936D-984DB6324D1A)
- [DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_TYPE_ROUTING_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B20060E7-00B8-42C3-9665-7CAFEC6BE4F6)
- [DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_TYPE_ROUTING_BACKEND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-944EEFBE-97FA-4020-B891-CB66AC1CC00F)
- [DBMS_CLOUD_OCI_APIGATEWAY_DYNAMIC_ROUTING_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-41C20DA9-5268-48A6-BEFD-673F17C3BE23)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-F37E55DC-0E72-43B2-AC5C-E84D373CFB6A)
- [DBMS_CLOUD_OCI_APIGATEWAY_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D3715E9E-A2A1-4227-BA48-E67484689D2F)
- [DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_RESP_SERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3A6049A7-C9EE-402C-8ECC-87C1C5A4CF53)
- [DBMS_CLOUD_OCI_APIGATEWAY_RESPONSE_CACHE_RESP_SERVER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-5A107DD3-B12F-43E4-9960-DC8E3E7BAF0E)
- [DBMS_CLOUD_OCI_APIGATEWAY_EXTERNAL_RESP_CACHE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C20EAB6D-4377-4783-8AD8-2412865145B9)
- [DBMS_CLOUD_OCI_APIGATEWAY_FIXED_TTL_RESPONSE_CACHE_STORE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-B8D8BCE4-BB30-4BE0-8A35-1180ECEAD4E3)
- [DBMS_CLOUD_OCI_APIGATEWAY_IP_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-CEC5B458-4FBB-4F94-B98C-A97B1758ED81)
- [DBMS_CLOUD_OCI_APIGATEWAY_IP_ADDRESS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-7219882A-080F-4E5F-A33F-9F2E93D8E482)
- [DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3F02D024-7729-4FBF-B4F9-C68C186D6879)
- [DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-488590A4-77D3-46A6-ABAD-2068DE4CCAED)
- [DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-5D6075FE-B259-4763-AB00-3C27B44C2AA0)
- [DBMS_CLOUD_OCI_APIGATEWAY_GATEWAY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BD8857AF-071C-4E45-8762-DC1F5DA62FFE)
- [DBMS_CLOUD_OCI_APIGATEWAY_HTTP_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-401465F4-00C9-4959-8CDC-6A081B743E45)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_FIELD_SPECIFICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4D58C2BD-1FD1-4888-AD6E-4B20DCD1A069)
- [DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9AD29E61-B680-40E1-A67E-AA1898FC3F05)
- [DBMS_CLOUD_OCI_APIGATEWAY_JSON_WEB_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BBD84680-E9DF-4EA4-B1C1-CEACFB12E0E7)
- [DBMS_CLOUD_OCI_APIGATEWAY_PUBLIC_KEY_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1A84F193-7148-4FEC-A1F8-48F3610B48D3)
- [DBMS_CLOUD_OCI_APIGATEWAY_JWT_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FB624723-0584-440D-AD83-040147A76190)
- [DBMS_CLOUD_OCI_APIGATEWAY_MODIFY_RESPONSE_VALIDATION_FAILURE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A476578F-BC03-48B0-8D3A-FE940C307DB4)
- [DBMS_CLOUD_OCI_APIGATEWAY_NO_CACHE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9AAC5AEC-2F6A-49A2-B8CD-1D2D3FF9EDBA)
- [DBMS_CLOUD_OCI_APIGATEWAY_NO_CONTENT_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4434670F-179B-4A54-913F-0E4EE78D30B8)
- [DBMS_CLOUD_OCI_APIGATEWAY_O_AUTH2_LOGOUT_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-63268614-724F-4106-B963-9A9D24DB91EA)
- [DBMS_CLOUD_OCI_APIGATEWAY_O_AUTH2_RESPONSE_VALIDATION_FAILURE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-06D9D158-15A4-498E-9477-53E4A2024422)
- [DBMS_CLOUD_OCI_APIGATEWAY_ORACLE_FUNCTION_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BEE6480F-486C-4073-A8A8-6D788ABF9E57)
- [DBMS_CLOUD_OCI_APIGATEWAY_PEM_ENCODED_PUBLIC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-398AEAF2-533C-4777-9693-C697EEE9DEA2)
- [DBMS_CLOUD_OCI_APIGATEWAY_REMOTE_JSON_WEB_KEY_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-97D18BDD-F31D-4778-B479-38CFF25848FE)
- [DBMS_CLOUD_OCI_APIGATEWAY_REQUEST_PARAMETER_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-8EA2923F-D451-4C26-B7B6-8813A8368055)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-FD5AC8BA-5578-4C82-8890-3C07334A5CE9)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C4EEABDE-77C5-4B5B-83C1-5B4F4B09AA08)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D144339E-987D-4309-909C-57E024DE422C)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-19F91BF7-D610-4AF8-BA8F-54F1360D562D)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_ALLOWED_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-5FF477C1-E8F1-40CA-BEC9-2D68E13E65FF)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_ALLOWED_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-DA9465EB-6D45-4B50-8545-6DBE596F3B5C)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-40FD2E91-B2DC-444D-8FC3-9BD5F1C1989F)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_OPTIONAL_PARAMETERS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E888421C-50CE-4AFC-8F4F-B01ACD140E8B)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D5A256F3-E8F8-4504-B720-857D6C575F69)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-EF88E67C-CAA3-462E-9589-9905C585E593)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3D4257D7-6F55-4F27-8606-A9239DF2622B)
- [DBMS_CLOUD_OCI_APIGATEWAY_SDK_LANGUAGE_TYPES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A759E1DE-F0BD-4572-94B1-0962849D28CB)
- [DBMS_CLOUD_OCI_APIGATEWAY_SIMPLE_LOOKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-30F25A7D-4660-474D-A78B-DA364361B31A)
- [DBMS_CLOUD_OCI_APIGATEWAY_SINGLE_SELECTION_SOURCE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-BC929948-A1DC-4772-B38C-FA520419EB0C)
- [DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-9B32CE42-F831-4872-A8C8-047ADF2BB4CE)
- [DBMS_CLOUD_OCI_APIGATEWAY_STATIC_PUBLIC_KEY_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-C8FFCAA3-A235-4D24-9838-1B06336B5696)
- [DBMS_CLOUD_OCI_APIGATEWAY_HEADER_FIELD_SPECIFICATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-35ACC877-64B2-4BEF-AD38-EE546A52BF54)
- [DBMS_CLOUD_OCI_APIGATEWAY_STOCK_RESPONSE_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-EE9B4995-FE74-4262-870E-9D88C3413D4F)
- [DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1770E939-F46C-4829-9E80-B232105063A7)
- [DBMS_CLOUD_OCI_APIGATEWAY_CLIENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-93294EE3-67A0-4D08-B90C-70736B6E9609)
- [DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-92453005-09A7-446F-A4EA-493C220DE8AA)
- [DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-68FE6A76-52E4-4C77-8B93-358F75864E04)
- [DBMS_CLOUD_OCI_APIGATEWAY_SUBSCRIBER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-282FE309-C053-4952-8390-87F29A7EEF12)
- [DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_VALIDATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-AC75DDC6-B3C3-49CD-B634-F04236A2C714)
- [DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A849EBAD-A90F-4C53-89C0-6ACCAB444FF2)
- [DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_REMOTE_DISCOVERY_VALIDATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A9AE96B9-EDD0-4792-9BDB-36CF8C84AD75)
- [DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_REMOTE_JWKS_VALIDATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D04EA790-C503-43A7-BEA9-7524C26D5387)
- [DBMS_CLOUD_OCI_APIGATEWAY_TOKEN_AUTHENTICATION_STATIC_KEYS_VALIDATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-25AA0773-6CE4-481F-B7EE-4F2DBDCE0AF0)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_API_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-6B1F79E5-5FD4-418C-9E53-5505DEDE9C62)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-F000473D-EB93-4478-A622-136AECB8A41E)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A13EF66F-077B-4511-9792-58D8BE9A4125)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A207E0AE-1F46-4936-A588-92FA054B5E00)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_SDK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E55DBD83-52AB-4461-8886-0A8643E12C19)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_SUBSCRIBER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4D18AE58-6132-4585-94C7-79D30E091F2D)
- [DBMS_CLOUD_OCI_APIGATEWAY_UPDATE_USAGE_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-3459F4AC-02CA-4523-B77F-C6F22D10F7DA)
- [DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-18F5CE50-41D8-429C-991D-CEBB2D4E83FB)
- [DBMS_CLOUD_OCI_APIGATEWAY_ENTITLEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-99D18CF5-A5C1-4E2D-94CD-89C09A7B1292)
- [DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-530FFA75-7B58-4BD1-B7C3-16A337F9E563)
- [DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-0DDA35BE-B360-4798-AEC8-BC0B76AB9E91)
- [DBMS_CLOUD_OCI_APIGATEWAY_USAGE_PLAN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-E00B1E99-BBBD-4794-B2F4-7DC19F9B1E0A)
- [DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_BLOCK_CLIENT_APP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-141EB65E-5805-4917-AB05-C37491E1F924)
- [DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_BLOCK_SOURCE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-AFC890E8-DB32-4EC7-A081-75F8A975BAC3)
- [DBMS_CLOUD_OCI_APIGATEWAY_VALIDATION_REQUEST_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-80FB03C1-5D7E-4CBA-9C07-AB283F1611FA)
- [DBMS_CLOUD_OCI_APIGATEWAY_WILDCARD_SELECTION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-91CEFF7F-2731-484A-94AF-AFD4D652ED6B)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-1BA7A7D6-8220-48ED-92FF-1C0A0B1B3419)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D1EBA959-F631-46D3-BAD4-93B310B9214B)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-821BC3F7-9254-481E-87A1-7563427E7646)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-8CE35D45-2E4F-4703-9F9B-04AB09615101)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-066D5B4B-FB9A-475A-A139-363EA799701A)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-81E8D4E3-8789-4567-A3DC-6190DBF04696)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-D61C013E-E7A0-485C-B98B-6CBB4387B673)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-026C9E26-3B36-473C-98DE-18ABA6EF2A6A)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-4878A64D-E511-4B1E-B2FD-9ADC77DE8AFF)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-CCC56882-6EA3-4320-83D4-AAFFEE3F2F10)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-984FC16E-C702-40C5-9788-A182FD1917CD)
- [DBMS_CLOUD_OCI_APIGATEWAY_WORK_REQUEST_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apigateway_t.html#ADSDK-GUID-A1F1334E-01A0-4BF1-A5A0-251D2DC86597)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
