# WAAS Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html
- Fetched: 2026-09-05 19:22 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#dcoc-content-body)

## WAAS Common Types

### DBMS_CLOUD_OCI_WAAS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_CRITERIA_T Type

When defined, the parent challenge would be applied only for the requests that matched all the listed conditions.

Syntax
```

```

Fields

Field Description

`condition`

(required) The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request. - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must start with a `/`. - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field. URL must start with a `/`. - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL must start with a `/`. - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field. - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field. - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org). - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org). - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the `value` field. - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the `value` field. - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the `value` field. - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \*Example:* \"1.1.1.1\1.1.1.2\1.2.2.1/30\" - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \*Example:* \"1.1.1.1\1.1.1.2\1.2.2.1/30\" - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value` in this case is OCID of the address list. - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The `value` field in this case is OCID of the address list. - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match. *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match. - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH` *Example:* \"GET\POST\" - **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH` *Example:* \"GET\POST\" - **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see[ISO's website](https://www.iso.org/obp/ui/#search/code/). *Example:* \"AL\DZ\AM\" - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see[ISO's website](https://www.iso.org/obp/ui/#search/code/). *Example:* \"AL\DZ\AM\" - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field. *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0` - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field. *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

Allowed values are: 'URL_IS', 'URL_IS_NOT', 'URL_STARTS_WITH', 'URL_PART_ENDS_WITH', 'URL_PART_CONTAINS', 'URL_REGEX', 'URL_DOES_NOT_MATCH_REGEX', 'URL_DOES_NOT_START_WITH', 'URL_PART_DOES_NOT_CONTAIN', 'URL_PART_DOES_NOT_END_WITH', 'IP_IS', 'IP_IS_NOT', 'IP_IN_LIST', 'IP_NOT_IN_LIST', 'HTTP_HEADER_CONTAINS', 'HTTP_METHOD_IS', 'HTTP_METHOD_IS_NOT', 'COUNTRY_IS', 'COUNTRY_IS_NOT', 'USER_AGENT_IS', 'USER_AGENT_IS_NOT'

`value`

(required) The criteria value.

`is_case_sensitive`

(optional) When enabled, the condition will be matched with case-sensitive rules.

### DBMS_CLOUD_OCI_WAAS_HEADER_MANIPULATION_ACTION_T Type

An object that represents an action to apply to an HTTP headers.

Syntax
```

```

Fields

Field Description

`action`

(required)

Allowed values are: 'EXTEND_HTTP_RESPONSE_HEADER', 'ADD_HTTP_RESPONSE_HEADER', 'REMOVE_HTTP_RESPONSE_HEADER'

### DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_CRITERIA_TBL Type

Nested table type of dbms_cloud_oci_waas_access_rule_criteria_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_HEADER_MANIPULATION_ACTION_TBL Type

Nested table type of dbms_cloud_oci_waas_header_manipulation_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_T Type

A content access rule. An access rule specifies an action to take if a set of criteria is matched by a request.

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name of the access rule.

`criteria`

(required) The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.

`action`

(required) The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`. - **ALLOW:** Takes no action, just logs the request. - **DETECT:** Takes no action, but creates an alert for the request. - **BLOCK:** Blocks the request by returning specified response code or showing error page. - **BYPASS:** Bypasses some or all challenges. - **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`, `redirectResponseCode`. - **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page. Regardless of action, no further rules are processed once a rule is matched.

Allowed values are: 'ALLOW', 'DETECT', 'BLOCK', 'BYPASS', 'REDIRECT', 'SHOW_CAPTCHA'

`block_action`

(optional) The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to `SET_RESPONSE_CODE`.

Allowed values are: 'SET_RESPONSE_CODE', 'SHOW_ERROR_PAGE'

`block_response_code`

(optional) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.

`block_error_page_message`

(optional) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'

`block_error_page_code`

(optional) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access rules'.

`block_error_page_description`

(optional) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'

`bypass_challenges`

(optional) The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed. - **JS_CHALLENGE:** Bypasses JavaScript Challenge. - **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge. - **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge. - **CAPTCHA:** Bypasses CAPTCHA Challenge.

Allowed values are: 'JS_CHALLENGE', 'DEVICE_FINGERPRINT_CHALLENGE', 'HUMAN_INTERACTION_CHALLENGE', 'CAPTCHA'

`redirect_url`

(optional) The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.

`redirect_response_code`

(optional) The response status code to return when `action` is set to `REDIRECT`. - **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301). - **FOUND:** Used for designating the temporary movement of a page (numerical code - 302).

Allowed values are: 'MOVED_PERMANENTLY', 'FOUND'

`captcha_title`

(optional) The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.

`captcha_header`

(optional) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.

`captcha_footer`

(optional) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.

`captcha_submit_label`

(optional) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is challenged.

`response_header_manipulation`

(optional) An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of `action` value.

### DBMS_CLOUD_OCI_WAAS_ADD_HTTP_RESPONSE_HEADER_ACTION_T Type

An object that represents the action of replacing or adding a header field. All prior occurrences of the header with the given name are removed and then the header field with specified value is added.

Syntax
```

```

`dbms_cloud_oci_waas_add_http_response_header_action_t`is a subtype of the`dbms_cloud_oci_waas_header_manipulation_action_t`type.

Fields

Field Description

`header`

(required) A header field name that conforms to RFC 7230. Example: `example_header_name`

`value`

(required) A header field value that conforms to RFC 7230. Example: `example_value`

### DBMS_CLOUD_OCI_WAAS_ADDRESS_LIST_T Type

The details of the address list.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the address list.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the address list's compartment.

`display_name`

(optional) The user-friendly name of the address list.

`address_count`

(optional) The total number of unique IP addresses in the address list.

`addresses`

(optional) The list of IP addresses or CIDR notations.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current lifecycle state of the address list.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the address list was created, expressed in RFC 3339 timestamp format.

### DBMS_CLOUD_OCI_WAAS_ADDRESS_LIST_SUMMARY_T Type

A summary of the address list's information.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the address list.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the address list's compartment.

`display_name`

(optional) The user-friendly name of the address list.

`address_count`

(optional) The total number of unique IP addresses in the address list.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current lifecycle state of the address list.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the address list was created, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_WAAS_ADDRESS_RATE_LIMITING_T Type

The IP rate limiting configuration. Defines the amount of allowed requests from a unique IP address and the resulting block response code when that threshold is exceeded.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables or disables the address rate limiting Web Application Firewall feature.

`allowed_rate_per_address`

(optional) The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.

`max_delayed_count_per_address`

(optional) The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.

`block_response_code`

(optional) The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.

### DBMS_CLOUD_OCI_WAAS_BLOCK_CHALLENGE_SETTINGS_T Type

The challenge settings if `action` is set to `BLOCK`.

Syntax
```

```

Fields

Field Description

`block_action`

(optional) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.

Allowed values are: 'SET_RESPONSE_CODE', 'SHOW_ERROR_PAGE', 'SHOW_CAPTCHA'

`block_response_code`

(optional) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.

`block_error_page_message`

(optional) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.

`block_error_page_description`

(optional) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`

`block_error_page_code`

(optional) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.

`captcha_title`

(optional) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`

`captcha_header`

(optional) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`

`captcha_footer`

(optional) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.

`captcha_submit_label`

(optional) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.

### DBMS_CLOUD_OCI_WAAS_CACHING_RULE_CRITERIA_T Type

A caching rule criteria condition and value.

Syntax
```

```

Fields

Field Description

`condition`

(required) The condition of the caching rule criteria. - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field. - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field. URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&amp;` `?` symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.

Allowed values are: 'URL_IS', 'URL_STARTS_WITH', 'URL_PART_ENDS_WITH', 'URL_PART_CONTAINS'

`value`

(required) The value of the caching rule criteria.

### DBMS_CLOUD_OCI_WAAS_CACHING_RULE_CRITERIA_TBL Type

Nested table type of dbms_cloud_oci_waas_caching_rule_criteria_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CACHING_RULE_T Type

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique key for the caching rule.

`name`

(required) The name of the caching rule.

`action`

(required) The action to take when the criteria of a caching rule are met. - **CACHE:** Caches requested content when the criteria of the rule are met. - **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met.

Allowed values are: 'CACHE', 'BYPASS_CACHE'

`caching_duration`

(optional) The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the `action` is set to `CACHE`. Example: `PT1H`

`is_client_caching_enabled`

(optional) Enables or disables client caching. Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition of a `Cache-Control` header in responses.

