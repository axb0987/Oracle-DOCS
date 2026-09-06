# Load Balancer Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#dcoc-content-body)

## Load Balancer Common Types

### DBMS_CLOUD_OCI_LOAD_BALANCER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_ACTION_T Type

An entity that represents an action to apply for a routing rule.

Syntax
```

```

Fields

Field Description

`name`

(required)

Allowed values are: 'FORWARD_TO_BACKENDSET'

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_T Type

An object that represents an action to apply to a listener.

Syntax
```

```

Fields

Field Description

`action`

(required)

Allowed values are: 'ADD_HTTP_REQUEST_HEADER', 'EXTEND_HTTP_REQUEST_HEADER_VALUE', 'REMOVE_HTTP_REQUEST_HEADER', 'ADD_HTTP_RESPONSE_HEADER', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE', 'REMOVE_HTTP_RESPONSE_HEADER', 'ALLOW', 'CONTROL_ACCESS_USING_HTTP_METHODS', 'REDIRECT', 'HTTP_HEADER'

### DBMS_CLOUD_OCI_LOAD_BALANCER_ADD_HTTP_REQUEST_HEADER_RULE_T Type

An object that represents the action of adding a header to a request. This rule applies only to HTTP listeners. **NOTES:** * If a matching header already exists in the request, the system removes all of its occurrences, and then adds the new header. * The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_add_http_request_header_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

`value`

(required) A header value that conforms to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_value`

### DBMS_CLOUD_OCI_LOAD_BALANCER_ADD_HTTP_RESPONSE_HEADER_RULE_T Type

An object that represents the action of adding a header to a response. This rule applies only to HTTP listeners. **NOTES:** * If a matching header already exists in the response, the system removes all of its occurrences, and then adds the new header. * The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_add_http_response_header_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

`value`

(required) A header value that conforms to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_value`

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_CONDITION_T Type

A condition to apply to an access control rule.

Syntax
```

```

Fields

Field Description

`attribute_name`

(required)

Allowed values are: 'SOURCE_IP_ADDRESS', 'SOURCE_VCN_ID', 'SOURCE_VCN_IP_ADDRESS', 'PATH'

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_CONDITION_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_rule_condition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_ALLOW_RULE_T Type

An object that represents the action of configuring an access control rule. Access control rules permit access to application resources based on user-specified match conditions. This rule applies only to HTTP listeners. **NOTES:** * If you do not specify any access control rules, the default rule is to allow all traffic. * If you add access control rules, the load balancer denies any traffic that does not match the rules. * Maximum of two match conditions can be specified in a rule. * You can specify this rule only with the following `RuleCondition` combinations: * `SOURCE_IP_ADDRESS` * `SOURCE_VCN_ID` * `SOURCE_VCN_ID\", \"SOURCE_VCN_IP_ADDRESS`

Syntax
```

```

`dbms_cloud_oci_load_balancer_allow_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`conditions`

(required)

`description`

(optional) A brief description of the access control rule. Avoid entering confidential information. example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_T Type

The configuration of a backend server that is a member of a load balancer backend set. For more information, see[Managing Backend Servers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A read-only field showing the IP address and port that uniquely identify this backend server in the backend set. Example: `10.0.0.3:8080`

`ip_address`

(required) The IP address of the backend server. Example: `10.0.0.3`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(required) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`drain`

(required) Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic. Example: `false`

`backup`

(required) Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy. **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy. Example: `false`

`l_offline`

(required) Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_DETAILS_T Type

The load balancing configuration details of a backend server.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The IP address of the backend server. Example: `10.0.0.3`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`backup`

(optional) Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy. **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy. Example: `false`

`drain`

(optional) Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic. Example: `false`

`l_offline`

(optional) Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECK_RESULT_T Type

Information about a single backend server health check result reported by a load balancer.

Syntax
```

```

Fields

Field Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet hosting the load balancer that reported this health check status.

`source_ip_address`

(required) The IP address of the health check status report provider. This identifier helps you differentiate same-subnet load balancers that report health check status. Example: `10.0.0.7`

`l_timestamp`

(required) The date and time the data was retrieved, in the format defined by RFC3339. Example: `2017-06-02T18:28:11+00:00`

`health_check_status`

(required) The result of the most recent health check.

Allowed values are: 'OK', 'INVALID_STATUS_CODE', 'TIMED_OUT', 'REGEX_MISMATCH', 'CONNECT_FAILED', 'IO_ERROR', 'OFFLINE', 'UNKNOWN'

### DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECK_RESULT_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_health_check_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_HEALTH_T Type

The health status of the specified backend server as reported by the primary and standby load balancers.

Syntax
```

```

Fields

Field Description

`status`

(required) The general health status of the specified backend server as reported by the primary and standby load balancers. * **OK:** Both health checks returned `OK`. * **WARNING:** One health check returned `OK` and one did not. * **CRITICAL:** Neither health check returned `OK`. * **UNKNOWN:** One or both health checks returned `UNKNOWN`, or the system was unable to retrieve metrics at this time.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`health_check_results`

(required) A list of the most recent health check results returned for the specified backend server.

### DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECKER_T Type

The health check policy configuration. For more information, see[Editing Health Check Policies](https://docs.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol the health check must use; either HTTP or TCP. Example: `HTTP`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`port`

(required) The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the `Backend` object. Example: `8080`

`return_code`

(required) The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, you can use common HTTP status codes such as \"200\". Example: `200`

`retries`

(optional) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. Defaults to 3. Example: `3`

`timeout_in_millis`

(optional) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Defaults to 3000 (3 seconds). Example: `3000`

`interval_in_millis`

(optional) The interval between health checks, in milliseconds. The default is 10000 (10 seconds). Example: `10000`

`response_body_regex`

(required) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`is_force_plain_text`

(optional) Specifies if health checks should always be done using plain text instead of depending on whether or not the associated backend set is using SSL. If \"true\", health checks will be done using plain text even if the associated backend set is configured to use SSL. If \"false\", health checks will be done using SSL encryption if the associated backend set is configured to use SSL. If the backend set is not so configured the health checks will be done using plain text. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CONFIGURATION_T Type

A listener's SSL handling configuration. To use SSL, a listener must be associated with a`CERTIFICATE`Type. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`verify_depth`

(required) The maximum depth for peer certificate chain verification. Example: `3`

`verify_peer_certificate`

(required) Whether the load balancer listener should verify peer certificates. Example: `true`

`trusted_certificate_authority_ids`

(optional) Ids for OCI certificates service CA or CA bundles for the load balancer to trust. Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`

`certificate_ids`

(optional) Ids for OCI certificates service certificates. Currently only a single Id may be passed. Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`

`certificate_name`

(optional) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information. Example: `example_certificate_bundle`

`server_order_preference`

(optional) When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client ciphers. **Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This field is ignored when the `SSLConfiguration` object is associated with a backend set.

Allowed values are: 'ENABLED', 'DISABLED'

`cipher_suite_name`

(optional) The name of the cipher suite to use for HTTPS or SSL connections. If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`. **Notes:** * You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. Clients cannot perform an SSL handshake if there is an incompatible configuration. * You must ensure compatibility between the ciphers configured in the cipher suite and the configured certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA certificates. * If the cipher configuration is not modified after load balancer creation, the `GET` operation returns `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners that predate this feature. * If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET` operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for existing listeners that predate this feature. * The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing backend sets that predate this feature. * If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field, you must specify an appropriate predefined or custom cipher suite name when updating the resource. * The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for this field. example: `example_cipher_suite`

`protocols`

(optional) A list of SSL protocols the load balancer must support for HTTPS or SSL connections. The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure connection ensures that all data passed between the client and the server is private. The Load Balancing service supports the following protocols: * TLSv1 * TLSv1.1 * TLSv1.2 If this field is not specified, TLSv1.2 is the default. **Warning:** All SSL listeners created on a given port must use the same set of SSL protocols. **Notes:** * The handshake to establish an SSL connection fails if the client supports none of the specified protocols. * You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. * For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation displays a list of SSL protocols currently used by those resources. example: `[\"TLSv1.1\", \"TLSv1.2\"]`

### DBMS_CLOUD_OCI_LOAD_BALANCER_SESSION_PERSISTENCE_CONFIGURATION_DETAILS_T Type

The configuration details for implementing session persistence based on a user-specified cookie name (application cookie stickiness). Session persistence enables the Load Balancing service to direct any number of requests that originate from a single logical client to a single backend web server. For more information, see[Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm). With application cookie stickiness, the load balancer enables session persistence only when the response from a backend application server includes a `Set-cookie` header with the user-specified cookie name. To disable application cookie stickiness on a running load balancer, use the`UPDATE_BACKEND_SET`Function operation and specify `null` for the `SessionPersistenceConfigurationDetails` object. Example: `SessionPersistenceConfigurationDetails: null` **Note:** `SessionPersistenceConfigurationDetails` (application cookie stickiness) and `LBCookieSessionPersistenceConfigurationDetails` (LB cookie stickiness) are mutually exclusive. An error results if you try to enable both types of session persistence. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`cookie_name`

(required) The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist. Example: `example_cookie`

`disable_fallback`

(optional) Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_LB_COOKIE_SESSION_PERSISTENCE_CONFIGURATION_DETAILS_T Type

