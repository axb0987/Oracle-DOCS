# Health Checks Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#dcoc-content-body)

## Health Checks Common Types

### DBMS_CLOUD_OCI_HEALTHCHECKS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_HEALTHCHECKS_CHANGE_HTTP_MONITOR_COMPARTMENT_DETAILS_T Type

The request body used to move a monitor into a compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_HEALTHCHECKS_CHANGE_PING_MONITOR_COMPARTMENT_DETAILS_T Type

The request body used to move a monitor into a compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_HEALTHCHECKS_CONNECTION_T Type

The network connection results.

Syntax
```

```

Fields

Field Description

`address`

(optional) The connection IP address.

`port`

(optional) The port.

### DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_HTTP_MONITOR_DETAILS_T Type

The request body used to create an HTTP monitor.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`targets`

(required) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(required)

Allowed values are: 'HTTP', 'HTTPS'

`method`

(optional)

Allowed values are: 'GET', 'HEAD'

`path`

(optional) The optional URL path to probe, including query parameters.

`headers`

(optional) A dictionary of HTTP request headers. *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.

`display_name`

(required) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(required) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_ON_DEMAND_HTTP_PROBE_DETAILS_T Type

The request body used to create an on-demand HTTP probe.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`targets`

(required) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(required)

Allowed values are: 'HTTP', 'HTTPS'

`method`

(optional)

Allowed values are: 'GET', 'HEAD'

`path`

(optional) The optional URL path to probe, including query parameters.

`headers`

(optional) A dictionary of HTTP request headers. *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.

### DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_ON_DEMAND_PING_PROBE_DETAILS_T Type

The request body used to create an on-demand ping probe.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`targets`

(required) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(required)

Allowed values are: 'ICMP', 'TCP'

### DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_PING_MONITOR_DETAILS_T Type

The request body used to create a Ping monitor.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`targets`

(required) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(required)

Allowed values are: 'ICMP', 'TCP'

`display_name`

(required) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(required) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_HEALTHCHECKS_DNS_T Type

The DNS resolution results.

Syntax
```

```

Fields

Field Description

`domain_lookup_duration`

(optional) Total DNS resolution duration, in milliseconds. Calculated using `domainLookupEnd` minus `domainLookupStart`.

`addresses`

(optional) The addresses returned by DNS resolution.

### DBMS_CLOUD_OCI_HEALTHCHECKS_ERROR_T Type

An error response.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error. Meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_HEALTHCHECKS_GEOLOCATION_T Type

Geographic information about a vantage point.

Syntax
```

```

Fields

Field Description

`geo_key`

(optional) An opaque identifier for the geographic location of the vantage point.

`admin_div_code`

(optional) The ISO 3166-2 code for this location's first-level administrative division, either a US state or Canadian province. Only included for locations in the US or Canada. For a list of codes, see[Country Codes](https://www.iso.org/obp/ui/#search).

`city_name`

(optional) Common English-language name for the city.

`country_code`