`client_caching_duration`

(optional) The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the `action` is set to `CACHE`. Example: `PT1H`

`criteria`

(required) The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any of the listed conditions.

### DBMS_CLOUD_OCI_WAAS_CACHING_RULE_SUMMARY_T Type

The caching rule settings.

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique key for the caching rule.

`name`

(required) The name of the caching rule.

`action`

(required) The action to take when the criteria of a caching rule are met. - **CACHE:** Caches requested content when the criteria of the rule are met. - **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met.

Allowed values are: 'CACHE', 'BYPASS_CACHE'

`caching_duration`

(optional) The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the `action` is set to `CACHE`. Example: `PT1H`

`is_client_caching_enabled`

(optional) Enables or disables client caching. Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition of a `Cache-Control` header in responses.

`client_caching_duration`

(optional) The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the `action` is set to `CACHE`. Example: `PT1H`

`criteria`

(required) The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any of the listed conditions.

### DBMS_CLOUD_OCI_WAAS_CAPTCHA_T Type

The settings of the CAPTCHA challenge. If a specific URL should be accessed only by a human, a CAPTCHA challenge can be placed at the URL to protect the web application from bots. *Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`url`

(required) The unique URL path at which to show the CAPTCHA challenge.

`session_expiration_in_seconds`

(required) The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.

`title`

(required) The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`

`header_text`

(optional) The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from the image below.'

`footer_text`

(optional) The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as they are shown in the image above.'

`failure_message`

(required) The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`

`submit_label`

(required) The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_SUBJECT_NAME_T Type

The entity to be secured by the certificate.

Syntax
```

```

Fields

Field Description

`country`