The configuration details for implementing load balancer cookie session persistence (LB cookie stickiness). Session persistence enables the Load Balancing service to direct all requests that originate from a single logical client to a single backend web server. For more information, see[Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm). When you configure LB cookie stickiness, the load balancer inserts a cookie into the response. The parameters configured in the cookie enable session stickiness. This method is useful when you have applications and Web backend services that cannot generate their own cookies. Path route rules take precedence to determine the target backend server. The load balancer verifies that session stickiness is enabled for the backend server and that the cookie configuration (domain, path, and cookie hash) is valid for the target. The system ignores invalid cookies. To disable LB cookie stickiness on a running load balancer, use the`UPDATE_BACKEND_SET`Function operation and specify `null` for the `LBCookieSessionPersistenceConfigurationDetails` object. Example: `LBCookieSessionPersistenceConfigurationDetails: null` **Note:** `SessionPersistenceConfigurationDetails` (application cookie stickiness) and `LBCookieSessionPersistenceConfigurationDetails` (LB cookie stickiness) are mutually exclusive. An error results if you try to enable both types of session persistence. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`cookie_name`

(optional) The name of the cookie inserted by the load balancer. If this field is not configured, the cookie name defaults to \"X-Oracle-BMC-LBS-Route\". Example: `example_cookie` **Notes:** * Ensure that the cookie name used at the backend application servers is different from the cookie name used at the load balancer. To minimize the chance of name collision, Oracle recommends that you use a prefix such as \"X-Oracle-OCI-\" for this field. * If a backend server and the load balancer both insert cookies with the same name, the client or browser behavior can vary depending on the domain and path values associated with the cookie. If the name, domain, and path values of the `Set-cookie` generated by a backend server and the `Set-cookie` generated by the load balancer are all the same, the client or browser treats them as one cookie and returns only one of the cookie values in subsequent requests. If both `Set-cookie` names are the same, but the domain and path names are different, the client or browser treats them as two different cookies.

`disable_fallback`

(optional) Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false. Example: `false`

`domain`