(optional) The ISO 3166-1 alpha-2 country code. For a list of codes, see[Country Codes](https://www.iso.org/obp/ui/#search).

`country_name`

(optional) The common English-language name for the country.

`latitude`

(optional) Degrees north of the Equator.

`longitude`

(optional) Degrees east of the prime meridian.

### DBMS_CLOUD_OCI_HEALTHCHECKS_ROUTING_T Type

The routing information for a vantage point.

Syntax
```

```

Fields

Field Description

`as_label`

(optional) The registry label for `asn`, usually the name of the organization that owns the ASN. May be omitted or null.

`asn`

(optional) The Autonomous System Number (ASN) identifying the organization responsible for routing packets to `prefix`.

`prefix`

(optional) An IP prefix (CIDR syntax) that is less specific than `address`, through which `address` is routed.

`weight`

(optional) An integer between 0 and 100 used to select between multiple origin ASNs when routing to `prefix`. Most prefixes have exactly one origin ASN, in which case `weight` will be 100.

### DBMS_CLOUD_OCI_HEALTHCHECKS_ROUTING_TBL Type

Nested table type of dbms_cloud_oci_healthchecks_routing_t.

Syntax
```

```

### DBMS_CLOUD_OCI_HEALTHCHECKS_HEALTH_CHECKS_VANTAGE_POINT_SUMMARY_T Type

Information about a vantage point.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name for the vantage point. Display names are determined by the best information available and may change over time.

`provider_name`

(optional) The organization on whose infrastructure this vantage point resides. Provider names are not unique, as Oracle Cloud Infrastructure maintains many vantage points in each major provider.

`name`

(optional) The unique, permanent name for the vantage point.

`geo`

(optional)

`routing`

(optional) An array of objects that describe how traffic to this vantage point is routed, including which prefixes and ASNs connect it to the internet. The addresses are sorted from the most-specific to least-specific prefix (the smallest network to largest network). When a prefix has multiple origin ASNs (MOAS routing), they are sorted by weight (highest to lowest). Weight is determined by the total percentage of peers observing the prefix originating from an ASN. Only present if `fields` includes `routing`. The field will be null if the address's routing information is unknown.

### DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_MONITOR_T Type

This model contains all of the mutable and immutable properties for an HTTP monitor.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'HTTP', 'HTTPS'

`method`

(optional)

Allowed values are: 'GET', 'HEAD'

`path`

(optional) The optional URL path to probe, including query parameters.

`headers`

(optional) A dictionary of HTTP request headers. *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_MONITOR_SUMMARY_T Type

A summary containing all of the mutable and immutable properties for an HTTP monitor.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`protocol`

(optional)

Allowed values are: 'HTTP', 'HTTPS'

### DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_PROBE_T Type

A summary that contains all of the mutable and immutable properties for an HTTP probe.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'HTTP', 'HTTPS'

`method`

(optional)

Allowed values are: 'GET', 'HEAD'

`path`

(optional) The optional URL path to probe, including query parameters.

`headers`

(optional) A dictionary of HTTP request headers. *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.

### DBMS_CLOUD_OCI_HEALTHCHECKS_TCP_CONNECTION_T Type

TCP connection results. All durations are in milliseconds.

Syntax
```

```

Fields

Field Description

`address`

(optional) The connection IP address.

`port`

(optional) The port.

`connect_duration`

(optional) Total connect duration, calculated using `connectEnd` minus `connectStart`.

`secure_connect_duration`

(optional) The duration to secure the connection. This value will be zero for insecure connections. Calculated using `connectEnd` minus `secureConnectionStart`.

### DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_PROBE_RESULT_SUMMARY_T Type

The results returned by running an HTTP probe. All times and durations are returned in milliseconds. All times are relative to the POSIX epoch (1970-01-01T00:00Z). Time properties conform to W3C Resource Timing. For more information, see[PerformanceResourceTiming](https://w3c.github.io/resource-timing/#sec-resource-timing)interface.

Syntax
```

```

Fields

Field Description

`key`

(optional) A value identifying this specific probe result. The key is only unique within the results of its probe configuration. The key may be reused after 90 days.

`probe_configuration_id`

(optional) The OCID of the monitor or on-demand probe responsible for creating this result.

`start_time`

(optional) The date and time the probe was executed, expressed in milliseconds since the POSIX epoch. This field is defined by the PerformanceResourceTiming interface of the W3C Resource Timing specification. For more information, see[Resource Timing](https://w3c.github.io/resource-timing/#sec-resource-timing).

`target`

(optional) The target hostname or IP address of the probe.

`vantage_point_name`

(optional) The name of the vantage point that executed the probe.

`is_timed_out`

(optional) True if the probe did not complete before the configured `timeoutInSeconds` value.

`is_healthy`

(optional) True if the probe result is determined to be healthy based on probe type-specific criteria. For HTTP probes, a probe result is considered healthy if the HTTP response code is greater than or equal to 200 and less than 300.

`error_category`

(optional) The category of error if an error occurs executing the probe. The `errorMessage` field provides a message with the error details. * NONE - No error * DNS - DNS errors * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error. * NETWORK - Network-related errors, for example a \"network unreachable\" error. * SYSTEM - Internal system errors.

Allowed values are: 'NONE', 'DNS', 'TRANSPORT', 'NETWORK', 'SYSTEM'

`error_message`

(optional) The error information indicating why a probe execution failed.

`protocol`

(optional)

Allowed values are: 'HTTP', 'HTTPS'

`connection`

(optional)

`dns`

(optional)

`status_code`

(optional) The HTTP response status code.

`domain_lookup_start`

(optional) The time immediately before the vantage point starts the domain name lookup for the resource.

`domain_lookup_end`

(optional) The time immediately before the vantage point finishes the domain name lookup for the resource.

`connect_start`

(optional) The time immediately before the vantage point starts establishing the connection to the server to retrieve the resource.

`secure_connection_start`

(optional) The time immediately before the vantage point starts the handshake process to secure the current connection.

`connect_end`

(optional) The time immediately after the vantage point finishes establishing the connection to the server to retrieve the resource.

`fetch_start`

(optional) The time immediately before the vantage point starts to fetch the resource.

`request_start`

(optional) The time immediately before the vantage point starts requesting the resource from the server.

`response_start`

(optional) The time immediately after the vantage point's HTTP parser receives the first byte of the response.

`response_end`

(optional) The time immediately after the vantage point receives the last byte of the response or immediately before the transport connection is closed, whichever comes first.

`duration`

(optional) The total duration from start of request until response is fully consumed or the connection is closed.

`encoded_body_size`

(optional) The size, in octets, of the payload body prior to removing any applied content-codings.

### DBMS_CLOUD_OCI_HEALTHCHECKS_PING_MONITOR_T Type

A summary containing all of the mutable and immutable properties for a ping monitor.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'ICMP', 'TCP'

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_HEALTHCHECKS_PING_MONITOR_SUMMARY_T Type

This model contains all of the mutable and immutable summary properties for an HTTP monitor.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`protocol`

(optional)

Allowed values are: 'ICMP', 'TCP'

### DBMS_CLOUD_OCI_HEALTHCHECKS_PING_PROBE_T Type

This model contains all of the mutable and immutable properties for a ping probe.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the resource.

`results_url`

(optional) A URL for fetching the probe results.

`home_region`

(optional) The region where updates must be made and where results must be fetched from.

`time_created`

(optional) The RFC 3339-formatted creation date and time of the probe.

`compartment_id`

(optional) The OCID of the compartment.

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'ICMP', 'TCP'

### DBMS_CLOUD_OCI_HEALTHCHECKS_PING_PROBE_RESULT_SUMMARY_T Type

The results returned by running a ping probe. All times and durations are returned in milliseconds. All times are relative to the POSIX epoch (1970-01-01T00:00Z).

Syntax
```

```

Fields

Field Description

`key`

(optional) A value identifying this specific probe result. The key is only unique within the results of its probe configuration. The key may be reused after 90 days.

`probe_configuration_id`

(optional) The OCID of the monitor or on-demand probe responsible for creating this result.

`start_time`

(optional) The date and time the probe was executed, expressed in milliseconds since the POSIX epoch. This field is defined by the PerformanceResourceTiming interface of the W3C Resource Timing specification. For more information, see[Resource Timing](https://w3c.github.io/resource-timing/#sec-resource-timing).

`target`

(optional) The target hostname or IP address of the probe.

`vantage_point_name`

(optional) The name of the vantage point that executed the probe.

`is_timed_out`

(optional) True if the probe did not complete before the configured `timeoutInSeconds` value.

`is_healthy`

(optional) True if the probe result is determined to be healthy based on probe type-specific criteria. For HTTP probes, a probe result is considered healthy if the HTTP response code is greater than or equal to 200 and less than 300.

`error_category`

(optional) The category of error if an error occurs executing the probe. The `errorMessage` field provides a message with the error details. * NONE - No error * DNS - DNS errors * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error. * NETWORK - Network-related errors, for example a \"network unreachable\" error. * SYSTEM - Internal system errors.

Allowed values are: 'NONE', 'DNS', 'TRANSPORT', 'NETWORK', 'SYSTEM'

`error_message`

(optional) The error information indicating why a probe execution failed.

`protocol`

(optional)

Allowed values are: 'ICMP', 'TCP'

`connection`

(optional)

`dns`

(optional)

`domain_lookup_start`

(optional) The time immediately before the vantage point starts the domain name lookup for the resource.

`domain_lookup_end`

(optional) The time immediately before the vantage point finishes the domain name lookup for the resource.

`latency_in_ms`

(optional) The latency of the probe execution, in milliseconds.

`icmp_code`

(optional) The ICMP code of the response message. This field is not used when the protocol is set to TCP. For more information on ICMP codes, see[Internet Control Message Protocol (ICMP) Parameters](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml).

### DBMS_CLOUD_OCI_HEALTHCHECKS_UPDATE_HTTP_MONITOR_DETAILS_T Type

The request body used to update an HTTP monitor.

Syntax
```

```

Fields

Field Description

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'HTTP', 'HTTPS'

`method`

(optional)

Allowed values are: 'GET', 'HEAD'

`path`

(optional) The optional URL path to probe, including query parameters.

`headers`

(optional) A dictionary of HTTP request headers. *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_HEALTHCHECKS_UPDATE_PING_MONITOR_DETAILS_T Type

The request body used to update a ping monitor.

Syntax
```

```

Fields

Field Description

`targets`

(optional) A list of targets (hostnames or IP addresses) of the probe.

`vantage_point_names`

(optional) A list of names of vantage points from which to execute the probe.

`port`

(optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`timeout_in_seconds`

(optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`protocol`

(optional)

Allowed values are: 'ICMP', 'TCP'

`display_name`

(optional) A user-friendly and mutable name suitable for display in a user interface.

`interval_in_seconds`

(optional) The monitor interval in seconds. Valid values: 10, 30, and 60.

`is_enabled`

(optional) Enables or disables the monitor. Set to 'true' to launch monitoring.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Health Checks Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-C8ACC533-8EDC-44DB-9F2A-D26C0AF2D5CC)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-F2D0AFD2-229F-4AC6-9280-1DDAE13AF229)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CHANGE_HTTP_MONITOR_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-08474B12-3A04-42A9-8CA9-D5CDFF0583F8)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CHANGE_PING_MONITOR_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-5D4421E2-3F66-4696-8DDB-3A0235600FA8)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-56F2F8DF-4D06-4FD7-BE67-1968668EB146)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_HTTP_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-C6C73263-A3F5-4DEF-B683-7762A885B1A7)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_ON_DEMAND_HTTP_PROBE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-42C7F279-8E45-4A9F-9DD7-9837AF298D5B)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_ON_DEMAND_PING_PROBE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-15D729AF-78A3-4622-B253-2279B6B34CF2)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_CREATE_PING_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-C100D979-A608-46AE-BD49-A0436D696579)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_DNS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-F35901D2-A6CE-47E8-8CC2-2AB11502C7E8)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-B4BB66EC-A055-4A03-99B4-32616E29ADDF)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_GEOLOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-433BA6F3-0407-4BDA-AE70-4C0BFD121260)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_ROUTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-5ED7E87A-4322-4A24-BD3A-C18EA72B025B)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_ROUTING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-344E57A3-63E5-4AC2-80EB-BBF463202EB6)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_HEALTH_CHECKS_VANTAGE_POINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-DFEE6E52-32BC-4F69-9881-14D0A4EF153B)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_MONITOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-032C7F8A-83C0-41C4-82D9-FCE60AF536CC)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_MONITOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-3FA8DAD4-0227-457E-A51E-B8B7A2D075E1)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_PROBE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-282B3223-D8E4-4968-A239-804E474966C4)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_TCP_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-DF64AC60-E392-4398-A620-E809F042FE5C)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_HTTP_PROBE_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-F03D7681-B054-466E-8ADC-162F05189609)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_PING_MONITOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-AC188508-B133-4166-8FB6-A2E163E34B68)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_PING_MONITOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-792B4534-2BA9-4218-9D35-1740A96FE3F7)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_PING_PROBE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-D6725BCC-1338-4223-A321-B4B9DD48386C)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_PING_PROBE_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-76A7A02E-7391-4AFF-AD23-C3A30E0248A7)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_UPDATE_HTTP_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-8E0BC6D8-9D2B-46F2-BC27-3B9723F1891B)
- [DBMS_CLOUD_OCI_HEALTHCHECKS_UPDATE_PING_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/healthchecks_t.html#ADSDK-GUID-E3694819-1361-4C27-A2DA-5389C0BA7CFA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