(optional) ISO 3166-1 alpha-2 code of the country where the organization is located. For a list of codes, see[ISO's website](https://www.iso.org/obp/ui/#search/code/).

`state_province`

(optional) The province where the organization is located.

`locality`

(optional) The city in which the organization is located.

`organization`

(optional) The organization name.

`organizational_unit`

(optional) The field to differentiate between divisions within an organization.

`common_name`

(optional) The fully qualified domain name used for DNS lookups of the server.

`email_address`

(optional) The email address of the server's administrator.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_ISSUER_NAME_T Type

The issuer of the certificate.

Syntax
```

```

Fields

Field Description

`country`

(optional) ISO 3166-1 alpha-2 code of the country where the organization is located. For a list of codes, see[ISO's website](https://www.iso.org/obp/ui/#search/code/).

`state_province`

(optional) The province where the organization is located.

`locality`

(optional) The city in which the organization is located.

`organization`

(optional) The organization name.

`organizational_unit`

(optional) The field to differentiate between divisions within an organization.

`common_name`

(optional) The Certificate Authority (CA) name.

`email_address`

(optional) The email address of the server's administrator.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_PUBLIC_KEY_INFO_T Type

Information about the public key and the algorithm used by the public key.

Syntax
```

```

Fields

Field Description

`algorithm`

(optional) The algorithm identifier and parameters for the public key.

`exponent`

(optional) The private key exponent.

`key_size`

(optional) The number of bits in a key used by a cryptographic algorithm.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_EXTENSIONS_T Type

Syntax
```

```

Fields

Field Description

`name`

(optional) The certificate extension name.

`is_critical`

(optional) The critical flag of the extension. Critical extensions must be processed, non-critical extensions can be ignored.

`value`

(optional) The certificate extension value.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_EXTENSIONS_TBL Type

Nested table type of dbms_cloud_oci_waas_certificate_extensions_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_T Type

The details of the SSL certificate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate's compartment.

`display_name`

(required) The user-friendly name of the certificate.

`issued_by`

(optional)

`subject_name`

(optional)

`issuer_name`

(optional)

`serial_number`

(required) A unique, positive integer assigned by the Certificate Authority (CA). The issuer name and serial number identify a unique certificate.

`version`

(required) The version of the encoded certificate.

`signature_algorithm`

(required) The identifier for the cryptographic algorithm used by the Certificate Authority (CA) to sign this certificate.

`time_not_valid_before`

(required) The date and time the certificate will become valid, expressed in RFC 3339 timestamp format.

`time_not_valid_after`

(required) The date and time the certificate will expire, expressed in RFC 3339 timestamp format.

`public_key_info`

(optional)

`extensions`

(optional) Additional attributes associated with users or public keys for managing relationships between Certificate Authorities.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current lifecycle state of the SSL certificate.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the certificate was created, expressed in RFC 3339 timestamp format.

`is_trust_verification_disabled`

(optional) This indicates whether trust verification was disabled during the creation of SSL certificate. If `true` SSL certificate trust verification was disabled and this SSL certificate is most likely self-signed.

`certificate_data`

(optional) The data of the SSL certificate.

### DBMS_CLOUD_OCI_WAAS_CERTIFICATE_SUMMARY_T Type

A summary of the SSL certificate's information. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SSL certificate.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SSL certificate's compartment.

`display_name`

(optional) The user-friendly name of the SSL certificate.

`time_not_valid_after`

(optional) The date and time the certificate will expire, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current lifecycle state of the certificate.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the certificate was created, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_WAAS_CHANGE_ADDRESS_LIST_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

### DBMS_CLOUD_OCI_WAAS_CHANGE_CERTIFICATE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

### DBMS_CLOUD_OCI_WAAS_CHANGE_CUSTOM_PROTECTION_RULE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

### DBMS_CLOUD_OCI_WAAS_CHANGE_HTTP_REDIRECT_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAAS_CHANGE_WAAS_POLICY_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

### DBMS_CLOUD_OCI_WAAS_CREATE_ADDRESS_LIST_DETAILS_T Type

The data used to create a new address list of IP addresses and CIDR notations.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the address list.

`display_name`

(required) A user-friendly name for the address list.

`addresses`

(required) A list of IP addresses or CIDR notations.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_CREATE_CERTIFICATE_DETAILS_T Type

The data used to create a new SSL certificate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the SSL certificate.

`display_name`

(optional) A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.

`certificate_data`

(required) The data of the SSL certificate. **Note:** Many SSL certificate providers require an intermediate certificate chain to ensure a trusted status. If your SSL certificate requires an intermediate certificate chain, please append the intermediate certificate key in the `certificateData` field after the leaf certificate issued by the SSL certificate provider. If you are unsure if your certificate requires an intermediate certificate chain, see your certificate provider's documentation. The example below shows an intermediate certificate appended to a leaf certificate.

`private_key_data`

(required) The private key of the SSL certificate.

`is_trust_verification_disabled`

(optional) Set to `true` if the SSL certificate is self-signed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_CREATE_CUSTOM_PROTECTION_RULE_DETAILS_T Type

The required data to create a custom protection rule. For more information about custom protection rules, see[Custom Protection Rules](https://docs.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the custom protection rule.

`display_name`

(required) A user-friendly name for the custom protection rule.

`description`

(optional) A description for the Custom Protection rule.

`template`

(required) The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language. Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule. `id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example. `ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated. *Example:* ``` SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 1/2.', \\ id: {{id_1}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 2/2.', \\ id: {{id_2}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" ``` The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase. For more information about custom protection rules, see[Custom Protection Rules](https://docs.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm). For more information about ModSecurity syntax, see[Making Rules: The Basic Syntax](https://www.modsecurity.org/CRS/Documentation/making.html). For more information about ModSecurity's open source WAF rules, see[Mod Security's OWASP Core Rule Set documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_TARGET_T Type

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol used for the target, http or https.

Allowed values are: 'HTTP', 'HTTPS'

`host`

(required) The host portion of the redirect.

`port`

(optional) Port number of the target destination of the redirect, default to match protocol

`path`

(required) The path component of the target URL (e.g., \"/path/to/resource\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying, or request-prefixing. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value is treated the same as static \"/\". A static value must begin with a leading \"/\", optionally followed by other path characters. A request-copying value must exactly match \"{path}\", and will be replaced with the path component of the request URL (including its initial \"/\"). A request-prefixing value must start with \"/\" and end with a non-escaped \"{path}\", which will be replaced with the path component of the request URL (including its initial \"/\"). Only one such replacement token is allowed.

`query`

(required) The query component of the target URL (e.g., \"?redirected\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value results in a redirection target URL with no query component. A static value must begin with a leading \"?\", optionally followed by other query characters. A request-copying value must exactly match \"{query}\", and will be replaced with the query component of the request URL (including a leading \"?\" if and only if the request URL includes a query component).

### DBMS_CLOUD_OCI_WAAS_CREATE_HTTP_REDIRECT_DETAILS_T Type

The details of a HTTP Redirect configured to redirect traffic from one hostname to another. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirects compartment.

`display_name`

(optional) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.

`domain`

(required) The domain from which traffic will be redirected.

`target`

(required) The redirect target object including all the redirect data.

`response_code`

(optional) The response code returned for the redirect to the client. For more information, see[RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_HEADER_T Type

An HTTP header with name and value.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the header.

`value`

(required) The value of the header.

### DBMS_CLOUD_OCI_WAAS_HEADER_TBL Type

Nested table type of dbms_cloud_oci_waas_header_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_ORIGIN_T Type

A detailed description of your web application's origin host server. An origin must be defined to set up WAF rules.

Syntax
```

```

Fields

Field Description

`uri`

(required) The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.

`http_port`

(optional) The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`. If `0` is specified - the origin is not used for HTTP traffic.

`https_port`

(optional) The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`. If `0` is specified - the origin is not used for HTTPS traffic.

`custom_headers`

(optional) A list of HTTP headers to forward to your origin.

### DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_ORIGINS_T Type

Syntax
```

```

Fields

Field Description

`origin`

(optional) The IP address or CIDR notation of the origin server.

`weight`

(optional) The weight of the origin used in load balancing. Origins with higher weights will receive larger proportions of client requests.

### DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_ORIGINS_TBL Type

Nested table type of dbms_cloud_oci_waas_origin_group_origins_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_T Type

Syntax
```

```

Fields

Field Description

`origins`

(optional) The list of objects containing origin references and additional properties.

### DBMS_CLOUD_OCI_WAAS_LOAD_BALANCING_METHOD_T Type

Syntax
```

```

Fields

Field Description

`method`

(required) Load balancing methods are algorithms used to efficiently distribute traffic among origin servers. - **[IP_HASH](https://docs.oracle.com/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod):** All the incoming requests from the same client IP address should go to the same content origination server. IP_HASH load balancing method uses origin weights when choosing which origin should the hash be assigned to initially. - **[ROUND_ROBIN](https://docs.oracle.com/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod):** Forwards requests sequentially to the available origin servers. The first request - to the first origin server, the second request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over a period of time, origins will receive a number of requests in proportion to their weight. - **[STICKY_COOKIE](https://docs.oracle.com/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod):** Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request.

Allowed values are: 'IP_HASH', 'ROUND_ROBIN', 'STICKY_COOKIE'

### DBMS_CLOUD_OCI_WAAS_HEALTH_CHECK_T Type

Health checks monitor the status of your origin servers and only route traffic to the origins that pass the health check. If the health check fails, origin is automatically removed from the load balancing. There is roughly one health check per EDGE POP per period. Any checks that pass will be reported as \"healthy\".

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Enables or disables the health checks.

`method`

(optional) An HTTP verb (i.e. HEAD, GET, or POST) to use when performing the health check.

Allowed values are: 'GET', 'HEAD', 'POST'

`path`

(optional) Path to visit on your origins when performing the health check.

`headers`

(optional) HTTP header fields to include in health check requests, expressed as `\"name\": \"value\"` properties. Because HTTP header field names are case-insensitive, any use of names that are case-insensitive equal to other names will be rejected. If Host is not specified, requests will include a Host header field with value matching the policy's protected domain. If User-Agent is not specified, requests will include a User-Agent header field with value \"waf health checks\". **Note:** The only currently-supported header fields are Host and User-Agent.

`expected_response_code_group`

(optional) The HTTP response codes that signify a healthy state. - **2XX:** Success response code group. - **3XX:** Redirection response code group. - **4XX:** Client errors response code group. - **5XX:** Server errors response code group.

Allowed values are: '2XX', '3XX', '4XX', '5XX'

`is_response_text_check_enabled`

(optional) Enables or disables additional check for predefined text in addition to response code.

`expected_response_text`

(optional) Health check will search for the given text in a case-sensitive manner within the response body and will fail if the text is not found.

`interval_in_seconds`

(optional) Time between health checks of an individual origin server, in seconds.

`timeout_in_seconds`

(optional) Response timeout represents wait time until request is considered failed, in seconds.

`healthy_threshold`

(optional) Number of successful health checks after which the server is marked up.

`unhealthy_threshold`

(optional) Number of failed health checks after which the server is marked down.

### DBMS_CLOUD_OCI_WAAS_POLICY_CONFIG_T Type

The configuration details for the WAAS policy.

Syntax
```

```

Fields

Field Description

`certificate_id`

(optional) The OCID of the SSL certificate to use if HTTPS is supported.

`is_https_enabled`

(optional) Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.

`is_https_forced`

(optional) Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.

`tls_protocols`

(optional) A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification. - **TLS_V1_1:** corresponds to TLS 1.1 specification. - **TLS_V1_2:** corresponds to TLS 1.2 specification. - **TLS_V1_3:** corresponds to TLS 1.3 specification. Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.

Allowed values are: 'TLS_V1', 'TLS_V1_1', 'TLS_V1_2', 'TLS_V1_3'

`is_origin_compression_enabled`

(optional) Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the empty `Accept-Encoding:` header is used.

`is_behind_cdn`

(optional) Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.

`client_address_header`

(optional) Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled. The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last IP address in the header's value as the true IP address. Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3` In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP address to prevent spoofing. - **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name. - **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name. - **X_REAL_IP:** Corresponds to `X-Real-Ip` header name. - **CLIENT_IP:** Corresponds to `Client-Ip` header name. - **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.

Allowed values are: 'X_FORWARDED_FOR', 'X_CLIENT_IP', 'X_REAL_IP', 'CLIENT_IP', 'TRUE_CLIENT_IP'

`is_cache_control_respected`

(optional) Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.

`is_response_buffering_enabled`

(optional) Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.

`cipher_group`

(optional) The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes only. - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`

Allowed values are: 'DEFAULT'

`load_balancing_method`

(optional) An object that represents a load balancing method and its properties.

`websocket_path_prefixes`

(optional) ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.

`is_sni_enabled`

(optional) SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.

`health_checks`

(optional)

### DBMS_CLOUD_OCI_WAAS_DEVICE_FINGERPRINT_CHALLENGE_T Type

The device fingerprint challenge settings. The device fingerprint challenge generates hashed signatures of both virtual and real browsers to identify and block malicious bots.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables or disables the device fingerprint challenge Web Application Firewall feature.

`action`

(optional) The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.

Allowed values are: 'DETECT', 'BLOCK'

`failure_threshold`

(optional) The number of failed requests allowed before taking action. If unspecified, defaults to `10`.

`action_expiration_in_seconds`

(optional) The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.

`failure_threshold_expiration_in_seconds`

(optional) The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.

`max_address_count`

(optional) The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.

`max_address_count_expiration_in_seconds`

(optional) The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.

`challenge_settings`

(optional)

### DBMS_CLOUD_OCI_WAAS_HUMAN_INTERACTION_CHALLENGE_T Type

The human interaction challenge settings. The human interaction challenge checks various event listeners in the user's browser to determine if there is a human user making a request.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables or disables the human interaction challenge Web Application Firewall feature.

`action`

(optional) The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.

Allowed values are: 'DETECT', 'BLOCK'

`failure_threshold`

(optional) The number of failed requests before taking action. If unspecified, defaults to `10`.

`action_expiration_in_seconds`

(optional) The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.

`failure_threshold_expiration_in_seconds`

(optional) The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.

`interaction_threshold`

(optional) The number of interactions required to pass the challenge. If unspecified, defaults to `3`.

`recording_period_in_seconds`

(optional) The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.

`set_http_header`

(optional) Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.

`challenge_settings`

(optional)

`is_nat_enabled`

(optional) When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.

### DBMS_CLOUD_OCI_WAAS_JS_CHALLENGE_T Type

The JavaScript challenge settings. JavaScript Challenge is the function to filter abnormal or malicious bots and allow access to real clients.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables or disables the JavaScript challenge Web Application Firewall feature.

`action`

(optional) The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.

Allowed values are: 'DETECT', 'BLOCK'

`failure_threshold`

(optional) The number of failed requests before taking action. If unspecified, defaults to `10`.

`action_expiration_in_seconds`

(optional) The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.

`set_http_header`

(optional) Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.

`challenge_settings`

(optional)

`are_redirects_challenged`

(optional) When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an HTML body containing JavaScript page redirection.

`criteria`

(optional) When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.

`is_nat_enabled`

(optional) When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.

### DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_EXCLUSION_T Type

Allows specified types of requests to bypass the protection rule. If a request matches any of the criteria in the `exclusions` field, the protection rule will not be executed. Rules can have more than one exclusion and exclusions are applied to requests disjunctively, meaning the specified exclusion strings are independently matched against the specified targets of a request. The first target to match a specified string will trigger an exclusion. **Example:** If the following exclusions are defined for a protection rule: \"action\": \"BLOCK\", \"exclusions\": [ { \"target\":\"REQUEST_COOKIES\", \"exclusions\":[\"example.com\", \"12345\", \"219ffwef9w0f\"] }, { \"target\":\"REQUEST_COOKIE_NAMES\", \"exclusions\":[\"OAMAuthnCookie\", \"JSESSIONID\", \"HCM-PSJSESSIONID\"] } ], \"key\": \"1000000\", A request with the cookie name `sessionid` would trigger an exclusion. A request with the cookie name `yourcompany.com` would *not* trigger and exclusion.

Syntax
```

```

Fields

Field Description

`target`

(optional) The target of the exclusion.

Allowed values are: 'REQUEST_COOKIES', 'REQUEST_COOKIE_NAMES', 'ARGS', 'ARGS_NAMES'

`exclusions`

(optional)

### DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_EXCLUSION_TBL Type

Nested table type of dbms_cloud_oci_waas_protection_rule_exclusion_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SETTING_T Type

The OCID and action of a custom protection rule.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule.

`action`

(optional) The action to take when the custom protection rule is triggered. `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the criteria of the custom protection rule are met.

Allowed values are: 'DETECT', 'BLOCK'

`exclusions`

(optional)

### DBMS_CLOUD_OCI_WAAS_PROTECTION_SETTINGS_T Type

The settings used for protection rules.

Syntax
```

```

Fields

Field Description

`block_action`

(optional) If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.

Allowed values are: 'SHOW_ERROR_PAGE', 'SET_RESPONSE_CODE'

`block_response_code`

(optional) The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`.

`block_error_page_message`

(optional) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'

`block_error_page_code`

(optional) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.

`block_error_page_description`

(optional) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`

`max_argument_count`

(optional) The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is enabled, such as the \"Number of Arguments Limits\" rule (key: 960335). Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked: `GET /myapp/path?query=one&amp;query=two&amp;query=three` `POST /myapp/path` with Body `{\"argument1\":\"one\",\"argument2\":\"two\",\"argument3\":\"three\"}`

`max_name_length_per_argument`

(optional) The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \"Values Limits\" rule (key: 960208).

`max_total_name_length_of_arguments`

(optional) The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the \"Total Arguments Limits\" rule (key: 960341).

`recommendations_period_in_days`

(optional) The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified, defaults to `10`. Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.

`is_response_inspected`

(optional) Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`. **Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected.

`max_response_size_in_ki_b`

(optional) The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified, defaults to `1024`.

`allowed_http_methods`

(optional) The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding protection rule is enabled, such as the \"Restrict HTTP Request Methods\" rule (key: 911100).

Allowed values are: 'OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH', 'PROPFIND'

`media_types`

(optional) The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be inspected. If unspecified, defaults to `[\"text/html\", \"text/plain\", \"text/xml\"]`. Supported MIME types include: - text/html - text/plain - text/asp - text/css - text/x-script - application/json - text/webviewhtml - text/x-java-source - application/x-javascript - application/javascript - application/ecmascript - text/javascript - text/ecmascript - text/x-script.perl - text/x-script.phyton - application/plain - application/xml - text/xml

### DBMS_CLOUD_OCI_WAAS_WHITELIST_T Type

An array of IP addresses that bypass the Web Application Firewall. Supports both single IP addresses or subnet masks (CIDR notation).

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name of the whitelist.

`addresses`

(optional) A set of IP addresses or CIDR notations to include in the whitelist.

`address_lists`

(optional) A list of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of IP address lists to include in the whitelist.

### DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_TBL Type

Nested table type of dbms_cloud_oci_waas_access_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CAPTCHA_TBL Type

Nested table type of dbms_cloud_oci_waas_captcha_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CACHING_RULE_TBL Type

Nested table type of dbms_cloud_oci_waas_caching_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SETTING_TBL Type

Nested table type of dbms_cloud_oci_waas_custom_protection_rule_setting_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WHITELIST_TBL Type

Nested table type of dbms_cloud_oci_waas_whitelist_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WAF_CONFIG_DETAILS_T Type

The Web Application Firewall configuration for the WAAS policy creation.

Syntax
```

```

Fields

Field Description

`access_rules`

(optional) The access rules applied to the Web Application Firewall. Access rules allow custom content access policies to be defined and `ALLOW`, `DETECT`, or `BLOCK` actions to be taken on a request when specified criteria are met.

`address_rate_limiting`

(optional) The settings used to limit the number of requests from an IP address.

`captchas`

(optional) A list of CAPTCHA challenge settings. CAPTCHAs challenge requests to ensure a human is attempting to reach the specified URL and not a bot.

`device_fingerprint_challenge`

(optional) The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.

`human_interaction_challenge`

(optional) The human interaction challenge settings. Detects natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.

`js_challenge`

(optional) The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.

`origin`

(optional) The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but is not required upon updating the configuration.

`caching_rules`

(optional) A list of caching rules applied to the web application.

`custom_protection_rules`

(optional) A list of the custom protection rule OCIDs and their actions.

`origin_groups`

(optional) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

`protection_settings`

(optional) The settings applied to protection rules.

`whitelists`

(optional) A list of IP addresses that bypass the Web Application Firewall.

### DBMS_CLOUD_OCI_WAAS_CREATE_WAAS_POLICY_DETAILS_T Type

The required data to create a WAAS policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the WAAS policy.

`display_name`

(optional) A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.

`domain`

(required) The web application domain that the WAAS policy protects.

`additional_domains`

(optional) An array of additional domains for the specified web application.

`origins`

(optional) A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

`origin_groups`

(optional) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

`policy_config`

(optional)

`waf_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_T Type

The details of a custom protection rule.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule's compartment.

`display_name`

(optional) The user-friendly name of the custom protection rule.

`description`

(optional) The description of the custom protection rule.

`mod_security_rule_ids`

(optional) The auto-generated ID for the custom protection rule. These IDs are referenced in logs.

`template`

(optional) The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language. Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule. `id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example. `ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated. *Example:* ``` SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 1/2.', \\ id: {{id_1}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 2/2.', \\ id: {{id_2}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" ``` The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase. For more information about custom protection rules, see[Custom Protection Rules](https://docs.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm). For more information about ModSecurity syntax, see[Making Rules: The Basic Syntax](https://www.modsecurity.org/CRS/Documentation/making.html). For more information about ModSecurity's open source WAF rules, see[Mod Security's OWASP Core Rule Set documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`lifecycle_state`

(optional) The current lifecycle state of the custom protection rule.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the protection rule was created, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SUMMARY_T Type

An overview of a custom protection rule.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule's compartment.

`display_name`

(optional) The user-friendly name of the custom protection rule.

`mod_security_rule_ids`

(optional) The auto-generated ID for the custom protection rule. These IDs are referenced in logs.

`lifecycle_state`

(optional) The current lifecycle state of the custom protection rule.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the protection rule was created, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_EDGE_SUBNET_T Type

The details about an edge node subnet.

Syntax
```

```

Fields

Field Description

`cidr`

(optional) An edge node subnet. This can include /24 or /8 addresses.

`time_modified`

(optional) The date and time the last change was made to the indicated edge node subnet, expressed in RFC 3339 timestamp format.

`l_region`

(optional) The name of the region containing the indicated subnet.

### DBMS_CLOUD_OCI_WAAS_ERROR_T Type

An error code and message.

Syntax
```

```

Fields

Field Description

`code`

(required)

`message`

(required)

### DBMS_CLOUD_OCI_WAAS_EXTEND_HTTP_RESPONSE_HEADER_ACTION_T Type

An object that represents the action of adding a header field to a response. If the header with specified value already exists, nothing will be added. If the header exists with different value, additional header name:value pair will be added. Comma separated header values are not considered individually (instead as a single value) when adding a new header field.

Syntax
```

```

`dbms_cloud_oci_waas_extend_http_response_header_action_t`is a subtype of the`dbms_cloud_oci_waas_header_manipulation_action_t`type.

Fields

Field Description

`header`

(required) A header field name that conforms to RFC 7230. Example: `example_header_name`

`value`

(required) A header field value that conforms to RFC 7230. Example: `example_value`

### DBMS_CLOUD_OCI_WAAS_GOOD_BOT_T Type

The good bot settings. Good bots provides a list of bots which are managed by known providers.

Syntax
```

```

Fields

Field Description

`key`

(required) The unique key for the bot.

`name`

(optional) The bot name.

`is_enabled`

(required) Enables or disables the bot.

`description`

(optional) The description of the bot.

### DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_T Type

The details of a HTTP Redirect configuration to allow redirecting HTTP traffic from a request domain to a new target. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect's compartment.

`display_name`

(optional) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.

`domain`

(optional) The domain from which traffic will be redirected.

`target`

(optional) The redirect target object including all the redirect data.

`response_code`

(optional) The response code returned for the redirect to the client. For more information, see[RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).

`time_created`

(optional) The date and time the policy was created, expressed in RFC 3339 timestamp format.

`lifecycle_state`

(optional) The current lifecycle state of the HTTP Redirect.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_SUMMARY_T Type

The details of a HTTP Redirect configuration to allow redirecting HTTP traffic from a request domain to a new target. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect's compartment.

`display_name`

(optional) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.

`domain`

(optional) The domain from which traffic will be redirected.

`target`

(optional) The redirect target object including all the redirect data.

`response_code`

(optional) The response code returned for the redirect to the client. For more information, see[RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).

`lifecycle_state`

(optional) The current lifecycle state of the HTTP Redirect.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the policy was created, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_IP_HASH_LOAD_BALANCING_METHOD_T Type

An object that represents the `ip-hash` load balancing method.

Syntax
```

```

`dbms_cloud_oci_waas_ip_hash_load_balancing_method_t`is a subtype of the`dbms_cloud_oci_waas_load_balancing_method_t`type.

### DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_T Type

The protection rule settings. Protection rules can allow, block, or trigger an alert if a request meets the parameters of an applied rule.

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique key of the protection rule.

`mod_security_rule_ids`

(optional) The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see[Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`name`

(optional) The name of the protection rule.

`description`

(optional) The description of the protection rule.

`action`

(optional) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.

Allowed values are: 'OFF', 'DETECT', 'BLOCK'

`labels`

(optional) The list of labels for the protection rule. **Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true.

`exclusions`

(optional)

### DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_ACTION_T Type

A protection rule key and the associated action to apply to that rule.

Syntax
```

```

Fields

Field Description

`key`

(required) The unique key of the protection rule.

`action`

(required) The action to apply to the protection rule. If unspecified, defaults to `OFF`.

Allowed values are: 'OFF', 'DETECT', 'BLOCK'

`exclusions`

(optional) The types of requests excluded from the protection rule action. If the requests matches the criteria in the `exclusions`, the protection rule action will not be executed.

### DBMS_CLOUD_OCI_WAAS_PURGE_CACHE_T Type

The list of cached resources to purge. If a resource is not specified, the purge targets all rules in a policy.

Syntax
```

```

Fields

Field Description

`resources`

(optional) A resource to purge, specified by either a hostless absolute path starting with a single slash (Example: `/path/to/resource`) or by a relative path in which the first component will be interpreted as a domain protected by the WAAS policy (Example: `example.com/path/to/resource`).

### DBMS_CLOUD_OCI_WAAS_RECOMMENDATION_T Type

A recommended protection rule for a web application. This recommendation can be accepted to apply it to the Web Application Firewall configuration for this policy. Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended protection rules.

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique key for the recommended protection rule.

`mod_security_rule_ids`

(optional) The list of the ModSecurity rule IDs associated with the protection rule. For more information about ModSecurity's open source WAF rules, see[Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`name`

(optional) The name of the recommended protection rule.

`description`

(optional) The description of the recommended protection rule.

`labels`

(optional) The list of labels for the recommended protection rule.

`recommended_action`

(optional) The recommended action to apply to the protection rule.

### DBMS_CLOUD_OCI_WAAS_REMOVE_HTTP_RESPONSE_HEADER_ACTION_T Type

An object that represents the action of removing from a response all occurrences of header fields with a specified name.

Syntax
```

```

`dbms_cloud_oci_waas_remove_http_response_header_action_t`is a subtype of the`dbms_cloud_oci_waas_header_manipulation_action_t`type.

Fields

Field Description

`header`

(required) A header field name that conforms to RFC 7230. Example: `example_header_name`

### DBMS_CLOUD_OCI_WAAS_ROUND_ROBIN_LOAD_BALANCING_METHOD_T Type

An object that represents the `round-robin` load balancing method.

Syntax
```

```

`dbms_cloud_oci_waas_round_robin_load_balancing_method_t`is a subtype of the`dbms_cloud_oci_waas_load_balancing_method_t`type.

### DBMS_CLOUD_OCI_WAAS_STICKY_COOKIE_LOAD_BALANCING_METHOD_T Type

An object that represents the `sticky-cookie` load balancing method and its properties.

Syntax
```

```

`dbms_cloud_oci_waas_sticky_cookie_load_balancing_method_t`is a subtype of the`dbms_cloud_oci_waas_load_balancing_method_t`type.

Fields

Field Description

`name`

(optional) The name of the cookie used to track the persistence. Can contain any US-ASCII character except separator or control character.

`domain`

(optional) The domain for which the cookie is set, defaults to WAAS policy domain.

`expiration_time_in_seconds`

(optional) The time for which a browser should keep the cookie in seconds. Empty value will cause the cookie to expire at the end of a browser session.

### DBMS_CLOUD_OCI_WAAS_THREAT_FEED_T Type

The settings of the threat intelligence feed. You can block requests from IP addresses based on their reputations with various commercial and open source threat feeds.

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique key of the threat intelligence feed.

`name`

(optional) The name of the threat intelligence feed.

`action`

(optional) The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to `OFF`.

Allowed values are: 'OFF', 'DETECT', 'BLOCK'

`description`

(optional) The description of the threat intelligence feed.

### DBMS_CLOUD_OCI_WAAS_THREAT_FEED_ACTION_T Type

The action to take for a request that has been determined to be potentially malicious.

Syntax
```

```

Fields

Field Description

`key`

(required) The unique key of the object for which the action applies.

`action`

(required) The selected action. If unspecified, defaults to `OFF`.

Allowed values are: 'OFF', 'DETECT', 'BLOCK'

### DBMS_CLOUD_OCI_WAAS_UPDATE_ADDRESS_LIST_DETAILS_T Type

The data used to update the address list: IP addresses and CIDR notations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the address list.

`addresses`

(optional) A list of IP addresses or CIDR notations.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_UPDATE_CERTIFICATE_DETAILS_T Type

The data used to create a new SSL certificate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_UPDATE_CUSTOM_PROTECTION_RULE_DETAILS_T Type

Updates the configuration details of a custom protection rule. Custom protection rules can only be updated if they are not active in a WAAS policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the custom protection rule.

`description`

(optional) A description for the custom protection rule.

`template`

(optional) The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language. Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule. `id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example. `ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated. *Example:* ``` SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 1/2.', \\ id: {{id_1}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\ \"phase:2, \\ msg:'Detects chained SQL injection attempts 2/2.', \\ id: {{id_2}}, \\ ctl:ruleEngine={{mode}}, \\ deny\" ``` The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase. For more information about custom protection rules, see[Custom Protection Rules](https://docs.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm). For more information about ModSecurity syntax, see[Making Rules: The Basic Syntax](https://www.modsecurity.org/CRS/Documentation/making.html). For more information about ModSecurity's open source WAF rules, see[Mod Security's OWASP Core Rule Set documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_UPDATE_HTTP_REDIRECT_DETAILS_T Type

The details of a HTTP Redirect configured to redirect traffic from one hostname to another. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.

`target`

(optional) The redirect target object including all the redirect data.

`response_code`

(optional) The response code returned for the redirect to the client. For more information, see[RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_GOOD_BOT_TBL Type

Nested table type of dbms_cloud_oci_waas_good_bot_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_TBL Type

Nested table type of dbms_cloud_oci_waas_protection_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_THREAT_FEED_TBL Type

Nested table type of dbms_cloud_oci_waas_threat_feed_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WAF_CONFIG_T Type

The Web Application Firewall configuration for the WAAS policy.

Syntax
```

```

Fields

Field Description

`access_rules`

(optional) The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.

`address_rate_limiting`

(optional) The IP address rate limiting settings used to limit the number of requests from an address.

`captchas`

(optional) A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.

`device_fingerprint_challenge`

(optional) The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.

`good_bots`

(optional) A list of bots allowed to access the web application.

`human_interaction_challenge`

(optional) The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.

`js_challenge`

(optional) The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.

`origin`

(optional) The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.

`caching_rules`

(optional) A list of caching rules applied to the web application.

`custom_protection_rules`

(optional) A list of the custom protection rule OCIDs and their actions.

`origin_groups`

(optional) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

`protection_rules`

(optional) A list of the protection rules and their details.

`protection_settings`

(optional) The settings to apply to protection rules.

`threat_feeds`

(optional) A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.

`whitelists`

(optional) A list of IP addresses that bypass the Web Application Firewall.

### DBMS_CLOUD_OCI_WAAS_UPDATE_WAAS_POLICY_DETAILS_T Type

Updates the configuration details of a WAAS policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.

`additional_domains`

(optional) An array of additional domains protected by this WAAS policy.

`origins`

(optional) A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

`origin_groups`

(optional) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

`policy_config`

(optional)

`waf_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_T Type

The details of a Web Application Acceleration and Security (WAAS) policy. A policy describes how the WAAS service should operate for the configured web application. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WAAS policy.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WAAS policy's compartment.

`display_name`

(optional) The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.

`domain`

(optional) The web application domain that the WAAS policy protects.

`additional_domains`

(optional) An array of additional domains for this web application.

`cname`

(optional) The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.

`lifecycle_state`

(optional) The current lifecycle state of the WAAS policy.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the policy was created, expressed in RFC 3339 timestamp format.

`origins`

(optional) A map of host servers (origins) and their keys for the web application. Origin keys are used to associate origins to specific protection rules. The key should be a user-friendly name for the host. **Examples:** `primary` or `secondary`.

`origin_groups`

(optional) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.

`policy_config`

(optional)

`waf_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_CUSTOM_PROTECTION_RULE_SUMMARY_T Type

The OCID and action of a custom protection rule.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom protection rule.

`display_name`

(optional) The user-friendly name of the custom protection rule.

`action`

(optional) The action to take when the custom protection rule is triggered. `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the criteria of the custom protection rule are met.

Allowed values are: 'DETECT', 'BLOCK'

`mod_security_rule_ids`

(optional) The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see[Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).

`exclusions`

(optional)

### DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_SUMMARY_T Type

Summary information about a WAAS policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WAAS policy.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WAAS policy's compartment.

`display_name`

(optional) The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.

`domain`

(optional) The web application domain that the WAAS policy protects.

`lifecycle_state`

(optional) The current lifecycle state of the WAAS policy.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the policy was created, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_WAAS_WAF_BLOCKED_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`time_observed`

(optional) The date and time the blocked requests were observed, expressed in RFC 3339 timestamp format.

`time_range_in_seconds`

(optional) The number of seconds the data covers.

`waf_feature`

(optional) The specific Web Application Firewall feature that blocked the requests, such as JavaScript Challenge or Access Control.

Allowed values are: 'PROTECTION_RULES', 'JS_CHALLENGE', 'ACCESS_RULES', 'THREAT_FEEDS', 'HUMAN_INTERACTION_CHALLENGE', 'DEVICE_FINGERPRINT_CHALLENGE', 'CAPTCHA', 'ADDRESS_RATE_LIMITING'

`l_count`

(optional) The count of blocked requests.

### DBMS_CLOUD_OCI_WAAS_WAF_LOG_T Type

A list of Web Application Firewall log entries. Each entry is a JSON object, including a timestamp property and other fields varying based on log type. Logs record what rules and countermeasures are triggered by requests and are used as a basis to move request handling into block mode. For more information about WAF logs, see[Logs](https://docs.oracle.com/iaas/Content/WAF/Tasks/logs.htm).

Syntax
```

```

Fields

Field Description

`action`

(optional) The action taken on the request, either `ALLOW`, `DETECT`, or `BLOCK`.

`captcha_action`

(optional) The CAPTCHA action taken on the request, `ALLOW` or `BLOCK`. For more information about CAPTCHAs, see `UpdateCaptchas`.

`captcha_expected`

(optional) The CAPTCHA challenge answer that was expected.

`captcha_received`

(optional) The CAPTCHA challenge answer that was received.

`captcha_fail_count`

(optional) The number of times the CAPTCHA challenge was failed.

`client_address`

(optional) The IPv4 address of the requesting client.

`country_name`

(optional) The name of the country where the request originated.

`user_agent`

(optional) The value of the request's `User-Agent` header field.

`domain`

(optional) The `Host` header data of the request.

`protection_rule_detections`

(optional) A map of protection rule keys to detection message details. Detections are requests that matched the criteria of a protection rule but the rule's action was set to `DETECT`.

`http_method`

(optional) The HTTP method of the request.

`request_url`

(optional) The path and query string of the request.

`http_headers`

(optional) The map of the request's header names to their respective values.

`referrer`

(optional) The `Referrer` header value of the request.

`response_code`

(optional) The status code of the response.

`response_size`

(optional) The size in bytes of the response.

`incident_key`

(optional) The incident key of a request. An incident key is generated for each request processed by the Web Application Firewall and is used to idenitfy blocked requests in applicable logs.

`fingerprint`

(optional) The hashed signature of the device's fingerprint. For more information, see `DeviceFingerPrintChallenge`.

`device`

(optional) The type of device that the request was made from.

`country_code`

(optional) ISO 3166-1 alpha-2 code of the country from which the request originated. For a list of codes, see[ISO's website](https://www.iso.org/obp/ui/#search/code/).

`request_headers`

(optional) A map of header names to values of the request sent to the origin, including any headers appended by the Web Application Firewall.

`threat_feed_key`

(optional) The `ThreatFeed` key that matched the request. For more information about threat feeds, see `UpdateThreatFeeds`.

`access_rule_key`

(optional) The `AccessRule` key that matched the request. For more information about access rules, see `UpdateAccessRules`.

`address_rate_limiting_key`

(optional) The `AddressRateLimiting` key that matched the request. For more information about address rate limiting, see `UpdateWafAddressRateLimiting`.

`l_timestamp`

(optional) The date and time the Web Application Firewall processed the request and logged it.

`log_type`

(optional) The type of log of the request. For more about log types, see[Logs](https://docs.oracle.com/iaas/Content/WAF/Tasks/logs.htm).

`origin_address`

(optional) The address of the origin server where the request was sent.

`origin_response_time`

(optional) The amount of time it took the origin server to respond to the request, in seconds.

### DBMS_CLOUD_OCI_WAAS_WAF_METER_DATUM_T Type

Syntax
```

```

Fields

Field Description

`time_observed`

(optional) The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.

`time_range_in_seconds`

(optional) The number of seconds this data covers.

`tenancy_id`

(optional) The tenancy OCID of the data.

`compartment_id`

(optional) The compartment OCID of the data.

`waas_policy_id`

(optional) The policy OCID of the data.

`is_oci_origin`

(optional) True if origin (endpoint) is an OCI resource. False if external.

`is_bot_enabled`

(optional) True if bot manager is enabled.

`request_count`

(optional) The number of incoming requests.

`traffic_in_bytes`

(optional) Traffic in bytes.

`tag_slug`

(optional) The tag slug for the specified `waasPolicyId`.

### DBMS_CLOUD_OCI_WAAS_WAF_REQUEST_T Type

A time series of request counts handled by the Web Application Firewall, including blocked requests.

Syntax
```

```

Fields

Field Description

`time_observed`

(optional) The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.

`time_range_in_seconds`

(optional) The number of seconds this data covers.

`l_count`

(optional) The total number of requests received in this time period.

### DBMS_CLOUD_OCI_WAAS_WAF_TRAFFIC_DATUM_T Type

A time series of traffic data for the Web Application Firewall configured for a policy.

Syntax
```

```

Fields

Field Description

`time_observed`

(optional) The date and time the traffic was observed, rounded down to the start of the range, and expressed in RFC 3339 timestamp format.

`time_range_in_seconds`

(optional) The number of seconds this data covers.

`tenancy_id`

(optional) The tenancy OCID of the data.

`compartment_id`

(optional) The compartment OCID of the data.

`waas_policy_id`

(optional) The policy OCID of the data.

`traffic_in_bytes`

(optional) Traffic in bytes.

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_RESOURCE_T Type

The resource on which the work request is operating.

Syntax
```

```

Fields

Field Description

`action_type`

(optional) How the work request affects the resource.

Allowed values are: 'IN_PROGRESS', 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'PURGED'

`entity_type`

(optional) The resource type the work request affects.

`identifier`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource that the work request affects.

`entity_uri`

(optional) The URI path used while performing a `GET` to access the resource metadata.

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_LOG_ENTRY_T Type

A log message for a work request.

Syntax
```

```

Fields

Field Description

`message`

(optional) The log message.

`l_timestamp`

(optional) The date and time the work request log event happend, expressed in RFC 3339 timestamp format.

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_ERROR_T Type

An object returned in the event of a work request error.

Syntax
```

```

Fields

Field Description

`code`

(optional) A machine-usable code for the error that occurred.

`message`

(optional) The error message.

`l_timestamp`

(optional) The date and time the work request error happened, expressed in RFC 3339 timestamp format.

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_waas_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_waas_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_waas_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_T Type

Many of the API requests you use to create and configure WAAS policies do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. `WorkRequest` objects provide visibility for in-progress work flows. For more information about work requests, see[Viewing the State of a Work Request](https://docs.oracle.com/iaas/Content/Balance/Tasks/viewingworkrequest.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`operation_type`

(required) A description of the operation requested by the work request.

Allowed values are: 'CREATE_WAAS_POLICY', 'UPDATE_WAAS_POLICY', 'DELETE_WAAS_POLICY', 'CREATE_HTTP_REDIRECT', 'UPDATE_HTTP_REDIRECT', 'DELETE_HTTP_REDIRECT', 'PURGE_WAAS_POLICY_CACHE', 'CREATE_CUSTOM_PROTECTION_RULE', 'UPDATE_CUSTOM_PROTECTION_RULE', 'DELETE_CUSTOM_PROTECTION_RULE'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(optional) The resources being used to complete the work request operation.

`percent_complete`

(optional) The percentage of work completed by the work request.

`logs`

(optional) The list of log entries from the work request workflow.

`errors`

(optional) The list of errors that occurred while fulfilling the work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(required) The date and time the work request moved from the `ACCEPTED` state to the `IN_PROGRESS` state, expressed in RFC 3339 timestamp format.

`time_finished`

(required) The date and time the work request was fulfilled or terminated, expressed in RFC 3339 timestamp format.

### DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_SUMMARY_T Type

The summarized details of a work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`operation_type`

(required) A description of the operation requested by the work request.

Allowed values are: 'CREATE_WAAS_POLICY', 'UPDATE_WAAS_POLICY', 'DELETE_WAAS_POLICY', 'CREATE_HTTP_REDIRECT', 'UPDATE_HTTP_REDIRECT', 'DELETE_HTTP_REDIRECT', 'PURGE_WAAS_POLICY_CACHE', 'CREATE_CUSTOM_PROTECTION_RULE', 'UPDATE_CUSTOM_PROTECTION_RULE', 'DELETE_CUSTOM_PROTECTION_RULE'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(optional) The resources being used to complete the work request operation.

`percent_complete`

(optional) The percentage of work completed by the work request.

`time_accepted`

(required) The date and time the work request was created, expressed in RFC 3339 timestamp format.

`time_started`

(required) The date and time the work request moved from the `ACCEPTED` state to the `IN_PROGRESS` state, expressed in RFC 3339 timestamp format.

`time_finished`

(required) The date and time the work request was fulfilled or terminated, in the format defined by RFC3339.

- [WAAS Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-4A457485-B9CA-40F5-8D69-6538306212B0)
- [DBMS_CLOUD_OCI_WAAS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-136D481F-A032-4FD9-AD49-B27F73E4EC08)
- [DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-3D583343-F3E9-4E40-A001-AA6946F5887E)
- [DBMS_CLOUD_OCI_WAAS_HEADER_MANIPULATION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-99E9AD16-CFED-4B65-831B-C136A743242B)
- [DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_CRITERIA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-8D112D2E-8D2D-49DC-83B8-161A7EC2E01B)
- [DBMS_CLOUD_OCI_WAAS_HEADER_MANIPULATION_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-8446FF74-4C10-4C65-B0E4-40A2420A1786)
- [DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FF260E7A-2415-4D50-875D-9F86C8B36A2B)
- [DBMS_CLOUD_OCI_WAAS_ADD_HTTP_RESPONSE_HEADER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-75D2E9C3-ECE8-4FC7-9BAB-26B26F0A5E53)
- [DBMS_CLOUD_OCI_WAAS_ADDRESS_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-C296E565-E7F3-4312-9070-108CF50A6352)
- [DBMS_CLOUD_OCI_WAAS_ADDRESS_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-26220AE4-A3C2-4A49-93ED-0047A9240196)
- [DBMS_CLOUD_OCI_WAAS_ADDRESS_RATE_LIMITING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-7312EBC8-BBD6-45DB-85B1-3072BF291C07)
- [DBMS_CLOUD_OCI_WAAS_BLOCK_CHALLENGE_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-6A6DB5D8-0E33-4DC2-834F-D6031C39DF5A)
- [DBMS_CLOUD_OCI_WAAS_CACHING_RULE_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-5779CC90-96EA-4885-9637-648F28B53B1E)
- [DBMS_CLOUD_OCI_WAAS_CACHING_RULE_CRITERIA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-7A7521F9-0630-4497-A8A2-7598C899E126)
- [DBMS_CLOUD_OCI_WAAS_CACHING_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-4561B3F7-2884-4C24-8C2D-2B7152468A4E)
- [DBMS_CLOUD_OCI_WAAS_CACHING_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-08E856EB-E6B4-4512-A16A-B04B4EB0E9E4)
- [DBMS_CLOUD_OCI_WAAS_CAPTCHA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-CEC08D9E-EC9B-41B6-8E0C-4DD2FA4AF427)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_SUBJECT_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-4F9A5A17-9E6F-4583-82F8-67581CE0A419)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_ISSUER_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-23B529D7-8A30-4D35-ABCE-D75149265C3F)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_PUBLIC_KEY_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-E9F05724-92DD-438E-9C93-D24BA5DB81A0)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_EXTENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-1E288168-8FE9-496C-83D2-C6B378F7CECC)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_EXTENSIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-BDCC2727-525E-4D4D-9FB4-26AD58209A78)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-CAF1D10B-E1CD-430C-BC62-4FBE50284CB2)
- [DBMS_CLOUD_OCI_WAAS_CERTIFICATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-865D0ABE-F63C-4207-BBE8-31CAA4BE9792)
- [DBMS_CLOUD_OCI_WAAS_CHANGE_ADDRESS_LIST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-EA577E9C-C4CA-4E2A-AC40-E4A6FE181AA4)
- [DBMS_CLOUD_OCI_WAAS_CHANGE_CERTIFICATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-91808983-2B3E-47BE-9758-F56D76B16744)
- [DBMS_CLOUD_OCI_WAAS_CHANGE_CUSTOM_PROTECTION_RULE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-C6C33778-69AE-43C8-8EFE-FA5DC57AEB98)
- [DBMS_CLOUD_OCI_WAAS_CHANGE_HTTP_REDIRECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-4768A478-D774-4305-B40F-6C2A9DB154ED)
- [DBMS_CLOUD_OCI_WAAS_CHANGE_WAAS_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-F8B35E56-9365-4785-9B46-25EB047ACC06)
- [DBMS_CLOUD_OCI_WAAS_CREATE_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-F232E5A4-83CD-44FC-99A2-85FCA409791E)
- [DBMS_CLOUD_OCI_WAAS_CREATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-6B61692A-0C22-4B5F-996B-D7F1A1FE228E)
- [DBMS_CLOUD_OCI_WAAS_CREATE_CUSTOM_PROTECTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-39D69C37-4797-4157-9423-AD5AE8123B11)
- [DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-3B35A41D-B992-42A3-A1BE-75FABC9BB4E2)
- [DBMS_CLOUD_OCI_WAAS_CREATE_HTTP_REDIRECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-92438720-A697-43BD-8E80-0F6C51288E60)
- [DBMS_CLOUD_OCI_WAAS_HEADER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-0CC44910-BE26-4817-9C8C-57D1D9A96988)
- [DBMS_CLOUD_OCI_WAAS_HEADER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-09EACB67-4974-412D-A15E-0D151090A6C3)
- [DBMS_CLOUD_OCI_WAAS_ORIGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-AFF52487-D4BD-4394-AFDD-91ABA5A760A5)
- [DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_ORIGINS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-60222E20-01BB-4300-9A58-DADAEEA05C4B)
- [DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_ORIGINS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-EA5E8919-6F2E-4CB5-91AF-434FA3A8BF9D)
- [DBMS_CLOUD_OCI_WAAS_ORIGIN_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-6C077697-19A2-415D-86F8-8713662F71FC)
- [DBMS_CLOUD_OCI_WAAS_LOAD_BALANCING_METHOD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-B053105A-A757-4B94-B5B1-C8B93045197D)
- [DBMS_CLOUD_OCI_WAAS_HEALTH_CHECK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-91B59811-A5B7-4D70-BF34-4AD5686B9ECF)
- [DBMS_CLOUD_OCI_WAAS_POLICY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FBE26509-B5B6-4851-BC08-7A285094E273)
- [DBMS_CLOUD_OCI_WAAS_DEVICE_FINGERPRINT_CHALLENGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-DA6D1E2F-779A-4B73-8824-3F0398A12F07)
- [DBMS_CLOUD_OCI_WAAS_HUMAN_INTERACTION_CHALLENGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-78FA3EB9-7F22-42FF-801F-12263D0FDCD0)
- [DBMS_CLOUD_OCI_WAAS_JS_CHALLENGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-55180778-1C54-4667-B17A-8F66E8851735)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_EXCLUSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-93A7A85C-2B4C-4160-9ADE-C415A9FF0ECF)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_EXCLUSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-7687E02E-1305-4F6A-ADC5-FF49602CC2F0)
- [DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SETTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-58B88598-91E4-4869-AA48-10D4554FCB38)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-C25E9E20-8683-4E6F-912B-FDB0F5B34A4B)
- [DBMS_CLOUD_OCI_WAAS_WHITELIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-90DACEF7-C460-40C3-A527-1C2D3E5E39C5)
- [DBMS_CLOUD_OCI_WAAS_ACCESS_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-B33659F0-4E40-40F2-AC5A-11CC4EDF67C6)
- [DBMS_CLOUD_OCI_WAAS_CAPTCHA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FC5EA062-B81F-4518-A96F-A3594C449CD8)
- [DBMS_CLOUD_OCI_WAAS_CACHING_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FF3035D2-CD27-4DF4-8E38-64AA66E52BCA)
- [DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SETTING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-8394B38B-5A8B-43D3-AEE6-0E44382E915E)
- [DBMS_CLOUD_OCI_WAAS_WHITELIST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-99D62289-A1B3-4E37-BCB2-EF671374317E)
- [DBMS_CLOUD_OCI_WAAS_WAF_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-80675EE9-7746-4BB2-B1FA-EAF50D6A87EE)
- [DBMS_CLOUD_OCI_WAAS_CREATE_WAAS_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-2D12D4BE-DF60-49AC-895F-A9FC81255934)
- [DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-2EB184A5-2231-4B6A-A438-F1D8F64D792B)
- [DBMS_CLOUD_OCI_WAAS_CUSTOM_PROTECTION_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-E2896E0A-E1CA-4EAB-B89A-0E1F66ED735B)
- [DBMS_CLOUD_OCI_WAAS_EDGE_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-B25A96BC-56F0-413F-90EC-81E129EC4E6C)
- [DBMS_CLOUD_OCI_WAAS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-CFEA9634-F9D3-4E6A-A0F3-74B43E6E9DB1)
- [DBMS_CLOUD_OCI_WAAS_EXTEND_HTTP_RESPONSE_HEADER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-F57CA130-CE01-4E1F-9FE6-1D1791D673CD)
- [DBMS_CLOUD_OCI_WAAS_GOOD_BOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-02F02D4A-64BB-4612-B691-CA1BECEECB17)
- [DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-857E188D-B998-4F56-BDBE-26EB05F78B1E)
- [DBMS_CLOUD_OCI_WAAS_HTTP_REDIRECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-3513AD47-8CAB-424F-8C59-E56AA5B8C86D)
- [DBMS_CLOUD_OCI_WAAS_IP_HASH_LOAD_BALANCING_METHOD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-3BA2B682-4E3B-4375-8B95-391946E85410)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-B9F8D56D-E42B-4DA4-B354-77D056CD4922)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-968C15BF-CAE0-4A78-AD98-BB73E50C0C2B)
- [DBMS_CLOUD_OCI_WAAS_PURGE_CACHE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-529CCB4B-7D19-427B-8B00-4FF28FAB4C52)
- [DBMS_CLOUD_OCI_WAAS_RECOMMENDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-503C500C-C305-45B2-9356-7D16494EC1F9)
- [DBMS_CLOUD_OCI_WAAS_REMOVE_HTTP_RESPONSE_HEADER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-09ED87D7-B77E-4C73-8745-D26332FF11EE)
- [DBMS_CLOUD_OCI_WAAS_ROUND_ROBIN_LOAD_BALANCING_METHOD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-9251F8BB-1BDB-41D3-9286-87C73C77518D)
- [DBMS_CLOUD_OCI_WAAS_STICKY_COOKIE_LOAD_BALANCING_METHOD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-A6F63B84-DB47-4863-9045-3D476CE68B4C)
- [DBMS_CLOUD_OCI_WAAS_THREAT_FEED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-31D3A412-FCC7-4365-AF9B-5FEC5F71748A)
- [DBMS_CLOUD_OCI_WAAS_THREAT_FEED_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-AB352282-859B-4FC5-9491-74A6033C8682)
- [DBMS_CLOUD_OCI_WAAS_UPDATE_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-644ABF38-136C-4BE8-8317-33C229AB1D7F)
- [DBMS_CLOUD_OCI_WAAS_UPDATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-37D7F737-4752-4CAF-9285-EB6781B1CFBE)
- [DBMS_CLOUD_OCI_WAAS_UPDATE_CUSTOM_PROTECTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-A6BA39B4-3E14-4D2A-BAE0-24178EF5B51C)
- [DBMS_CLOUD_OCI_WAAS_UPDATE_HTTP_REDIRECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-A03C8025-A9C0-471F-BD9B-7337A7FEF0BD)
- [DBMS_CLOUD_OCI_WAAS_GOOD_BOT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-45DBDDA8-CF12-4B4C-9D22-78A1B37761C7)
- [DBMS_CLOUD_OCI_WAAS_PROTECTION_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-E75E6C30-6BC9-4754-9AA4-1E64390D317F)
- [DBMS_CLOUD_OCI_WAAS_THREAT_FEED_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-48020B22-5DBF-4E4A-897E-3FD7E40AF976)
- [DBMS_CLOUD_OCI_WAAS_WAF_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-808C9FA3-5A48-40BC-ABFB-6381485A5905)
- [DBMS_CLOUD_OCI_WAAS_UPDATE_WAAS_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-09701EF5-D323-4F1C-B6A4-487DE5B9A30B)
- [DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-12908088-B675-44CA-A7EB-1B5734FF1D1B)
- [DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_CUSTOM_PROTECTION_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-8564ED5C-6AB7-487D-B1BF-2D39A613B91B)
- [DBMS_CLOUD_OCI_WAAS_WAAS_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-7FCE321C-259C-4BCD-B871-057827CEEFA7)
- [DBMS_CLOUD_OCI_WAAS_WAF_BLOCKED_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-A534734A-24C1-4722-A138-C672AF1F57E3)
- [DBMS_CLOUD_OCI_WAAS_WAF_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-8A7ABC73-C3C4-45B2-AB60-62CB36F5E0F0)
- [DBMS_CLOUD_OCI_WAAS_WAF_METER_DATUM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FAB6977C-6F6A-48BD-AFD0-02862C0E8EB6)
- [DBMS_CLOUD_OCI_WAAS_WAF_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-C59AE6B6-ECCD-424F-BA75-10229680BC6F)
- [DBMS_CLOUD_OCI_WAAS_WAF_TRAFFIC_DATUM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-0CDCA802-2A3B-44FE-8E9C-F7232196CC00)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-A4D3116C-3833-484C-9709-74FB5AB6F73A)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-C09BBAFE-65F8-4135-AB28-3DC341617046)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-23FE45A4-5340-42C2-83B6-6224D1F234BA)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-FA6A9408-AA3A-458F-821E-0FE12D65843E)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-57946E96-7DA2-41B4-AE71-74136EBEFD56)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-1E23D439-4E7F-4EBD-8DF5-2B4FD56114CC)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-83A0CEDB-81CB-4E87-A5C8-989885715435)
- [DBMS_CLOUD_OCI_WAAS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waas_t.html#ADSDK-GUID-05EAFA23-2EEA-4D85-A048-21299A3E4D5E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