(optional) The domain in which the cookie is valid. The `Set-cookie` header inserted by the load balancer contains a domain attribute with the specified value. This attribute has no default value. If you do not specify a value, the load balancer does not insert the domain attribute into the `Set-cookie` header. **Notes:** *[RFC 6265 - HTTP State Management Mechanism](https://www.ietf.org/rfc/rfc6265.txt)describes client and browser behavior when the domain attribute is present or not present in the `Set-cookie` header. If the value of the `Domain` attribute is `example.com` in the `Set-cookie` header, the client includes the same cookie in the `Cookie` header when making HTTP requests to `example.com`, `www.example.com`, and `www.abc.example.com`. If the `Domain` attribute is not present, the client returns the cookie only for the domain to which the original request was made. * Ensure that this attribute specifies the correct domain value. If the `Domain` attribute in the `Set-cookie` header does not include the domain to which the original request was made, the client or browser might reject the cookie. As specified in RFC 6265, the client accepts a cookie with the `Domain` attribute value `example.com` or `www.example.com` sent from `www.example.com`. It does not accept a cookie with the `Domain` attribute `abc.example.com` or `www.abc.example.com` sent from `www.example.com`. Example: `example.com`

`path`

(optional) The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path` attribute with the specified value. Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a subdirectory of, the cookie's `Path` attribute. The default value is `/`. Example: `/example`

`max_age_in_seconds`

(optional) The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains a `Max-Age` attribute with the specified value. The specified value must be at least one second. There is no default value for this attribute. If you do not specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In most cases, the client or browser retains the cookie until the current session ends, as defined by the client. Example: `3600`

`is_secure`

(optional) Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the cookie only using a secure protocol. **Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP listener. Example: `true`

`is_http_only`

(optional) Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP requests. This attribute directs the client or browser to omit the cookie when providing access to cookies through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels. Example: `true`

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_backend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_T Type

The configuration of a load balancer backend set. For more information on backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Note:** The `sessionPersistenceConfiguration` (application cookie stickiness) and `lbCookieSessionPersistenceConfiguration` (LB cookie stickiness) attributes are mutually exclusive. To avoid returning an error, configure only one of these two attributes per backend set. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the backend set. It must be unique and it cannot be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information. Example: `example_backend_set`

`policy`

(required) The load balancer policy for the backend set. To get a list of available policies, use the`LIST_POLICIES`Function operation. Example: `LEAST_CONNECTIONS`

`backends`

(required)

`health_checker`

(required)

`ssl_configuration`

(optional)

`session_persistence_configuration`

(optional)

`lb_cookie_session_persistence_configuration`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECKER_DETAILS_T Type

The health check policy's configuration details.

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol the health check must use; either HTTP or TCP. Example: `HTTP`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`port`

(optional) The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the `Backend` object. Example: `8080`

`return_code`

(optional) The status code a healthy backend server should return. Example: `200`

`retries`

(optional) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. Example: `3`

`timeout_in_millis`

(optional) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Example: `3000`

`interval_in_millis`

(optional) The interval between health checks, in milliseconds. Example: `10000`

`response_body_regex`

(optional) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`is_force_plain_text`

(optional) Specifies if health checks should always be done using plain text instead of depending on whether or not the associated backend set is using SSL. If \"true\", health checks will be done using plain text even if the associated backend set is configured to use SSL. If \"false\", health checks will be done using SSL encryption if the associated backend set is configured to use SSL. If the backend set is not so configured the health checks will be done using plain text. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CONFIGURATION_DETAILS_T Type

The load balancer's SSL handling configuration details. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`verify_depth`

(optional) The maximum depth for peer certificate chain verification. Example: `3`

`verify_peer_certificate`

(optional) Whether the load balancer listener should verify peer certificates. Example: `true`

`trusted_certificate_authority_ids`

(optional) Ids for OCI certificates service CA or CA bundles for the load balancer to trust. Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`

`certificate_ids`

(optional) Ids for OCI certificates service certificates. Currently only a single Id may be passed. Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`

`certificate_name`

(optional) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information. Example: `example_certificate_bundle`

`protocols`

(optional) A list of SSL protocols the load balancer must support for HTTPS or SSL connections. The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure connection ensures that all data passed between the client and the server is private. The Load Balancing service supports the following protocols: * TLSv1 * TLSv1.1 * TLSv1.2 If this field is not specified, TLSv1.2 is the default. **Warning:** All SSL listeners created on a given port must use the same set of SSL protocols. **Notes:** * The handshake to establish an SSL connection fails if the client supports none of the specified protocols. * You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. * For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation displays a list of SSL protocols currently used by those resources. example: `[\"TLSv1.1\", \"TLSv1.2\"]`

`cipher_suite_name`

(optional) The name of the cipher suite to use for HTTPS or SSL connections. If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`. **Notes:** * You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. Clients cannot perform an SSL handshake if there is an incompatible configuration. * You must ensure compatibility between the ciphers configured in the cipher suite and the configured certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA certificates. * If the cipher configuration is not modified after load balancer creation, the `GET` operation returns `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners that predate this feature. * If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET` operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for existing listeners that predate this feature. * The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing backend sets that predate this feature. * If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field, you must specify an appropriate predefined or custom cipher suite name when updating the resource. * The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for this field. example: `example_cipher_suite`

`server_order_preference`

(optional) When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client ciphers. **Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This field is ignored when the `SSLConfiguration` object is associated with a backend set.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_backend_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_DETAILS_T Type

The configuration details for a load balancer backend set. For more information on backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Note:** The `sessionPersistenceConfiguration` (application cookie stickiness) and `lbCookieSessionPersistenceConfiguration` (LB cookie stickiness) attributes are mutually exclusive. To avoid returning an error, configure only one of these two attributes per backend set.

Syntax
```

```

Fields

Field Description

`policy`

(required) The load balancer policy for the backend set. To get a list of available policies, use the`LIST_POLICIES`Function operation. Example: `LEAST_CONNECTIONS`

`backends`

(optional)

`health_checker`

(required)

`ssl_configuration`

(optional)

`session_persistence_configuration`

(optional)

`lb_cookie_session_persistence_configuration`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_HEALTH_T Type

The health status details for a backend set. This object does not explicitly enumerate backend servers with a status of `OK`. However, they are included in the `totalBackendCount` sum.

Syntax
```

```

Fields

Field Description

`status`

(required) Overall health status of the backend set. * **OK:** All backend servers in the backend set return a status of `OK`. * **WARNING:** Half or more of the backend set's backend servers return a status of `OK` and at least one backend server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`. * **CRITICAL:** Fewer than half of the backend set's backend servers return a status of `OK`. * **UNKNOWN:** More than half of the backend set's backend servers return a status of `UNKNOWN`, the system was unable to retrieve metrics, or the backend set does not have a listener attached.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`warning_state_backend_names`

(required) A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by IP address and port. Example: `10.0.0.3:8080`

`critical_state_backend_names`

(required) A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by IP address and port. Example: `10.0.0.4:8080`

`unknown_state_backend_names`

(required) A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by IP address and port. Example: `10.0.0.5:8080`

`total_backend_count`

(required) The total number of backend servers in this backend set. Example: `7`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CERTIFICATE_T Type

The configuration details of a certificate bundle. For more information on SSL certficate configuration, see[Managing SSL Certificates](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`certificate_name`

(required) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information. Example: `example_certificate_bundle`

`public_certificate`

(required) The public certificate, in PEM format, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw ... -----END CERTIFICATE-----

`ca_certificate`

(required) The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy ... -----END CERTIFICATE-----

### DBMS_CLOUD_OCI_LOAD_BALANCER_CERTIFICATE_DETAILS_T Type

The configuration details for a certificate bundle. For more information on SSL certficate configuration, see[Managing SSL Certificates](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`passphrase`

(optional) A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.

`private_key`

(optional) The SSL private key for your certificate, in PEM format. Example: -----BEGIN RSA PRIVATE KEY----- jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16 /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ ... -----END RSA PRIVATE KEY-----

`public_certificate`

(optional) The public certificate, in PEM format, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw ... -----END CERTIFICATE-----

`ca_certificate`

(optional) The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy ... -----END CERTIFICATE-----

`certificate_name`

(required) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information. Example: `example_certificate_bundle`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CHANGE_LOAD_BALANCER_COMPARTMENT_DETAILS_T Type

The configuration details for moving a load balancer to a different compartment. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the load balancer to.

### DBMS_CLOUD_OCI_LOAD_BALANCER_CONNECTION_CONFIGURATION_T Type

Configuration details for the connection between the client and backend servers.

Syntax
```

```

Fields

Field Description

`idle_timeout`

(required) The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations. For more information, see[Connection Configuration](https://docs.oracle.com/iaas/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration). Example: `1200`

`backend_tcp_proxy_protocol_version`

(optional) The backend TCP Proxy Protocol version. Example: `1`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CONTROL_ACCESS_USING_HTTP_METHODS_RULE_T Type

An object that represents the action of returning a specified response code when the requested HTTP method is not in the list of allowed methods for the listener. The load balancer does not forward a disallowed request to the back end servers. The default response code is `405 Method Not Allowed`. If you set the response code to `405` or leave it blank, the system adds an \"allow\" response header that contains a list of the allowed methods for the listener. If you set the response code to anything other than `405` (or blank), the system does not add the \"allow\" response header with a list of allowed methods. This rule applies only to HTTP listeners. No more than one `ControlAccessUsingHttpMethodsRule` object can be present in a given listener.

Syntax
```

```

`dbms_cloud_oci_load_balancer_control_access_using_http_methods_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`allowed_methods`

(required) The list of HTTP methods allowed for this listener. By default, you can specify only the standard HTTP methods defined in the[HTTP Method Registry](http://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also see a list of supported standard HTTP methods in the Load Balancing service documentation at[Managing Rule Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm). Your backend application must be able to handle the methods specified in this list. The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact[My Oracle Support](http://support.oracle.com/)to remove the restriction for your tenancy. Example: [\"GET\", \"PUT\", \"POST\", \"PROPFIND\"]

`status_code`

(optional) The HTTP status code to return when the requested HTTP method is not in the list of allowed methods. The associated status line returned with the code is mapped from the standard HTTP specification. The default value is `405 (Method Not Allowed)`. Example: 403

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_BACKEND_DETAILS_T Type

The configuration details for creating a backend server in a backend set. For more information on backend server configuration, see[Managing Backend Servers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm).

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The IP address of the backend server. Example: `10.0.0.3`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`backup`

(optional) Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy. **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy. Example: `false`

`drain`

(optional) Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic. Example: `false`

`l_offline`

(optional) Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_BACKEND_SET_DETAILS_T Type

The configuration details for creating a backend set in a load balancer. For more information on backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Note:** The `sessionPersistenceConfiguration` (application cookie stickiness) and `lbCookieSessionPersistenceConfiguration` (LB cookie stickiness) attributes are mutually exclusive. To avoid returning an error, configure only one of these two attributes per backend set. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the backend set. It must be unique and it cannot be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information. Example: `example_backend_set`

`policy`

(required) The load balancer policy for the backend set. To get a list of available policies, use the`LIST_POLICIES`Function operation. Example: `LEAST_CONNECTIONS`

`backends`

(optional)

`health_checker`

(required)

`ssl_configuration`

(optional)

`session_persistence_configuration`

(optional)

`lb_cookie_session_persistence_configuration`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_CERTIFICATE_DETAILS_T Type

The configuration details for adding a certificate bundle to a listener. For more information on SSL certficate configuration, see[Managing SSL Certificates](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`passphrase`

(optional) A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.

`private_key`

(optional) The SSL private key for your certificate, in PEM format. Example: -----BEGIN RSA PRIVATE KEY----- jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16 /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ ... -----END RSA PRIVATE KEY-----

`public_certificate`

(optional) The public certificate, in PEM format, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbM..QswCQYDVQQGEwJKU A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxE..TAPBgNVBAoTCEZyY MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWB..gNVBAMTD0ZyYW5rN YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmc..mFuazRkZC5jb20wH ... -----END CERTIFICATE-----

`ca_certificate`

(optional) The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider. Example: -----BEGIN CERTIFICATE----- MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy ... -----END CERTIFICATE-----

`certificate_name`

(required) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information. Example: `example_certificate_bundle`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_HOSTNAME_DETAILS_T Type

The details of the hostname resource to add to a load balancer. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_hostname_001`

`hostname`

(required) A virtual hostname. For more information about virtual hostname string construction, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm#routing). Example: `app.example.com`

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_LISTENER_DETAILS_T Type

The configuration details for adding a listener to a backend set. For more information on listener configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the`LIST_PROTOCOLS`Function operation. Example: `HTTP`

`hostname_names`

(optional) An array of hostname resource names.

`path_route_set_name`

(optional) Deprecated. Please use `routingPolicies` instead. The name of the set of path-based routing rules,`PATH_ROUTE_SET`Type, applied to this listener's traffic. Example: `example_path_route_set`

`ssl_configuration`

(optional)

`connection_configuration`

(optional)

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_listener`

`routing_policy_name`

(optional) The name of the routing policy applied to this listener's traffic. Example: `example_routing_policy`

`rule_set_names`

(optional) The names of the`RULE_SET`Type to apply to the listener. Example: [\"example_rule_set\"]

### DBMS_CLOUD_OCI_LOAD_BALANCER_SHAPE_DETAILS_T Type

The configuration details to update load balancer to a different shape.

Syntax
```

```

Fields

Field Description

`minimum_bandwidth_in_mbps`

(required) Bandwidth in Mbps that determines the total pre-provisioned bandwidth (ingress plus egress). The values must be between 10 and the maximumBandwidthInMbps. Example: `150`

`maximum_bandwidth_in_mbps`

(required) Bandwidth in Mbps that determines the maximum bandwidth (ingress plus egress) that the load balancer can achieve. This bandwidth cannot be always guaranteed. For a guaranteed bandwidth use the minimumBandwidthInMbps parameter. The values must be between minimumBandwidthInMbps and 8000 (8Gbps). Example: `1500`

### DBMS_CLOUD_OCI_LOAD_BALANCER_RESERVED_IP_T Type

Syntax
```

```

Fields

Field Description

`id`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_DETAILS_T Type

The listener's configuration details.

Syntax
```

```

Fields

Field Description

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the`LIST_PROTOCOLS`Function operation. Example: `HTTP`

`hostname_names`

(optional) An array of hostname resource names.

`path_route_set_name`

(optional) Deprecated. Please use `routingPolicies` instead. The name of the set of path-based routing rules,`PATH_ROUTE_SET`Type, applied to this listener's traffic. Example: `example_path_route_set`

`ssl_configuration`

(optional)

`connection_configuration`

(optional)

`routing_policy_name`

(optional) The name of the routing policy applied to this listener's traffic. Example: `example_routing_policy`

`rule_set_names`

(optional) The names of the`RULE_SET`Type to apply to the listener. Example: [\"example_rule_set\"]

### DBMS_CLOUD_OCI_LOAD_BALANCER_HOSTNAME_DETAILS_T Type

The details of a hostname resource associated with a load balancer.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the hostname resource. Example: `example_hostname_001`

`hostname`

(required) A virtual hostname. For more information about virtual hostname string construction, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm#routing). Example: `app.example.com`

### DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CIPHER_SUITE_DETAILS_T Type

The configuration details of an SSL cipher suite. The algorithms that compose a cipher suite help you secure Transport Layer Security (TLS) or Secure Socket Layer (SSL) network connections. A cipher suite defines the list of security algorithms your load balancer uses to negotiate with peers while sending and receiving information. The cipher suites you use affect the security level, performance, and compatibility of your data traffic. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. Oracle created the following predefined cipher suites that you can specify when you define a resource's[SSL configuration](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/datatypes/SSLConfigurationDetails). You can[create custom cipher suites](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/SSLCipherSuite/CreateSSLCipherSuite)if the predefined cipher suites do not meet your requirements. * __oci-default-ssl-cipher-suite-v1__ \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-modern-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" * __oci-wider-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA\" \"DH-DSS-AES256-SHA256\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA\" \"DH-RSA-AES256-SHA256\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-AES256-SHA256\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-AES256-SHA256\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-AES256-SHA384\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\"

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the SSL cipher suite. It must be unique and it cannot be changed. **Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or reserved SSL cipher suite names: * oci-default-ssl-cipher-suite-v1 * oci-modern-ssl-cipher-suite-v1 * oci-compatible-ssl-cipher-suite-v1 * oci-wider-compatible-ssl-cipher-suite-v1 * oci-customized-ssl-cipher-suite example: `example_cipher_suite`

`ciphers`

(required) A list of SSL ciphers the load balancer must support for HTTPS or SSL connections. The following ciphers are valid values for this property: * __TLSv1.2 ciphers__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA256\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA256\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA384\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __TLSv1 ciphers also supported by TLSv1.2__ \"AES128-SHA\" \"AES256-SHA\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES256-SHA\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES256-SHA\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\" example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_MATCH_TYPE_T Type

The type of matching to apply to incoming URIs.

Syntax
```

```

Fields

Field Description

`match_type`

(required) Specifies how the load balancing service compares a`PATH_ROUTE`Function object's `path` string against the incoming URI. * **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path. * **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning portion of the incoming URI path. * **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path. * **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path. For a full description of how the system handles `matchType` in a path route set containing multiple rules, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

Allowed values are: 'EXACT_MATCH', 'FORCE_LONGEST_PREFIX_MATCH', 'PREFIX_MATCH', 'SUFFIX_MATCH'

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_T Type

A \"path route rule\" to evaluate an incoming URI path, and then route a matching request to the specified backend set. Path route rules apply only to HTTP and HTTPS requests. They have no effect on TCP requests.

Syntax
```

```

Fields

Field Description

`path`

(required) The path string to match against the incoming URI path. * Path strings are case-insensitive. * Asterisk (*) wildcards are not supported. * Regular expressions are not supported. Example: `/example/video/123`

`path_match_type`

(required) The type of matching to apply to incoming URIs.

`backend_set_name`

(required) The name of the target backend set for requests where the incoming URI matches the specified path. Example: `example_backend_set`

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_path_route_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_SET_DETAILS_T Type

A set of path route rules.

Syntax
```

```

Fields

Field Description

`path_routes`

(required) The set of path route rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_SET_DETAILS_T Type

The rules that compose a rule set.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of rules that compose the rule set.

### DBMS_CLOUD_OCI_LOAD_BALANCER_RESERVED_IP_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_reserved_ip_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_LOAD_BALANCER_DETAILS_T Type

The configuration details for creating a load balancer. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the load balancer.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `example_load_balancer`

`shape_name`

(required) A template that determines the total pre-provisioned bandwidth (ingress plus egress). To get a list of available shapes, use the`LIST_SHAPES`Function operation. Example: `flexible` NOTE: Starting May 2023, Fixed shapes - 10Mbps, 100Mbps, 400Mbps, 8000Mbps would be deprecated and only shape allowed would be `Flexible`

`shape_details`

(optional) The configuration details to create load balancer using Flexible shape. This is required only if shapeName is `Flexible`.

`is_private`

(optional) Whether the load balancer has a VCN-local (private) IP address. If \"true\", the service assigns a private IP address to the load balancer. If \"false\", the service assigns a public IP address to the load balancer. A public load balancer is accessible from the internet, depending on your VCN's[security list rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). For more information about public and private load balancers, see[How Load Balancing Works](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#how-load-balancing-works). Example: `true`

`ip_mode`

(optional) Whether the load balancer has an IPv4 or IPv6 IP address. If \"IPV4\", the service assigns an IPv4 address and the load balancer supports IPv4 traffic. If \"IPV6\", the service assigns an IPv6 address and the load balancer supports IPv6 traffic. Example: \"ipMode\":\"IPV6\"

Allowed values are: 'IPV4', 'IPV6'

`reserved_ips`

(optional) An array of reserved Ips.

`listeners`

(optional)

`hostnames`

(optional)

`backend_sets`

(optional)

`network_security_group_ids`

(optional) An array of NSG[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with this load balancer. During the load balancer's creation, the service adds the new load balancer to the specified NSGs. The benefits of using NSGs with the load balancer include: * NSGs define network security rules to govern ingress and egress traffic for the load balancer. * The network security rules of other resources can reference the NSGs associated with the load balancer to ensure access. Example: `[\"ocid1.nsg.oc1.phx.unique_ID\"]`

`subnet_ids`

(required) An array of subnet[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`certificates`

(optional)

`ssl_cipher_suites`

(optional)

`path_route_sets`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`rule_sets`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_PATH_ROUTE_SET_DETAILS_T Type

A named set of path route rules to add to the load balancer. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_path_route_set`

`path_routes`

(required) The set of path route rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_ACTION_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_RULE_T Type

A routing rule examines an incoming request, routing matching requests to the specified backend set. Routing rules apply only to HTTP and HTTPS requests. They have no effect on TCP requests.

Syntax
```

```

Fields

Field Description

`name`

(required) A unique name for the routing policy rule. Avoid entering confidential information.

`condition`

(required) A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.

`actions`

(required) A list of actions to be applied when conditions of the routing rule are met.

### DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_RULE_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_routing_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_ROUTING_POLICY_DETAILS_T Type

An ordered list of routing rules. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for this list of routing rules. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_routing_rules`

`condition_language_version`

(required) The version of the language in which `condition` of `rules` are composed.

Allowed values are: 'V1'

`rules`

(required) The list of routing rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_RULE_SET_DETAILS_T Type

A named set of rules to add to the load balancer.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_rule_set`

`items`

(required) An array of rules that compose the rule set.

### DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_SSL_CIPHER_SUITE_DETAILS_T Type

The configuration details of an SSL cipher suite. The algorithms that compose a cipher suite help you secure Transport Layer Security (TLS) or Secure Socket Layer (SSL) network connections. A cipher suite defines the list of security algorithms your load balancer uses to negotiate with peers while sending and receiving information. The cipher suites you use affect the security level, performance, and compatibility of your data traffic. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. Oracle created the following predefined cipher suites that you can specify when you define a resource's[SSL configuration](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/datatypes/SSLConfigurationDetails). You can[create custom cipher suites](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/SSLCipherSuite/CreateSSLCipherSuite)if the predefined cipher suites do not meet your requirements. * __oci-default-ssl-cipher-suite-v1__ \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-modern-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" * __oci-wider-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA\" \"DH-DSS-AES256-SHA256\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA\" \"DH-RSA-AES256-SHA256\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-AES256-SHA256\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-AES256-SHA256\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-AES256-SHA384\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\"

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the SSL cipher suite. It must be unique and it cannot be changed. **Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or reserved SSL cipher suite names: * oci-default-ssl-cipher-suite-v1 * oci-modern-ssl-cipher-suite-v1 * oci-compatible-ssl-cipher-suite-v1 * oci-wider-compatible-ssl-cipher-suite-v1 * oci-customized-ssl-cipher-suite example: `example_cipher_suite`

`ciphers`

(required) A list of SSL ciphers the load balancer must support for HTTPS or SSL connections. The following ciphers are valid values for this property: * __TLSv1.2 ciphers__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA256\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA256\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA384\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __TLSv1 ciphers also supported by TLSv1.2__ \"AES128-SHA\" \"AES256-SHA\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES256-SHA\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES256-SHA\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\" example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`

### DBMS_CLOUD_OCI_LOAD_BALANCER_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOAD_BALANCER_EXTEND_HTTP_REQUEST_HEADER_VALUE_RULE_T Type

An object that represents the action of modifying a request header value. This rule applies only to HTTP listeners. This rule adds a prefix, a suffix, or both to the header value. **NOTES:** * This rule requires a value for a prefix, suffix, or both. * The system does not support this rule for headers with multiple values. * The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. If two such headers appear in a request, the system applies the action to the first header it finds. The affected header cannot be determined in advance. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_extend_http_request_header_value_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

`prefix`

(optional) A string to prepend to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_prefix_value`

`suffix`

(optional) A string to append to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_suffix_value`

### DBMS_CLOUD_OCI_LOAD_BALANCER_EXTEND_HTTP_RESPONSE_HEADER_VALUE_RULE_T Type

An object that represents the action of modifying a response header value. This rule applies only to HTTP listeners. This rule adds a prefix, a suffix, or both to the header value. **NOTES:** * This rule requires a value for a prefix, suffix, or both. * The system does not support this rule for headers with multiple values. * The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. If two such headers appear in a request, the system applies the action to the first header it finds. The affected header cannot be determined in advance. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_extend_http_response_header_value_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

`prefix`

(optional) A string to prepend to the header value. The resulting header value must still conform to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_prefix_value`

`suffix`

(optional) A string to append to the header value. The resulting header value must still conform to RFC 7230. With the following exceptions: * value cannot contain `$` * value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid. Example: `example_suffix_value`

### DBMS_CLOUD_OCI_LOAD_BALANCER_FORWARD_TO_BACKEND_SET_T Type

Action to forward requests to a given backend set.

Syntax
```

```

`dbms_cloud_oci_load_balancer_forward_to_backend_set_t`is a subtype of the`dbms_cloud_oci_load_balancer_action_t`type.

Fields

Field Description

`backend_set_name`

(required) Name of the backend set the listener will forward the traffic to. Example: `backendSetForImages`

### DBMS_CLOUD_OCI_LOAD_BALANCER_HOSTNAME_T Type

A hostname resource associated with a load balancer for use by one or more listeners. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_hostname_001`

`hostname`

(required) A virtual hostname. For more information about virtual hostname string construction, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm#routing). Example: `app.example.com`

### DBMS_CLOUD_OCI_LOAD_BALANCER_HTTP_HEADER_RULE_T Type

An object that represents the advance http header options that allow the setting of http header size and allow/disallow invalid characters in the http headers. For example httpLargeHeaderSizeInKB=32, the http header could have 4 buffers of 32KBs each This rule applies only to HTTP listeners. No more than one `HttpHeaderRule` object can be present in a given listener.

Syntax
```

```

`dbms_cloud_oci_load_balancer_http_header_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`are_invalid_characters_allowed`

(optional) Indicates whether or not invalid characters in client header fields will be allowed. Valid names are composed of English letters, digits, hyphens and underscores. If \"true\", invalid characters are allowed in the HTTP header. If \"false\", invalid characters are not allowed in the HTTP header

`http_large_header_size_in_kb`

(optional) The maximum size of each buffer used for reading http client request header. This value indicates the maximum size allowed for each buffer. The allowed values for buffer size are 8, 16, 32 and 64.

### DBMS_CLOUD_OCI_LOAD_BALANCER_IP_ADDRESS_T Type

A load balancer IP address.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) An IP address. Example: `192.168.0.3`

`is_public`

(optional) Whether the IP address is public or private. If \"true\", the IP address is public and accessible from the internet. If \"false\", the IP address is private and accessible only from within the associated VCN.

`reserved_ip`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_T Type

The listener's configuration. For more information on backend set configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Example: `example_listener`

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the`LIST_PROTOCOLS`Function operation. Example: `HTTP`

`hostname_names`

(optional) An array of hostname resource names.

`path_route_set_name`

(optional) Deprecated. Please use `routingPolicies` instead. The name of the set of path-based routing rules,`PATH_ROUTE_SET`Type, applied to this listener's traffic. Example: `example_path_route_set`

`ssl_configuration`

(optional)

`connection_configuration`

(optional)

`rule_set_names`

(optional) The names of the`RULE_SET`Type to apply to the listener. Example: [\"example_rule_set\"]

`routing_policy_name`

(optional) The name of the routing policy applied to this listener's traffic. Example: `example_routing_policy_name`

### DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_RULE_SUMMARY_T Type

The attributes of a rule associated with the specified listener, and the name of the rule set that the rule belongs to.

Syntax
```

```

Fields

Field Description

`rule`

(optional) A rule object that applies to the listener.

`rule_set_name`

(optional) The name of the rule set that the rule belongs to.

### DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CIPHER_SUITE_T Type

The configuration details of an SSL cipher suite. The algorithms that compose a cipher suite help you secure Transport Layer Security (TLS) or Secure Socket Layer (SSL) network connections. A cipher suite defines the list of security algorithms your load balancer uses to negotiate with peers while sending and receiving information. The cipher suites you use affect the security level, performance, and compatibility of your data traffic. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. Oracle created the following predefined cipher suites that you can specify when you define a resource's[SSL configuration](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/datatypes/SSLConfigurationDetails). You can[create custom cipher suites](https://docs.oracle.com/iaas/api/#/en/loadbalancer/20170115/SSLCipherSuite/CreateSSLCipherSuite)if the predefined cipher suites do not meet your requirements. * __oci-default-ssl-cipher-suite-v1__ \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-modern-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __oci-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" * __oci-wider-compatible-ssl-cipher-suite-v1__ \"AES128-GCM-SHA256\" \"AES128-SHA\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA\" \"AES256-SHA256\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA\" \"DH-DSS-AES256-SHA256\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA\" \"DH-RSA-AES256-SHA256\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-AES256-SHA256\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-AES256-SHA256\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-AES256-SHA384\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-AES256-SHA384\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\"

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the SSL cipher suite. It must be unique and it cannot be changed. **Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or reserved SSL cipher suite names: * oci-default-ssl-cipher-suite-v1 * oci-modern-ssl-cipher-suite-v1 * oci-compatible-ssl-cipher-suite-v1 * oci-wider-compatible-ssl-cipher-suite-v1 * oci-customized-ssl-cipher-suite example: `example_cipher_suite`

`ciphers`

(required) A list of SSL ciphers the load balancer must support for HTTPS or SSL connections. The following ciphers are valid values for this property: * __TLSv1.2 ciphers__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA256\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA256\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA384\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __TLSv1 ciphers also supported by TLSv1.2__ \"AES128-SHA\" \"AES256-SHA\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES256-SHA\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES256-SHA\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\" example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_SET_T Type

A named set of path route rules. For more information, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name for this set of path route rules. Avoid entering confidential information. Example: `example_path_route_set`

`path_routes`

(required) The set of path route rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_SET_T Type

A named set of rules associated with a load balancer. Rules are objects that represent actions to apply to a listener, such as adding, altering, or removing HTTP headers. For more information, see[Managing Rule Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information. Example: `example_rule_set`

`items`

(required) An array of rules that compose the rule set.

### DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_POLICY_T Type

A named ordered list of routing rules that is applied to a listener. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name for this list of routing rules. Avoid entering confidential information. Example: `example_routing_policy`

`condition_language_version`

(required) The version of the language in which `condition` of `rules` are composed.

Allowed values are: 'V1'

`rules`

(required) The ordered list of routing rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_IP_ADDRESS_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_ip_address_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_T Type

The properties that define a load balancer. For more information, see[Managing a Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancer.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Example: `example_load_balancer`

`lifecycle_state`

(required) The current state of the load balancer.

Allowed values are: 'CREATING', 'FAILED', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the load balancer was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`ip_addresses`

(optional) An array of IP addresses.

`shape_name`

(required) A template that determines the total pre-provisioned bandwidth (ingress plus egress). To get a list of available shapes, use the`LIST_SHAPES`Function operation. Example: `100Mbps`

`shape_details`

(optional)

`is_private`

(optional) Whether the load balancer has a VCN-local (private) IP address. If \"true\", the service assigns a private IP address to the load balancer. If \"false\", the service assigns a public IP address to the load balancer. A public load balancer is accessible from the internet, depending on your VCN's[security list rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). For more information about public and private load balancers, see[How Load Balancing Works](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#how-load-balancing-works). Example: `true`

`subnet_ids`

(optional) An array of subnet[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`network_security_group_ids`

(optional) An array of NSG[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the load balancer. During the load balancer's creation, the service adds the new load balancer to the specified NSGs. The benefits of associating the load balancer with NSGs include: * NSGs define network security rules to govern ingress and egress traffic for the load balancer. * The network security rules of other resources can reference the NSGs associated with the load balancer to ensure access. Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

`listeners`

(optional)

`hostnames`

(optional)

`ssl_cipher_suites`

(optional)

`certificates`

(optional)

`backend_sets`

(optional)

`path_route_sets`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`rule_sets`

(optional)

`routing_policies`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_HEALTH_T Type

The health status details for the specified load balancer. This object does not explicitly enumerate backend sets with a status of `OK`. However, they are included in the `totalBackendSetCount` sum.

Syntax
```

```

Fields

Field Description

`status`

(required) The overall health status of the load balancer. * **OK:** All backend sets associated with the load balancer return a status of `OK`. * **WARNING:** At least one of the backend sets associated with the load balancer returns a status of `WARNING`, no backend sets return a status of `CRITICAL`, and the load balancer life cycle state is `ACTIVE`. * **CRITICAL:** One or more of the backend sets associated with the load balancer return a status of `CRITICAL`. * **UNKNOWN:** If any one of the following conditions is true: * The load balancer life cycle state is not `ACTIVE`. * No backend sets are defined for the load balancer. * More than half of the backend sets associated with the load balancer return a status of `UNKNOWN`, none of the backend sets return a status of `WARNING` or `CRITICAL`, and the load balancer life cycle state is `ACTIVE`. * The system could not retrieve metrics for any reason.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`warning_state_backend_set_names`

(required) A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the friendly name you assigned when you created it. Example: `example_backend_set3`

`critical_state_backend_set_names`

(required) A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the friendly name you assigned when you created it. Example: `example_backend_set`

`unknown_state_backend_set_names`

(required) A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the friendly name you assigned when you created it. Example: `example_backend_set2`

`total_backend_set_count`

(required) The total number of backend sets associated with this load balancer. Example: `4`

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_HEALTH_SUMMARY_T Type

A health status summary for the specified load balancer.

Syntax
```

```

Fields

Field Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer the health status is associated with.

`status`

(required) The overall health status of the load balancer. * **OK:** All backend sets associated with the load balancer return a status of `OK`. * **WARNING:** At least one of the backend sets associated with the load balancer returns a status of `WARNING`, no backend sets return a status of `CRITICAL`, and the load balancer life cycle state is `ACTIVE`. * **CRITICAL:** One or more of the backend sets associated with the load balancer return a status of `CRITICAL`. * **UNKNOWN:** If any one of the following conditions is true: * The load balancer life cycle state is not `ACTIVE`. * No backend sets are defined for the load balancer. * More than half of the backend sets associated with the load balancer return a status of `UNKNOWN`, none of the backend sets return a status of `WARNING` or `CRITICAL`, and the load balancer life cycle state is `ACTIVE`. * The system could not retrieve metrics for any reason.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_POLICY_T Type

A policy that determines how traffic is distributed among backend servers. For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of a load balancing policy. Example: 'LEAST_CONNECTIONS'

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_PROTOCOL_T Type

A protocol that defines the type of traffic accepted by a listener.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of a protocol. Example: 'HTTP'

### DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_SHAPE_T Type

A shape is a template that determines the total pre-provisioned bandwidth (ingress plus egress) for the load balancer. Note that the pre-provisioned maximum capacity applies to aggregated connections, not to a single client attempting to use the full bandwidth.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the shape. Example: `100Mbps`

### DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_MATCH_CONDITION_T Type

The path string and match condition to apply when evaluating an incoming URI for redirection.

Syntax
```

```

`dbms_cloud_oci_load_balancer_path_match_condition_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) The path string that the redirection rule applies to. Example: `/example`

`operator`

(required) A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the incoming URI. * **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string. * **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best, longest match of the beginning portion of the incoming URI path. * **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the `attributeValue` string. * **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue` string.

Allowed values are: 'EXACT_MATCH', 'FORCE_LONGEST_PREFIX_MATCH', 'PREFIX_MATCH', 'SUFFIX_MATCH'

### DBMS_CLOUD_OCI_LOAD_BALANCER_REDIRECT_URI_T Type

An object that defines the redirect URI applied to the original request. The object property values compose the redirect URI. **NOTE:** The Load Balancing service cannot automatically detect or avoid infinite redirects. Be sure to provide meaningful, complete, and correct field values. If any component field of this object has no value, the system retains the value from the incoming HTTP request URI. For example, if you specify only the protocol field `https`, and the incoming request URI is `http://example.com:8080`, the resulting runtime redirect URI is `https://example.com:8080`. The system retains the host and port from the incoming URI and does not automatically change the port setting from `8080` to `443`. Be sure to configure valid percent-encoding (URL encoding) when needed. In addition to static string values, you can use the following tokens to construct the redirect URI. These tokens extract values from the incoming HTTP request URI. * {protocol} : The protocol from the incoming HTTP request URI. * {host} : The domain name from the incoming HTTP request URI. * {port} : The port from the incoming HTTP request URI. * {path} : The path from the incoming HTTP request URI. * {query} : The query string from the incoming HTTP request URI. The tokens are case sensitive. For example, `{host}` is a valid token, but `{HOST}` is not. You can retain the literal characters of a token when you specify values for the path and query properties of the redirect URI. Use a backslash (\\\\) as the escape character for the \\\\, {, and } characters. For example, if the incoming HTTP request URI is `/video`, the path property value: `/example{path}123\\{path\\}` appears in the constructed redirect URI as: `/example/video123{path}`

Syntax
```

```

Fields

Field Description

`protocol`

(optional) The HTTP protocol to use in the redirect URI. When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the incoming HTTP request URI. Allowed values are: * HTTP * HTTPS * {protocol} `{protocol}` is the only valid token for this property. It can appear only once in the value string. Example: `HTTPS`

`host`

(optional) The valid domain name (hostname) or IP address to use in the redirect URI. When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the incoming HTTP request URI. All RedirectUri tokens are valid for this property. You can use any token more than once. Curly braces are valid in this property only to surround tokens, such as `{host}` Examples: * **example.com** appears as `example.com` in the redirect URI. * **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI. * **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and the port is `8081` in the incoming HTTP request URI.

`port`

(optional) The communication port to use in the redirect URI. Valid values include integers from 1 to 65535. When this value is null, the service preserves the original port from the incoming HTTP request URI. Example: `8081`

`path`

(optional) The HTTP URI path to use in the redirect URI. When this value is null, not set, or set to `{path}`, the service preserves the original path from the incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \"\". All RedirectUri tokens are valid for this property. You can use any token more than once. The path string must begin with `/` if it does not begin with the `{path}` token. Examples: * __/example/video/123__ appears as `/example/video/123` in the redirect URI. * __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the incoming HTTP request URI. * __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI. * __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI. * __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI. * __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and `123` is the port in the incoming HTTP request URI. * __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP request URI.

`query`

(optional) The query string to use in the redirect URI. When this value is null, not set, or set to `{query}`, the service preserves the original query parameters from the incoming HTTP request URI. All `RedirectUri` tokens are valid for this property. You can use any token more than once. If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character. You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand (&amp;) character. To omit all incoming query parameters from the redirect URI, set this value to an empty string, \"\". If the specified query string results in a redirect URI ending with `?` or `&amp;`, the last character is truncated. For example, if the incoming URI is `http://host:8080/documents` and the query property value is `?lang=en&amp;{query}`, the redirect URI is `http://host:8080/documents?lang=en`. The system truncates the final ampersand (&amp;) because the incoming URI included no value to replace the {query} token. Examples: * **lang=en&amp;time_zone=PST** appears as `lang=en&amp;time_zone=PST` in the redirect URI. * **{query}** appears as `lang=en&amp;time_zone=PST` in the redirect URI if `lang=en&amp;time_zone=PST` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}` token renders as an empty string. * **lang=en&amp;{query}&amp;time_zone=PST** appears as `lang=en&amp;country=us&amp;time_zone=PST` in the redirect URI if `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, this value renders as `lang=en&amp;time_zone=PST`. * **protocol={protocol}&amp;hostname={host}** appears as `protocol=http&amp;hostname=example.com` in the redirect URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request. * **port={port}&amp;hostname={host}** appears as `port=8080&amp;hostname=example.com` in the redirect URI if the port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.

### DBMS_CLOUD_OCI_LOAD_BALANCER_REDIRECT_RULE_T Type

An object that represents the action of returning a specified response code and a redirect URI. Each RedirectRule object is configured for a particular listener and a designated path. The default response code is `302 Found`. **NOTES:** * This rule applies only to HTTP listeners. * You can specify this rule only with the`RULE_CONDITION`Function type `PATH`. * A listener can have only one RedirectRule object for a given original path. The`PATH_MATCH_CONDITION`Function `attributeValue` specifies the original path.

Syntax
```

```

`dbms_cloud_oci_load_balancer_redirect_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`response_code`

(optional) The HTTP status code to return when the incoming request is redirected. The status line returned with the code is mapped from the standard HTTP specification. Valid response codes for redirection are: * 301 * 302 * 303 * 307 * 308 The default value is `302` (Found). Example: `301`

`conditions`

(required)

`redirect_uri`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_REMOVE_HTTP_REQUEST_HEADER_RULE_T Type

An object that represents the action of removing a header from a request. This rule applies only to HTTP listeners. If the same header appears more than once in the request, the load balancer removes all occurances of the specified header. **Note:** The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_remove_http_request_header_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

### DBMS_CLOUD_OCI_LOAD_BALANCER_REMOVE_HTTP_RESPONSE_HEADER_RULE_T Type

An object that represents the action of removing a header from a response. This rule applies only to HTTP listeners. If the same header appears more than once in the response, the load balancer removes all occurances of the specified header. **Note:** The system does not distinquish between underscore and dash characters in headers. That is, it treats `example_header_name` and `example-header-name` as identical. Oracle recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.

Syntax
```

```

`dbms_cloud_oci_load_balancer_remove_http_response_header_rule_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_t`type.

Fields

Field Description

`header`

(required) A header name that conforms to RFC 7230. Example: `example_header_name`

### DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_POLICY_DETAILS_T Type

An ordered list of routing rules. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`rules`

(required) The list of routing rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_IP_ADDRESS_CONDITION_T Type

A rule condition that checks client source IP against specified IP address or address range.

Syntax
```

```

`dbms_cloud_oci_load_balancer_source_ip_address_condition_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) An IPv4 or IPv6 address range that the source IP address of an incoming packet must match. The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y or x:x::x/y) strings. Specify 0.0.0.0/0 or ::/0 to match all incoming traffic.

### DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_VCN_ID_CONDITION_T Type

An access control rule condition that requires a match on the specified source VCN OCID.

Syntax
```

```

`dbms_cloud_oci_load_balancer_source_vcn_id_condition_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the originating VCN that an incoming packet must match. You can use this condition in conjunction with `SourceVcnIpAddressCondition`. **NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition matches all incoming traffic in the specified VCN.

### DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_VCN_IP_ADDRESS_CONDITION_T Type

An access control rule condition that requires a match on the specified source VCN and IP address range. This condition must be used only in conjunction with `SourceVcnIdCondition`.

Syntax
```

```

`dbms_cloud_oci_load_balancer_source_vcn_ip_address_condition_t`is a subtype of the`dbms_cloud_oci_load_balancer_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) An IPv4 address range that the original client IP address (in the context of the specified VCN) of an incoming packet must match. The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y) strings. Specify 0.0.0.0/0 to match all incoming traffic in the customer VCN. example: \"10.10.1.0/24\"

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_BACKEND_DETAILS_T Type

The configuration details for updating a backend server.

Syntax
```

```

Fields

Field Description

`weight`

(required) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`backup`

(required) Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy. **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy. Example: `false`

`drain`

(required) Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic. Example: `false`

`l_offline`

(required) Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_BACKEND_SET_DETAILS_T Type

The configuration details for updating a load balancer backend set. For more information on backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Note:** The `sessionPersistenceConfiguration` (application cookie stickiness) and `lbCookieSessionPersistenceConfiguration` (LB cookie stickiness) attributes are mutually exclusive. To avoid returning an error, configure only one of these two attributes per backend set. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`policy`

(required) The load balancer policy for the backend set. To get a list of available policies, use the`LIST_POLICIES`Function operation. Example: `LEAST_CONNECTIONS`

`backends`

(required)

`health_checker`

(required)

`ssl_configuration`

(optional)

`session_persistence_configuration`

(optional)

`lb_cookie_session_persistence_configuration`

(optional)

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_HEALTH_CHECKER_DETAILS_T Type

The health checker's configuration details.

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol the health check must use; either HTTP or TCP. Example: `HTTP`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`port`

(required) The backend server port against which to run the health check. Example: `8080`

`return_code`

(required) The status code a healthy backend server should return. Example: `200`

`retries`

(required) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. Example: `3`

`timeout_in_millis`

(required) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Example: `3000`

`interval_in_millis`

(required) The interval between health checks, in milliseconds. Example: `10000`

`response_body_regex`

(required) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`is_force_plain_text`

(optional) Specifies if health checks should always be done using plain text instead of depending on whether or not the associated backend set is using SSL. If \"true\", health checks will be done using plain text even if the associated backend set is configured to use SSL. If \"false\", health checks will be done using SSL encryption if the associated backend set is configured to use SSL. If the backend set is not so configured the health checks will be done using plain text. Example: `true`

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_HOSTNAME_DETAILS_T Type

The configuration details for updating a virtual hostname. For more information on virtual hostnames, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

Syntax
```

```

Fields

Field Description

`hostname`

(optional) The virtual hostname to update. For more information about virtual hostname string construction, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm#routing). Example: `app.example.com`

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LISTENER_DETAILS_T Type

The configuration details for updating a listener.

Syntax
```

```

Fields

Field Description

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the`LIST_PROTOCOLS`Function operation. Example: `HTTP`

`hostname_names`

(optional) An array of hostname resource names.

`path_route_set_name`

(optional) Deprecated. Please use `routingPolicies` instead. The name of the set of path-based routing rules,`PATH_ROUTE_SET`Type, applied to this listener's traffic. Example: `example_path_route_set`

`routing_policy_name`

(optional) The name of the routing policy applied to this listener's traffic. Example: `example_routing_policy`

`ssl_configuration`

(optional)

`connection_configuration`

(optional)

`rule_set_names`

(optional) The names of the`RULE_SET`Type to apply to the listener. Example: [\"example_rule_set\"]

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LOAD_BALANCER_DETAILS_T Type

Configuration details to update a load balancer. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly display name for the load balancer. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `example_load_balancer`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LOAD_BALANCER_SHAPE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`shape_name`

(required) The new shape name for the load balancer. Allowed values are : * 10Mbps * 100Mbps * 400Mbps * 8000Mbps * Flexible Example: `flexible` * NOTE: Fixed shapes 10Mbps, 100Mbps, 400Mbps, 8000Mbps will be deprecated from May 2023. This api * will only support `Flexible` shape after that date.

`shape_details`

(optional) The configuration details to update load balancer to a different profile.

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_NETWORK_SECURITY_GROUPS_DETAILS_T Type

An object representing an updated list of network security groups (NSGs) that overwrites the existing list of NSGs. * If the load balancer has no NSGs configured, it uses the NSGs in this list. * If the load balancer has a list of NSGs configured, this list replaces the existing list. * If the load balancer has a list of NSGs configured and this list is empty, the operation removes all of the load balancer's NSG associations.

Syntax
```

```

Fields

Field Description

`network_security_group_ids`

(optional) An array of NSG[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the load balancer. During the load balancer's creation, the service adds the new load balancer to the specified NSGs. The benefits of associating the load balancer with NSGs include: * NSGs define network security rules to govern ingress and egress traffic for the load balancer. * The network security rules of other resources can reference the NSGs associated with the load balancer to ensure access.

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_PATH_ROUTE_SET_DETAILS_T Type

An updated set of path route rules that overwrites the existing set of rules.

Syntax
```

```

Fields

Field Description

`path_routes`

(required) The set of path route rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_ROUTING_POLICY_DETAILS_T Type

An updated list of routing rules that overwrites the existing list of routing rules.

Syntax
```

```

Fields

Field Description

`condition_language_version`

(optional) The version of the language in which `condition` of `rules` are composed.

Allowed values are: 'V1'

`rules`

(required) The list of routing rules.

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_RULE_SET_DETAILS_T Type

An updated set of rules that overwrites the existing set of rules.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of rules that compose the rule set.

### DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_SSL_CIPHER_SUITE_DETAILS_T Type

The configuration details for updating an SSL cipher suite. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`ciphers`

(required) A list of SSL ciphers the load balancer must support for HTTPS or SSL connections. The following ciphers are valid values for this property: * __TLSv1.2 ciphers__ \"AES128-GCM-SHA256\" \"AES128-SHA256\" \"AES256-GCM-SHA384\" \"AES256-SHA256\" \"DH-DSS-AES128-GCM-SHA256\" \"DH-DSS-AES128-SHA256\" \"DH-DSS-AES256-GCM-SHA384\" \"DH-DSS-AES256-SHA256\" \"DH-RSA-AES128-GCM-SHA256\" \"DH-RSA-AES128-SHA256\" \"DH-RSA-AES256-GCM-SHA384\" \"DH-RSA-AES256-SHA256\" \"DHE-DSS-AES128-GCM-SHA256\" \"DHE-DSS-AES128-SHA256\" \"DHE-DSS-AES256-GCM-SHA384\" \"DHE-DSS-AES256-SHA256\" \"DHE-RSA-AES128-GCM-SHA256\" \"DHE-RSA-AES128-SHA256\" \"DHE-RSA-AES256-GCM-SHA384\" \"DHE-RSA-AES256-SHA256\" \"ECDH-ECDSA-AES128-GCM-SHA256\" \"ECDH-ECDSA-AES128-SHA256\" \"ECDH-ECDSA-AES256-GCM-SHA384\" \"ECDH-ECDSA-AES256-SHA384\" \"ECDH-RSA-AES128-GCM-SHA256\" \"ECDH-RSA-AES128-SHA256\" \"ECDH-RSA-AES256-GCM-SHA384\" \"ECDH-RSA-AES256-SHA384\" \"ECDHE-ECDSA-AES128-GCM-SHA256\" \"ECDHE-ECDSA-AES128-SHA256\" \"ECDHE-ECDSA-AES256-GCM-SHA384\" \"ECDHE-ECDSA-AES256-SHA384\" \"ECDHE-RSA-AES128-GCM-SHA256\" \"ECDHE-RSA-AES128-SHA256\" \"ECDHE-RSA-AES256-GCM-SHA384\" \"ECDHE-RSA-AES256-SHA384\" * __TLSv1 ciphers also supported by TLSv1.2__ \"AES128-SHA\" \"AES256-SHA\" \"CAMELLIA128-SHA\" \"CAMELLIA256-SHA\" \"DES-CBC3-SHA\" \"DH-DSS-AES128-SHA\" \"DH-DSS-AES256-SHA\" \"DH-DSS-CAMELLIA128-SHA\" \"DH-DSS-CAMELLIA256-SHA\" \"DH-DSS-DES-CBC3-SHAv\" \"DH-DSS-SEED-SHA\" \"DH-RSA-AES128-SHA\" \"DH-RSA-AES256-SHA\" \"DH-RSA-CAMELLIA128-SHA\" \"DH-RSA-CAMELLIA256-SHA\" \"DH-RSA-DES-CBC3-SHA\" \"DH-RSA-SEED-SHA\" \"DHE-DSS-AES128-SHA\" \"DHE-DSS-AES256-SHA\" \"DHE-DSS-CAMELLIA128-SHA\" \"DHE-DSS-CAMELLIA256-SHA\" \"DHE-DSS-DES-CBC3-SHA\" \"DHE-DSS-SEED-SHA\" \"DHE-RSA-AES128-SHA\" \"DHE-RSA-AES256-SHA\" \"DHE-RSA-CAMELLIA128-SHA\" \"DHE-RSA-CAMELLIA256-SHA\" \"DHE-RSA-DES-CBC3-SHA\" \"DHE-RSA-SEED-SHA\" \"ECDH-ECDSA-AES128-SHA\" \"ECDH-ECDSA-AES256-SHA\" \"ECDH-ECDSA-DES-CBC3-SHA\" \"ECDH-ECDSA-RC4-SHA\" \"ECDH-RSA-AES128-SHA\" \"ECDH-RSA-AES256-SHA\" \"ECDH-RSA-DES-CBC3-SHA\" \"ECDH-RSA-RC4-SHA\" \"ECDHE-ECDSA-AES128-SHA\" \"ECDHE-ECDSA-AES256-SHA\" \"ECDHE-ECDSA-DES-CBC3-SHA\" \"ECDHE-ECDSA-RC4-SHA\" \"ECDHE-RSA-AES128-SHA\" \"ECDHE-RSA-AES256-SHA\" \"ECDHE-RSA-DES-CBC3-SHA\" \"ECDHE-RSA-RC4-SHA\" \"IDEA-CBC-SHA\" \"KRB5-DES-CBC3-MD5\" \"KRB5-DES-CBC3-SHA\" \"KRB5-IDEA-CBC-MD5\" \"KRB5-IDEA-CBC-SHA\" \"KRB5-RC4-MD5\" \"KRB5-RC4-SHA\" \"PSK-3DES-EDE-CBC-SHA\" \"PSK-AES128-CBC-SHA\" \"PSK-AES256-CBC-SHA\" \"PSK-RC4-SHA\" \"RC4-MD5\" \"RC4-SHA\" \"SEED-SHA\" example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`

### DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_ERROR_T Type

An object returned in the event of a work request error.

Syntax
```

```

Fields

Field Description

`error_code`

(required)

Allowed values are: 'BAD_INPUT', 'INTERNAL_ERROR'

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_load_balancer_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_T Type

Many of the API requests you use to create and configure load balancing do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility for in-progress work flows. For more information about work requests, see[Viewing the State of a Work Request](https://docs.oracle.com/iaas/Content/Balance/Tasks/viewingworkrequest.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer with which the work request is associated.

`l_type`

(required) The type of action the work request represents. Example: `CreateListener`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancer.

`lifecycle_state`

(required) The current state of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`message`

(required) A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure. Possible data elements include: - workflow name - event ID - work request ID - load balancer ID - workflow completion message

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) The date and time the work request was completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`error_details`

(required)

- [Load Balancer Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-2F22E4A1-FFA3-4F16-9FC3-60103885A9CE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-E246B8CA-2B8C-4875-A30B-8E22B2116D9A)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-26676483-2D4F-4874-AA90-32E903088243)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F4A078D9-B68C-433A-AC79-29EA3001598E)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ADD_HTTP_REQUEST_HEADER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-6D9534D1-C342-4F14-B0FA-7D5DCA01BF20)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ADD_HTTP_RESPONSE_HEADER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-E0E30BD4-A3B7-42B8-8D6D-5C172D40676E)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-FCF4B539-36B2-47A9-8701-954348EF3214)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_CONDITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A7C8980A-89F8-4A02-B1C9-A5CE7752897D)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ALLOW_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-C598DEC2-F56C-4A4B-A37D-CE26474E51AE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-B0DA6BF0-EB14-457B-AD16-5B58C72E09EC)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-7BCB8503-550A-40A9-80EB-3F465C9395A2)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECK_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-98C15EE7-BE71-4C7E-B085-B60917CDDD38)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECK_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-8385114B-A88D-44EF-BA48-C8F5BBE4E8DF)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A95DBEE9-FFBC-4758-AA23-5F102F46CB9B)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECKER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-172AD109-BED0-489F-A7B7-155E593F4AAF)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-1AA42630-1371-40F0-B990-4BF3D81B7DB9)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SESSION_PERSISTENCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F349E899-4A7F-4543-BA63-EF989A4C02D4)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LB_COOKIE_SESSION_PERSISTENCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-EB656C42-91EE-4B18-B2E8-733927A96653)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-8FE57467-66A0-4BC6-BF69-4C168E298CCF)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-E15E5FA1-CA7D-4DC9-AF44-CDB31CDF70A8)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HEALTH_CHECKER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A7095924-0546-4C58-8D39-90F3EE0327F8)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-9F412559-86F2-4306-AFB3-FACC5972BC0D)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-8E5338EE-6E9D-42EE-A69C-4EA2D1B63BC5)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-692AD020-A37A-4FE8-9003-8D75D9D4C297)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_BACKEND_SET_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-AE9E82D8-30E8-4D2F-9AE3-928CBF8196D3)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-2DFC949F-2D94-4151-8FEE-7C0E9B0BAE1D)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-6594A9BF-D0F4-4353-85FE-119F16312214)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CHANGE_LOAD_BALANCER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-5B97F428-1363-4BA7-A51F-67075E77649F)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CONNECTION_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-0707FB17-5836-490E-AB94-D87A0A61FB93)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CONTROL_ACCESS_USING_HTTP_METHODS_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-DFC3F1AE-4FD8-428F-A75F-B111A3A00AC0)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-ECA019EC-D70E-4AF0-996D-010161C9CE9B)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-013A6D1F-624F-4678-AB36-E571DF2DD3CC)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-0EB29058-FA53-4721-9982-3C5BF733874A)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_HOSTNAME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A0AAC689-7297-406C-A9FC-4AD36A7F8E96)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-23724600-0B17-4676-ABEC-5E6AF4621CE5)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SHAPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-73B3BE0F-4B92-4841-B698-E61B64322F02)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RESERVED_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-6A95BA03-FE1B-4D6B-B17F-0E1260EC42E9)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-282AF0D0-4D39-446E-82CB-66CCB8824796)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HOSTNAME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-BE086B29-B333-41D8-9F74-EC6A9171DBB4)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CIPHER_SUITE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-9C4B30B8-8030-4EC0-B226-82F5724E0ADF)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_MATCH_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-E2A3B077-6D62-4A78-B0A5-F89B3466D940)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-78623B03-2586-4089-9D53-4ABD6EEBC953)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-9EC92EEE-2591-4091-B0FC-726F01B802E3)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-0887B7F0-AB23-492D-92D5-C8321CA5AF41)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A84989E3-A839-4AD8-B50C-9BC49BBDE6FA)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-D2528254-46BF-4A0F-9BD1-102F2C376F23)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RESERVED_IP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-A1647CEA-3F65-4404-BDFF-4C806C52AA89)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-9962B7A2-61E3-4FEF-9D88-BE2C8EFD99E7)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_PATH_ROUTE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-827EBD52-BD0B-4C75-9785-D4C9489CC876)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-FF533176-D5AB-49CE-894A-9004E08A330E)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-B89861AA-A9DA-48D3-94FF-68F567C18E04)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-1E4D1F60-7251-49CF-A6C6-7733C4F44054)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_ROUTING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F7E8D5A7-A3E2-493A-A1E3-920F553475A9)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_RULE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-91A6193D-EB25-4FE2-B5DA-69E5B496500A)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_CREATE_SSL_CIPHER_SUITE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-5CCB2AEA-9394-4890-A9EA-7FB45041FAE9)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-644EAF2B-0A54-4AB9-9F93-B2CE5C69E794)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_EXTEND_HTTP_REQUEST_HEADER_VALUE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-446AF1D8-835F-4A83-8A05-1A01ECC433CA)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_EXTEND_HTTP_RESPONSE_HEADER_VALUE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-6C959E95-1D2D-46DA-BCBE-1EAF6272DFF7)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_FORWARD_TO_BACKEND_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-770DA27C-9F2A-47E2-8BBF-5EDA47D6D0C5)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HOSTNAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-ABD22AB8-3417-4CF1-AF1B-CDC028AC6FA8)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_HTTP_HEADER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F92562AE-CABD-4B0D-ACBC-5D944F6DE3A0)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_IP_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-C5B0D4D3-2C71-4A56-9C3E-3288243D7A8C)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-3403C2C1-BFBA-4C3D-B36C-22677CC44857)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LISTENER_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-BD014415-B429-4EC2-853D-8FCE4E0128EE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SSL_CIPHER_SUITE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-4CD212D6-BBE9-4CA9-AFCE-0690E0B1F31D)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_ROUTE_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-5A3C5CDC-681F-47D2-9739-700DAFB28DDA)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_RULE_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-CAFE35E1-156F-4736-BD5E-719A4255351A)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-CC9AA62E-2ABB-46ED-81C3-196146AFC242)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_IP_ADDRESS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-C53DA728-F92D-4F44-A10E-27415ADB41CD)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-6B10FA74-70B8-41BE-9A74-53B9D9D52D20)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-B0B7A81F-CCF4-45F5-8B09-200D5BC800BE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_HEALTH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-73B8F12B-DCB8-42F4-ACCF-84994328F0AD)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-57912E5C-1A3C-431B-8419-EEDC5C5F9E29)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_PROTOCOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F6CF7EDE-7CC6-4B2B-9F11-1289BA01C663)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_LOAD_BALANCER_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-AC0AE8EC-F39E-42A5-9719-50BCEDE717DE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_PATH_MATCH_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-FF9C98FF-73DE-49A5-A793-2AE8F2A9B3B7)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_REDIRECT_URI_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F24311C3-0BBB-4E6A-9438-46EF3EEB22DB)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_REDIRECT_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-65E8FB71-793C-4C21-B8E0-5FCB2948D2D0)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_REMOVE_HTTP_REQUEST_HEADER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-480D1C0B-AFB6-4349-8480-881AF503CA36)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_REMOVE_HTTP_RESPONSE_HEADER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-D4E342A5-CD90-40BD-ADC7-F7AA09C31912)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_ROUTING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F05E73BB-6B58-4490-A0FE-8004EC58B296)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_IP_ADDRESS_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-E57FE6E8-ED3E-45A6-88E7-EA25CDF4B366)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_VCN_ID_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-81EBF909-8AA1-4E1C-88CF-DA7BBB8B58E1)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_SOURCE_VCN_IP_ADDRESS_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-613D4F0E-4B05-405B-B2A2-708F5A8B1BFD)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-077F2711-507D-4979-B2F0-1B57B5531DBE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-B6DC5D63-E815-4983-AC7A-1D8CF8BDB953)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_HEALTH_CHECKER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-29D65AF7-95BE-42DF-8C47-3C34D76EF3BE)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_HOSTNAME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-17A17E9D-798B-49E6-BEC1-ED893FA680F5)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-30BCFE0C-488B-4907-AFE3-1D9A861FBD27)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-37E53E7B-0501-4F24-A4FA-8EA9D2F0EF5C)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_LOAD_BALANCER_SHAPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-937AA9EA-7625-474D-92C5-E2A4FF926C57)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_NETWORK_SECURITY_GROUPS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-B6A79F87-7FEF-42CD-B6F6-1037D220C523)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_PATH_ROUTE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-229AF144-0CDB-4FAB-ACB9-CC68CD076DFF)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_ROUTING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-1DC850AD-10ED-47FE-9814-A0ACF226FD17)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_RULE_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-D137840F-903A-4E2F-98D2-E2174B57660F)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_UPDATE_SSL_CIPHER_SUITE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-78E17ECD-9CBF-4967-A123-199AA0B58569)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-F23A8C44-BC93-477B-A1FE-1CEF1C2C4417)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-FDE294DD-CD95-42AD-8F11-F24210966492)
- [DBMS_CLOUD_OCI_LOAD_BALANCER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/load_balancer_t.html#ADSDK-GUID-D54A3127-BA7B-48F9-AC9E-B2640F6B2D4E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
