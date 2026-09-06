# DNS Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#dcoc-content-body)

## DNS Common Types

### DBMS_CLOUD_OCI_DNS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_T Type

Properties of an attached view.

Syntax
```

```

Fields

Field Description

`view_id`

(required) The OCID of the view.

### DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_DETAILS_T Type

Properties for defining an attached view.

Syntax
```

```

Fields

Field Description

`view_id`

(required) The OCID of the view.

### DBMS_CLOUD_OCI_DNS_CHANGE_RESOLVER_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resolver, along with its protected default view and resolver endpoints, should be moved.

### DBMS_CLOUD_OCI_DNS_CHANGE_STEERING_POLICY_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the steering policy should be moved.

### DBMS_CLOUD_OCI_DNS_CHANGE_TSIG_KEY_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the TSIG key should be moved.

### DBMS_CLOUD_OCI_DNS_CHANGE_VIEW_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the view should be moved.

### DBMS_CLOUD_OCI_DNS_CHANGE_ZONE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the zone should be moved.

### DBMS_CLOUD_OCI_DNS_DYNECT_MIGRATION_DETAILS_T Type

Details specific to performing a DynECT zone migration.

Syntax
```

```

Fields

Field Description

`customer_name`

(required) DynECT customer name the zone belongs to.

`username`

(required) DynECT API username to perform the migration with.

`password`

(required) DynECT API password for the provided username.

`http_redirect_replacements`

(optional) A map of fully-qualified domain names (FQDNs) to an array of `MigrationReplacement` objects.

### DBMS_CLOUD_OCI_DNS_CREATE_ZONE_BASE_DETAILS_T Type

The body for either defining a new zone or migrating a zone from migrationSource. This is determined by the migrationSource discriminator. NONE indicates creation of a new zone (default). DYNECT indicates migration from a DynECT zone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`migration_source`

(optional) Discriminator that is used to determine whether to create a new zone (NONE) or to migrate an existing DynECT zone (DYNECT).

Allowed values are: 'NONE', 'DYNECT'

`name`

(required) The name of the zone.

`compartment_id`

(required) The OCID of the compartment containing the zone.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DNS_CREATE_MIGRATED_DYNECT_ZONE_DETAILS_T Type

The body for migrating a zone from DynECT. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_create_migrated_dynect_zone_details_t`is a subtype of the`dbms_cloud_oci_dns_create_zone_base_details_t`type.

Fields

Field Description

`dynect_migration_details`

(optional)

### DBMS_CLOUD_OCI_DNS_CREATE_RESOLVER_ENDPOINT_DETAILS_T Type

The body for defining a new resolver endpoint. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.

`endpoint_type`

(optional) The type of resolver endpoint. VNIC is currently the only supported type.

Allowed values are: 'VNIC'

`forwarding_address`

(optional) An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.

`is_forwarding`

(required) A Boolean flag indicating whether or not the resolver endpoint is for forwarding.

`is_listening`

(required) A Boolean flag indicating whether or not the resolver endpoint is for listening.

`listening_address`

(optional) An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.

### DBMS_CLOUD_OCI_DNS_CREATE_RESOLVER_VNIC_ENDPOINT_DETAILS_T Type

The body for defining a new resolver VNIC endpoint. Either isForwarding or isListening must be true, but not both. If isListening is true, a listeningAddress may be provided. If isForwarding is true, a forwardingAddress may be provided. When not provided, an address will be chosen automatically. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_create_resolver_vnic_endpoint_details_t`is a subtype of the`dbms_cloud_oci_dns_create_resolver_endpoint_details_t`type.

Fields

Field Description

`subnet_id`

(required) The OCID of a subnet. Must be part of the VCN that the resolver is attached to.

`nsg_ids`

(optional) An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.

### DBMS_CLOUD_OCI_DNS_CREATE_STEERING_POLICY_ATTACHMENT_DETAILS_T Type

The body for defining an attachment between a steering policy and a domain. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`steering_policy_id`

(required) The OCID of the attached steering policy.

`zone_id`

(required) The OCID of the attached zone.

`domain_name`

(required) The attached domain within the attached zone.

`display_name`

(optional) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ANSWER_T Type

DNS record data with metadata for processing in a steering policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name for the answer, unique within the steering policy. An answer's `name` property can be referenced in `answerCondition` properties of rules using `answer.name`. **Example:** \"rules\": [ { \"ruleType\": \"FILTER\", \"defaultAnswerData\": [ { \"answerCondition\": \"answer.name == 'server 1'\", \"shouldKeep\": true } ] } ]

`rtype`

(required) The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more information, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).

`rdata`

(required) The record's data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).

`pool`

(optional) The freeform name of a group of one or more records in which this record is included, such as \"LAX data center\". An answer's `pool` property can be referenced in `answerCondition` properties of rules using `answer.pool`. **Example:** \"rules\": [ { \"ruleType\": \"FILTER\", \"defaultAnswerData\": [ { \"answerCondition\": \"answer.pool == 'US East Servers'\", \"shouldKeep\": true } ] } ]

`is_disabled`

(optional) Set this property to `true` to indicate that the answer is administratively disabled, such as when the corresponding server is down for maintenance. An answer's `isDisabled` property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`. **Example:** \"rules\": [ { \"ruleType\": \"FILTER\", \"defaultAnswerData\": [ { \"answerCondition\": \"answer.isDisabled != true\", \"shouldKeep\": true } ] },

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_RULE_T Type

The configuration of the sorting and filtering behaviors in a steering policy. Rules can filter and sort answers based on weight, priority, endpoint health, and other data. A rule may optionally include a sequence of cases, each with an optional `caseCondition` expression. Cases allow a sequence of conditions to be defined that will apply different parameters to the rule when the conditions are met. For more information about cases, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`description`

(optional) A user-defined description of the rule's purpose or behavior.

`rule_type`

(required) The type of a rule determines its sorting/filtering behavior. * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain only if their `shouldKeep` value is `true`. * `HEALTH` - Removes answers from the list if their `rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down. * `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served in relation to other answers. Anwers with a higher weight will be served more frequently. * `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`. * `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount` specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and there are five answers left, when the `LIMIT` rule is processed, only the first two answers will remain in the list.

Allowed values are: 'FILTER', 'HEALTH', 'WEIGHTED', 'PRIORITY', 'LIMIT'

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ANSWER_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_answer_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_RULE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_CREATE_STEERING_POLICY_DETAILS_T Type

The body for defining a new steering policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the steering policy.

`display_name`

(required) A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.

`ttl`

(optional) The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.

`health_check_monitor_id`

(optional) The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy. **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see[Managing Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm).

`template`

(required) A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries. **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability. It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy. All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm). **Template Types** * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy. * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights. * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see[Traffic Management Geographic Locations](https://docs.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm). * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN. * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address. * `CUSTOM` - Allows a customized configuration of rules.

Allowed values are: 'FAILOVER', 'LOAD_BALANCE', 'ROUTE_BY_GEO', 'ROUTE_BY_ASN', 'ROUTE_BY_IP', 'CUSTOM'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`answers`

(optional) The set of all answers that can potentially issue from the steering policy.

`rules`

(optional) The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request. The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.

### DBMS_CLOUD_OCI_DNS_CREATE_TSIG_KEY_DETAILS_T Type

The body for defining a TSIG key. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) TSIG key algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see[RFC 4635](https://tools.ietf.org/html/rfc4635#section-2).

`name`

(required) A globally unique domain name identifying the key for a given pair of hosts.

`compartment_id`

(required) The OCID of the compartment containing the TSIG key.

`secret`

(required) A base64 string encoding the binary shared secret.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DNS_CREATE_VIEW_DETAILS_T Type

The body for defining a new view. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the owning compartment.

`display_name`

(optional) The display name of the view.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DNS_EXTERNAL_MASTER_T Type

An external master name server used as the source of zone data.

Syntax
```

```

Fields

Field Description

`address`

(required) The server's IP address (IPv4 or IPv6).

`port`

(optional) The server's port. Port value must be a value of 53, otherwise omit the port value.

`tsig_key_id`

(optional) The OCID of the TSIG key.

### DBMS_CLOUD_OCI_DNS_EXTERNAL_DOWNSTREAM_T Type

External downstream nameserver for the zone. This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.

Syntax
```

```

Fields

Field Description

`address`

(required) The server's IP address (IPv4 or IPv6).

`port`

(optional) The server's port. Port value must be a value of 53, otherwise omit the port value.

`tsig_key_id`

(optional) The OCID of the TSIG key. A TSIG key is used to secure DNS messages (in this case, zone transfers) between two systems that both have the (shared) secret.

### DBMS_CLOUD_OCI_DNS_EXTERNAL_MASTER_TBL Type

Nested table type of dbms_cloud_oci_dns_external_master_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_EXTERNAL_DOWNSTREAM_TBL Type

Nested table type of dbms_cloud_oci_dns_external_downstream_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_CREATE_ZONE_DETAILS_T Type

The body for defining a new zone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_create_zone_details_t`is a subtype of the`dbms_cloud_oci_dns_create_zone_base_details_t`type.

Fields

Field Description

`zone_type`

(optional) The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.

Allowed values are: 'PRIMARY', 'SECONDARY'

`view_id`

(optional) This value will be null for zones in the global DNS.

`scope`

(optional) The scope of the zone.

Allowed values are: 'GLOBAL', 'PRIVATE'

`external_masters`

(optional) External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

`external_downstreams`

(optional) External secondary servers for the zone. This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.

### DBMS_CLOUD_OCI_DNS_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DNS_MIGRATION_REPLACEMENT_T Type

A record to add to a zone in replacement of contents that cannot be migrated.

Syntax
```

```

Fields

Field Description

`rtype`

(required) The type of DNS record, such as A or CNAME. For more information, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`substitute_rtype`

(optional) The canonical name for a substitute type of the replacement record to be used if the specified `rtype` is not allowed at the domain. The specified `ttl` and `rdata` will still apply with the substitute type.

`ttl`

(required) The Time To Live of the replacement record, in seconds.

`rdata`

(required) The record data of the replacement record, as whitespace-delimited tokens in type-specific presentation format.

### DBMS_CLOUD_OCI_DNS_NAMESERVER_T Type

A server that has been set up to answer DNS queries for a zone.

Syntax
```

```

Fields

Field Description

`hostname`

(required) The hostname of the nameserver.

### DBMS_CLOUD_OCI_DNS_RECORD_OPERATION_T Type

An extension of the existing record resource, describing either a precondition, an add, or a remove. Preconditions check all fields, including read-only data like `recordHash` and `rrsetVersion`.

Syntax
```

```

Fields

Field Description

`domain`

(optional) The fully qualified domain name where the record can be located.

`record_hash`

(optional) A unique identifier for the record within its zone.

`is_protected`

(optional) A Boolean flag indicating whether or not parts of the record are unable to be explicitly managed.

`rdata`

(optional) The record's data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)

`rrset_version`

(optional) The latest version of the record's zone in which its RRSet differs from the preceding version.

`rtype`

(optional) The type of DNS record, such as A or CNAME. For more information, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`ttl`

(optional) The Time To Live for the record, in seconds. Using a TTL lower than 30 seconds is not recommended.

`operation`

(optional) A description of how a record relates to a PATCH operation. - `REQUIRE` indicates a precondition that record data **must** already exist. - `PROHIBIT` indicates a precondition that record data **must not** already exist. - `ADD` indicates that record data **must** exist after successful application. - `REMOVE` indicates that record data **must not** exist after successful application. **Note:** `ADD` and `REMOVE` operations can succeed even if they require no changes when applied, such as when the described records are already present or absent. **Note:** `ADD` and `REMOVE` operations can describe changes for more than one record. **Example:** `{ \"domain\": \"www.example.com\", \"rtype\": \"AAAA\", \"ttl\": 60 }` specifies a new TTL for every record in the www.example.com AAAA RRSet.

Allowed values are: 'REQUIRE', 'PROHIBIT', 'ADD', 'REMOVE'

### DBMS_CLOUD_OCI_DNS_RECORD_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_dns_record_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_PATCH_DOMAIN_RECORDS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_PATCH_RR_SET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_PATCH_ZONE_RECORDS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_RECORD_T Type

A DNS resource record. For more information, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).

Syntax
```

```

Fields

Field Description

`domain`

(optional) The fully qualified domain name where the record can be located.

`record_hash`

(optional) A unique identifier for the record within its zone.

`is_protected`

(optional) A Boolean flag indicating whether or not parts of the record are unable to be explicitly managed.

`rdata`

(optional) The record's data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)

`rrset_version`

(optional) The latest version of the record's zone in which its RRSet differs from the preceding version.

`rtype`

(optional) The type of DNS record, such as A or CNAME. For more information, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`ttl`

(optional) The Time To Live for the record, in seconds. Using a TTL lower than 30 seconds is not recommended.

### DBMS_CLOUD_OCI_DNS_RECORD_TBL Type

Nested table type of dbms_cloud_oci_dns_record_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_RR_SET_T Type

A collection of DNS records of the same domain and type. For more information about record types, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

Syntax
```

```

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_DNS_RECORD_COLLECTION_T Type

A collection of DNS resource records.

Syntax
```

```

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_DNS_RECORD_DETAILS_T Type

A DNS resource record. For more information about records, see[RFC 1034](https://tools.ietf.org/html/rfc1034#section-3.6).

Syntax
```

```

Fields

Field Description

`domain`

(required) The fully qualified domain name where the record can be located.

`record_hash`

(optional) A unique identifier for the record within its zone.

`is_protected`

(optional) A Boolean flag indicating whether or not parts of the record are unable to be explicitly managed.

`rdata`

(required) The record's data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see[Supported DNS Resource Record Types](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)

`rrset_version`

(optional) The latest version of the record's zone in which its RRSet differs from the preceding version.

`rtype`

(required) The type of DNS record, such as A or CNAME. For more information, see[Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`ttl`

(required) The Time To Live for the record, in seconds. Using a TTL lower than 30 seconds is not recommended.

### DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_SUMMARY_T Type

An OCI DNS resolver endpoint. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.

`endpoint_type`

(optional) The type of resolver endpoint. VNIC is currently the only supported type.

Allowed values are: 'VNIC'

`forwarding_address`

(optional) An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.

`is_forwarding`

(required) A Boolean flag indicating whether or not the resolver endpoint is for forwarding.

`is_listening`

(required) A Boolean flag indicating whether or not the resolver endpoint is for listening.

`listening_address`

(optional) An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.

`compartment_id`

(required) The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under and will be updated if the resolver's compartment is changed.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`l_self`

(required) The canonical absolute URL of the resource.

### DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_T Type

A rule for a resolver. Specifying both qnameCoverConditions and clientAddressConditions is not allowed. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`client_address_conditions`

(required) A list of CIDR blocks. The query must come from a client within one of the blocks in order for the rule action to apply.

`qname_cover_conditions`

(required) A list of domain names. The query must be covered by one of the domains in order for the rule action to apply.

`action`

(required) The action determines the behavior of the rule. If a query matches a supplied condition, the action will apply. If there are no conditions on the rule, all queries are subject to the specified action. * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address.

Allowed values are: 'FORWARD'

### DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dns_resolver_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_TBL Type

Nested table type of dbms_cloud_oci_dns_attached_view_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_TBL Type

Nested table type of dbms_cloud_oci_dns_resolver_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_RESOLVER_T Type

An OCI DNS resolver. If the resolver has an attached VCN, the VCN will attempt to answer queries based on the attached views in priority order. If the query does not match any of the attached views, the query will be evaluated against the default view. If the default view does not match, the rules will be evaluated in priority order. If no rules match the query, answers come from Internet DNS. A resolver may have a maximum of 10 resolver endpoints. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the owning compartment.

`attached_vcn_id`

(optional) The OCID of the attached VCN.

`display_name`

(required) The display name of the resolver.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the resolver.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`l_self`

(required) The canonical absolute URL of the resource.

`default_view_id`

(optional) The OCID of the default view.

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

`endpoints`

(required) Read-only array of endpoints for the resolver.

`attached_views`

(required) The attached views. Views are evaluated in order.

`rules`

(optional) Rules for the resolver. Rules are evaluated in order.

### DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_T Type

An OCI DNS resolver endpoint. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.

`endpoint_type`

(optional) The type of resolver endpoint. VNIC is currently the only supported type.

Allowed values are: 'VNIC'

`forwarding_address`

(optional) An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.

`is_forwarding`

(required) A Boolean flag indicating whether or not the resolver endpoint is for forwarding.

`is_listening`

(required) A Boolean flag indicating whether or not the resolver endpoint is for listening.

`listening_address`

(optional) An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.

`compartment_id`

(required) The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under and will be updated if the resolver's compartment is changed.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`l_self`

(required) The canonical absolute URL of the resource.

### DBMS_CLOUD_OCI_DNS_RESOLVER_FORWARD_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_resolver_forward_rule_t`is a subtype of the`dbms_cloud_oci_dns_resolver_rule_t`type.

Fields

Field Description

`destination_addresses`

(required) IP addresses to which queries should be forwarded. Currently limited to a single address.

`source_endpoint_name`

(optional) Case-insensitive name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding interface. The endpoint must have isForwarding set to true.

### DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_DETAILS_T Type

A rule for a resolver. Specifying both qnameCoverConditions and clientAddressConditions is not allowed. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`client_address_conditions`

(optional) A list of CIDR blocks. The query must come from a client within one of the blocks in order for the rule action to apply.

`qname_cover_conditions`

(optional) A list of domain names. The query must be covered by one of the domains in order for the rule action to apply.

`action`

(required) The action determines the behavior of the rule. If a query matches a supplied condition, the action will apply. If there are no conditions on the rule, all queries are subject to the specified action. * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address.

Allowed values are: 'FORWARD'

### DBMS_CLOUD_OCI_DNS_RESOLVER_FORWARD_RULE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_dns_resolver_forward_rule_details_t`is a subtype of the`dbms_cloud_oci_dns_resolver_rule_details_t`type.

Fields

Field Description

`destination_addresses`

(required) IP addresses to which queries should be forwarded. Currently limited to a single address.

`source_endpoint_name`

(required) Case-insensitive name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding interface. The endpoint must have isForwarding set to true.

### DBMS_CLOUD_OCI_DNS_RESOLVER_SUMMARY_T Type

An OCI DNS resolver. If the resolver has an attached VCN, the VCN will attempt to answer queries based on the attached views in priority order. If the query does not match any of the attached views, the query will be evaluated against the default view. If the default view does not match, the rules will be evaluated in priority order. If no rules match the query, answers come from Internet DNS. A resolver may have a maximum of 10 resolver endpoints. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the owning compartment.

`attached_vcn_id`

(optional) The OCID of the attached VCN.

`display_name`

(required) The display name of the resolver.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the resolver.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`l_self`

(required) The canonical absolute URL of the resource.

`default_view_id`

(optional) The OCID of the default view.

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

### DBMS_CLOUD_OCI_DNS_RESOLVER_VNIC_ENDPOINT_T Type

An OCI DNS resolver VNIC endpoint. A VNIC is created for each ResolverVnicEndpoint. VCNs and subnets cannot be deleted while ResolverVnicEndpoints exist in them due to the VNIC. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_resolver_vnic_endpoint_t`is a subtype of the`dbms_cloud_oci_dns_resolver_endpoint_t`type.

Fields

Field Description

`subnet_id`

(optional) The OCID of a subnet. Must be part of the VCN that the resolver is attached to.

`nsg_ids`

(optional) An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.

### DBMS_CLOUD_OCI_DNS_RESOLVER_VNIC_ENDPOINT_SUMMARY_T Type

An OCI DNS resolver VNIC endpoint. A VNIC is created for each ResolverVnicEndpoint. VCNs and subnets cannot be deleted while ResolverVnicEndpoints exist in them due to the VNIC. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_resolver_vnic_endpoint_summary_t`is a subtype of the`dbms_cloud_oci_dns_resolver_endpoint_summary_t`type.

Fields

Field Description

`subnet_id`

(required) The OCID of a subnet. Must be part of the VCN that the resolver is attached to.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_T Type

A DNS steering policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the steering policy.

`display_name`

(required) A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.

`ttl`

(required) The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.

`health_check_monitor_id`

(optional) The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy. **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see[Managing Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm).

`template`

(required) A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries. **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability. It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy. All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm). **Template Types** * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy. * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights. * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see[Traffic Management Geographic Locations](https://docs.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm). * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN. * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address. * `CUSTOM` - Allows a customized configuration of rules.

Allowed values are: 'FAILOVER', 'LOAD_BALANCE', 'ROUTE_BY_GEO', 'ROUTE_BY_ASN', 'ROUTE_BY_IP', 'CUSTOM'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`answers`

(required) The set of all answers that can potentially issue from the steering policy.

`rules`

(required) The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request. The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING'

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ATTACHMENT_T Type

An attachment between a steering policy and a domain. An attachment constructs DNS responses using its steering policy instead of the records at its defined domain. Only records of the policy's covered rtype are blocked at the domain. A domain can have a maximum of one attachment covering any given rtype. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`steering_policy_id`

(required) The OCID of the attached steering policy.

`zone_id`

(required) The OCID of the attached zone.

`domain_name`

(required) The attached domain within the attached zone.

`display_name`

(required) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.

`rtypes`

(required) The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.

`compartment_id`

(required) The OCID of the compartment containing the steering policy attachment.

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING'

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ATTACHMENT_SUMMARY_T Type

An attachment between a steering policy and a domain.

Syntax
```

```

Fields

Field Description

`steering_policy_id`

(required) The OCID of the attached steering policy.

`zone_id`

(required) The OCID of the attached zone.

`domain_name`

(required) The attached domain within the attached zone.

`display_name`

(required) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.

`rtypes`

(required) The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.

`compartment_id`

(required) The OCID of the compartment containing the steering policy attachment.

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING'

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_ANSWER_DATA_T Type

Syntax
```

```

Fields

Field Description

`answer_condition`

(optional) An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.

`should_keep`

(optional) Keeps the answer only if the value is `true`.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_ANSWER_DATA_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_filter_answer_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_CASE_T Type

Syntax
```

```

Fields

Field Description

`case_condition`

(optional) An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.address in ('192.0.2.0/24')` to define a case that matches queries from that office.

`answer_data`

(optional) An array of `SteeringPolicyFilterAnswerData` objects.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_CASE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_filter_rule_case_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_steering_policy_filter_rule_t`is a subtype of the`dbms_cloud_oci_dns_steering_policy_rule_t`type.

Fields

Field Description

`cases`

(optional) An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.

`default_answer_data`

(optional) Defines a default set of answer conditions and values that are applied to an answer when `cases` is not defined for the rule, or a matching case does not have any matching `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_CASE_T Type

Syntax
```

```

Fields

Field Description

`case_condition`

(optional) An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.address in ('192.0.2.0/24')` to define a case that matches queries from that office.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_CASE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_health_rule_case_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_steering_policy_health_rule_t`is a subtype of the`dbms_cloud_oci_dns_steering_policy_rule_t`type.

Fields

Field Description

`cases`

(optional) An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_CASE_T Type

Syntax
```

```

Fields

Field Description

`case_condition`

(optional) An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.address in ('192.0.2.0/24')` to define a case that matches queries from that office.

`l_count`

(required) The number of answers allowed to remain after the limit rule has been processed, keeping only the first of the remaining answers in the list. Example: If the `count` property is set to `2` and four answers remain before the limit rule is processed, only the first two answers in the list will remain after the limit rule has been processed.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_CASE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_limit_rule_case_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_steering_policy_limit_rule_t`is a subtype of the`dbms_cloud_oci_dns_steering_policy_rule_t`type.

Fields

Field Description

`cases`

(optional) An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.

`default_count`

(optional) Defines a default count if `cases` is not defined for the rule or a matching case does not define `count`. `defaultCount` is **not** applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed. If no rules remain to be processed, the answer will be chosen from the remaining list of answers.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_ANSWER_DATA_T Type

Syntax
```

```

Fields

Field Description

`answer_condition`

(optional) An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.

`value`

(required) The rank assigned to the set of answers that match the expression in `answerCondition`. Answers with the lowest values move to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_ANSWER_DATA_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_priority_answer_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_CASE_T Type

Syntax
```

```

Fields

Field Description

`case_condition`

(optional) An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.address in ('192.0.2.0/24')` to define a case that matches queries from that office.

`answer_data`

(optional) An array of `SteeringPolicyPriorityAnswerData` objects.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_CASE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_priority_rule_case_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_steering_policy_priority_rule_t`is a subtype of the`dbms_cloud_oci_dns_steering_policy_rule_t`type.

Fields

Field Description

`cases`

(optional) An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.

`default_answer_data`

(optional) Defines a default set of answer conditions and values that are applied to an answer when `cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_SUMMARY_T Type

A DNS steering policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the steering policy.

`display_name`

(required) A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.

`ttl`

(required) The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.

`health_check_monitor_id`

(optional) The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy. **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see[Managing Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm).

`template`

(required) A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries. **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability. It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy. All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm). **Template Types** * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy. * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights. * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see[Traffic Management Geographic Locations](https://docs.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm). * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN. * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address. * `CUSTOM` - Allows a customized configuration of rules.

Allowed values are: 'FAILOVER', 'LOAD_BALANCE', 'ROUTE_BY_GEO', 'ROUTE_BY_ASN', 'ROUTE_BY_IP', 'CUSTOM'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING'

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_ANSWER_DATA_T Type

Syntax
```

```

Fields

Field Description

`answer_condition`

(optional) An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.

`value`

(required) The weight assigned to the set of selected answers. Answers with a higher weight will be served more frequently. Answers can be given a value between `0` and `255`.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_ANSWER_DATA_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_weighted_answer_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_CASE_T Type

Syntax
```

```

Fields

Field Description

`case_condition`

(optional) An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.address in ('192.0.2.0/24')` to define a case that matches queries from that office.

`answer_data`

(optional) An array of `SteeringPolicyWeightedAnswerData` objects.

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_CASE_TBL Type

Nested table type of dbms_cloud_oci_dns_steering_policy_weighted_rule_case_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_T Type

Syntax
```

```

`dbms_cloud_oci_dns_steering_policy_weighted_rule_t`is a subtype of the`dbms_cloud_oci_dns_steering_policy_rule_t`type.

Fields

Field Description

`cases`

(optional) An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.

`default_answer_data`

(optional) Defines a default set of answer conditions and values that are applied to an answer when `cases` is not defined for the rule or a matching case does not have any matching `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed.

### DBMS_CLOUD_OCI_DNS_TSIG_KEY_T Type

A TSIG key. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) TSIG key algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see[RFC 4635](https://tools.ietf.org/html/rfc4635#section-2).

`name`

(required) A globally unique domain name identifying the key for a given pair of hosts.

`compartment_id`

(required) The OCID of the compartment containing the TSIG key.

`secret`

(required) A base64 string encoding the binary shared secret.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the resource.

`l_self`

(required) The canonical absolute URL of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`time_updated`

(optional) The date and time the resource was last updated, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

### DBMS_CLOUD_OCI_DNS_TSIG_KEY_SUMMARY_T Type

A TSIG key.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) TSIG key algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see[RFC 4635](https://tools.ietf.org/html/rfc4635#section-2).

`name`

(required) A globally unique domain name identifying the key for a given pair of hosts.

`compartment_id`

(required) The OCID of the compartment containing the TSIG key.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the resource.

`l_self`

(required) The canonical absolute URL of the resource.

`time_created`

(required) The date and time the resource was created, expressed in RFC 3339 timestamp format. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

### DBMS_CLOUD_OCI_DNS_RECORD_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_dns_record_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_UPDATE_DOMAIN_RECORDS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_UPDATE_RR_SET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_dns_attached_view_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_dns_resolver_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_DETAILS_T Type

The body for updating an existing resolver. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the resolver.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`attached_views`

(optional) The attached views. Views are evaluated in order.

`rules`

(optional) Rules for the resolver. Rules are evaluated in order.

### DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_ENDPOINT_DETAILS_T Type

The body for updating an existing resolver endpoint. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`endpoint_type`

(optional) The type of resolver endpoint. VNIC is currently the only supported type.

Allowed values are: 'VNIC'

### DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_VNIC_ENDPOINT_DETAILS_T Type

The body for updating an existing resolver VNIC endpoint. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_dns_update_resolver_vnic_endpoint_details_t`is a subtype of the`dbms_cloud_oci_dns_update_resolver_endpoint_details_t`type.

Fields

Field Description

`nsg_ids`

(optional) An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.

### DBMS_CLOUD_OCI_DNS_UPDATE_STEERING_POLICY_ATTACHMENT_DETAILS_T Type

The body for updating a steering policy attachment. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.

### DBMS_CLOUD_OCI_DNS_UPDATE_STEERING_POLICY_DETAILS_T Type

The body for updating a steering policy. New rules and answers provided in the request will replace the existing rules and answers in the policy. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.

`ttl`

(optional) The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.

`health_check_monitor_id`

(optional) The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy. **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see[Managing Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm).

`template`

(optional) A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries. **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability. It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy. All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see[Traffic Management API Guide](https://docs.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm). **Template Types** * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy. * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights. * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see[Traffic Management Geographic Locations](https://docs.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm). * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN. * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address. * `CUSTOM` - Allows a customized configuration of rules.

Allowed values are: 'FAILOVER', 'LOAD_BALANCE', 'ROUTE_BY_GEO', 'ROUTE_BY_ASN', 'ROUTE_BY_IP', 'CUSTOM'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`answers`

(optional) The set of all answers that can potentially issue from the steering policy.

`rules`

(optional) The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request. The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.

### DBMS_CLOUD_OCI_DNS_UPDATE_TSIG_KEY_DETAILS_T Type

The body for updating a TSIG key. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DNS_UPDATE_VIEW_DETAILS_T Type

The body for updating an existing view. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the view.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DNS_UPDATE_ZONE_DETAILS_T Type

The body for updating a zone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`external_masters`

(optional) External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

`external_downstreams`

(optional) External secondary servers for the zone. This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.

### DBMS_CLOUD_OCI_DNS_UPDATE_ZONE_RECORDS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`items`

(optional)

### DBMS_CLOUD_OCI_DNS_VIEW_T Type

An OCI DNS view. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the owning compartment.

`display_name`

(required) The display name of the view.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the view.

`l_self`

(required) The canonical absolute URL of the resource.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'DELETED', 'DELETING', 'UPDATING'

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

### DBMS_CLOUD_OCI_DNS_VIEW_SUMMARY_T Type

An OCI DNS view. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the owning compartment.

`display_name`

(required) The display name of the view.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`id`

(required) The OCID of the view.

`l_self`

(required) The canonical absolute URL of the resource.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`time_updated`

(required) The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`lifecycle_state`

(required) The current state of the resource.

Allowed values are: 'ACTIVE', 'DELETED', 'DELETING', 'UPDATING'

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

### DBMS_CLOUD_OCI_DNS_ZONE_TRANSFER_SERVER_T Type

An OCI nameserver that transfers zone data with external nameservers.

Syntax
```

```

Fields

Field Description

`address`

(required) The server's IP address (IPv4 or IPv6).

`port`

(optional) The server's port.

`is_transfer_source`

(optional) A Boolean flag indicating whether or not the server is a zone data transfer source.

`is_transfer_destination`

(optional) A Boolean flag indicating whether or not the server is a zone data transfer destination.

### DBMS_CLOUD_OCI_DNS_NAMESERVER_TBL Type

Nested table type of dbms_cloud_oci_dns_nameserver_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_ZONE_TRANSFER_SERVER_TBL Type

Nested table type of dbms_cloud_oci_dns_zone_transfer_server_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DNS_ZONE_T Type

A DNS zone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the zone.

`zone_type`

(required) The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.

Allowed values are: 'PRIMARY', 'SECONDARY'

`compartment_id`

(required) The OCID of the compartment containing the zone.

`view_id`

(optional) The OCID of the private view containing the zone. This value will be null for zones in the global DNS, which are publicly resolvable and not part of a private view.

`scope`

(required) The scope of the zone.

Allowed values are: 'GLOBAL', 'PRIVATE'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`external_masters`

(required) External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

`external_downstreams`

(required) External secondary servers for the zone. This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the zone.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`version`

(required) Version is the never-repeating, totally-orderable, version of the zone, from which the serial field of the zone's SOA record is derived.

`serial`

(required) The current serial of the zone. As seen in the zone's SOA record.

`lifecycle_state`

(required) The current state of the zone resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

`nameservers`

(required) The authoritative nameservers for the zone.

`zone_transfer_servers`

(optional) The OCI nameservers that transfer the zone data with external nameservers.

### DBMS_CLOUD_OCI_DNS_ZONE_SUMMARY_T Type

A DNS zone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the zone.

`zone_type`

(required) The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.

Allowed values are: 'PRIMARY', 'SECONDARY'

`compartment_id`

(required) The OCID of the compartment containing the zone.

`view_id`

(optional) The OCID of the private view containing the zone. This value will be null for zones in the global DNS, which are publicly resolvable and not part of a private view.

`scope`

(required) The scope of the zone.

Allowed values are: 'GLOBAL', 'PRIVATE'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

`l_self`

(required) The canonical absolute URL of the resource.

`id`

(required) The OCID of the zone.

`time_created`

(required) The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format with a Z offset, as defined by RFC 3339. **Example:** `2016-07-22T17:23:59:60Z`

`version`

(required) Version is the never-repeating, totally-orderable, version of the zone, from which the serial field of the zone's SOA record is derived.

`serial`

(required) The current serial of the zone. As seen in the zone's SOA record.

`lifecycle_state`

(required) The current state of the zone resource.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING'

`is_protected`

(required) A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.

- [DNS Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-3BF57013-025E-46E5-BD6F-169EB90C29AE)
- [DBMS_CLOUD_OCI_DNS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-AF6115EA-1675-4C77-8135-CC524D6080C6)
- [DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-1979D0CF-02AF-4FD4-AC16-27A871803A29)
- [DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-49A11CD9-6086-4730-8A5A-0266CBFFC721)
- [DBMS_CLOUD_OCI_DNS_CHANGE_RESOLVER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-38AA63A9-7E4A-4C52-AA9E-9D845591E669)
- [DBMS_CLOUD_OCI_DNS_CHANGE_STEERING_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-91173AD3-0CB0-4DC8-9B05-A3F40FD476AA)
- [DBMS_CLOUD_OCI_DNS_CHANGE_TSIG_KEY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-9E9B8A56-A9CF-41D5-8539-503CC7E92E63)
- [DBMS_CLOUD_OCI_DNS_CHANGE_VIEW_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E04647FE-0181-4B45-9508-83EA1DA4F748)
- [DBMS_CLOUD_OCI_DNS_CHANGE_ZONE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-B84B45BB-19B5-4990-9A21-2E7C0D32B723)
- [DBMS_CLOUD_OCI_DNS_DYNECT_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-1C5D2299-79D8-4427-8DE2-DBA0ED079CEB)
- [DBMS_CLOUD_OCI_DNS_CREATE_ZONE_BASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-10F39511-C06E-49A8-895E-221F4BAF41FB)
- [DBMS_CLOUD_OCI_DNS_CREATE_MIGRATED_DYNECT_ZONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-39A2B69A-0629-4ABF-97E5-402F2E90EF5F)
- [DBMS_CLOUD_OCI_DNS_CREATE_RESOLVER_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E4C9129F-540B-4E66-B9F0-0EB021599F04)
- [DBMS_CLOUD_OCI_DNS_CREATE_RESOLVER_VNIC_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-922F94AF-3ED7-4F18-A6C9-DE7F2E93A8D5)
- [DBMS_CLOUD_OCI_DNS_CREATE_STEERING_POLICY_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-D62F0A5B-D725-4484-BEE3-922ED672E526)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ANSWER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-01F090FF-1E4E-4F09-804D-B4AD57DDBEE5)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-C1AEAAD9-329F-4FA0-BE80-122255CFA1D8)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ANSWER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-1F973AFD-2B36-4B99-8F15-85B67F4755D7)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-54C73DB6-C886-4D0E-8833-633642560597)
- [DBMS_CLOUD_OCI_DNS_CREATE_STEERING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-47F8CFA6-A3CA-4C50-BB7F-B86709529E0D)
- [DBMS_CLOUD_OCI_DNS_CREATE_TSIG_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-5797AF53-F245-4085-9051-84B217DE2F3C)
- [DBMS_CLOUD_OCI_DNS_CREATE_VIEW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-38630BB3-81EA-4523-9ED8-C2199F3DE410)
- [DBMS_CLOUD_OCI_DNS_EXTERNAL_MASTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E4173A64-4698-4E06-9AF0-FD36BA5801AE)
- [DBMS_CLOUD_OCI_DNS_EXTERNAL_DOWNSTREAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-3A815CA2-869C-4F8B-A416-7C2150CC6EA8)
- [DBMS_CLOUD_OCI_DNS_EXTERNAL_MASTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-09DA0026-F986-404E-8456-965780BF3271)
- [DBMS_CLOUD_OCI_DNS_EXTERNAL_DOWNSTREAM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-6E93BEA9-B5AD-42EA-A6E6-6C2DC2C896B9)
- [DBMS_CLOUD_OCI_DNS_CREATE_ZONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8A87E9FA-8655-4D7C-8614-065B74C56849)
- [DBMS_CLOUD_OCI_DNS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8C07A71B-2341-4C18-ABE4-230CFD49DA3C)
- [DBMS_CLOUD_OCI_DNS_MIGRATION_REPLACEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-DA17533C-F902-4ED4-8EAD-D1FB3486B116)
- [DBMS_CLOUD_OCI_DNS_NAMESERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-817DD6B9-9CC9-40F0-A26F-ABA9FE85DF0B)
- [DBMS_CLOUD_OCI_DNS_RECORD_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-F9D810B9-A4DC-439E-B762-74A8C6CB2982)
- [DBMS_CLOUD_OCI_DNS_RECORD_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-A0B3D30F-ADDF-46A5-A7EF-F9703F9F9475)
- [DBMS_CLOUD_OCI_DNS_PATCH_DOMAIN_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-BDFC658B-B197-45A1-9A0E-FC1A633F54FF)
- [DBMS_CLOUD_OCI_DNS_PATCH_RR_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E47F74E6-AE26-4E0A-8317-9D3BBC396381)
- [DBMS_CLOUD_OCI_DNS_PATCH_ZONE_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-9AAA07A9-2163-41CD-89FD-17557EDAFF90)
- [DBMS_CLOUD_OCI_DNS_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8E372F92-2E2D-4F61-AE86-AAADCA512CA9)
- [DBMS_CLOUD_OCI_DNS_RECORD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-B280AA38-7285-4F40-B79D-769A61BC58D4)
- [DBMS_CLOUD_OCI_DNS_RR_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-6F2FBE05-1437-4EBB-AB7D-CF90516FA04A)
- [DBMS_CLOUD_OCI_DNS_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-01DAD60B-8B08-4FBB-A885-43264CA17FBB)
- [DBMS_CLOUD_OCI_DNS_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-06A0A8B2-C4B5-44AB-9102-0C133F28FED8)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-C7CC6398-F166-4D3D-9540-EBD309FDCFA9)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-A0A2DA8C-4308-4592-A320-24EA46B67653)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-86A13110-643B-45F2-B5E6-64B43A9B4094)
- [DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-21470681-CA06-47F2-B3E6-09DD74481EFC)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-262E1B11-7BF9-451D-8CA2-FA8051589647)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-4A2E4133-8565-4082-B073-4E81119C1EE0)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E7969526-440C-4DF3-BF85-4777C050068B)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_FORWARD_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-3B4A8013-1619-4621-8DBC-8A17355395F2)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E7AED8E4-4940-4723-80D0-454B280A26F2)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_FORWARD_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E4EB58C8-6A50-4691-90C3-F7D4D47DD7E7)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-D58E9A5F-8DF0-4BE6-A6E9-095CF8627714)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_VNIC_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-FBC12754-F802-4CE0-AFDA-C15910375780)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_VNIC_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-23C51438-8C83-499E-A60C-4BB3CE6FC28F)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-10691B01-F7EA-478A-902D-86BD73405C7B)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-F90F4A95-EE43-475A-A4D1-B3C4D30B12AF)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-AB8CC147-1805-4DBB-968C-54E914963346)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_ANSWER_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-070AF8F8-DE31-4684-9FDC-AE73999CE138)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_ANSWER_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-BB9ED51F-E66A-4B55-92EA-1659E9CEE812)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_CASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8CFD638C-C281-4ACE-9D09-C30977A941D3)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_CASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-EF04393A-1642-4C67-959E-66F7F47A1DBF)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_FILTER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-9D866D76-09BD-4AA3-8262-D841F0265236)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_CASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-2C311409-9BD4-4085-A9C1-0B2D712D20FA)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_CASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8625D37E-4F08-4E40-B73B-4A7E0310032E)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_HEALTH_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-E41D0605-F000-4265-97DE-2B58697FE574)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_CASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-155967EF-20F9-4B0C-9585-212F6C2454DC)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_CASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-33B430BC-91AB-4FB6-92CC-21332E45EEA3)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_LIMIT_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-9E41247B-48A8-44B4-B1DD-0799EFAFBB58)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_ANSWER_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-FD2B2780-7911-46E5-9E55-B91BAE18EFCC)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_ANSWER_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-355450DF-3D6F-4A4C-8A4E-A934CCD405B4)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_CASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-09808CF4-68DF-4B35-9ADF-50E6244DDB93)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_CASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-A7581DC6-4BEF-40F0-9313-D7600509EF7E)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_PRIORITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-870E9D52-A234-4182-ABA9-F23A2597F152)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-1FF141B5-F934-4F36-82AE-9E7618E783B4)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_ANSWER_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-F013825D-DF0F-4DF2-9B25-8E068A87D4B0)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_ANSWER_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-2FC4B0DA-58B2-4227-A4FC-8AA044191C1F)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_CASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-F925FEE9-F385-4FBB-941D-6D7704C44A3E)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_CASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-C5FFEEF8-4FA6-416A-A512-E67740135CE0)
- [DBMS_CLOUD_OCI_DNS_STEERING_POLICY_WEIGHTED_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-D41F03C7-8768-4B24-BFF6-F172F6D007EC)
- [DBMS_CLOUD_OCI_DNS_TSIG_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-FBF4D57F-86CA-459D-9EE3-E1495B83D984)
- [DBMS_CLOUD_OCI_DNS_TSIG_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-602385AC-A88F-486F-B42B-C0729CB804F3)
- [DBMS_CLOUD_OCI_DNS_RECORD_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-1906A99F-5F2B-41BD-A8DB-7C39A7F0DF0E)
- [DBMS_CLOUD_OCI_DNS_UPDATE_DOMAIN_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-8CD3A708-18E4-46A6-BACE-C3A2BE461C78)
- [DBMS_CLOUD_OCI_DNS_UPDATE_RR_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-D18AE9D6-45C0-4C56-8DAB-A2C220BB2FFB)
- [DBMS_CLOUD_OCI_DNS_ATTACHED_VIEW_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-4E7B7B2D-00FC-4033-B714-1E0D64E7FA43)
- [DBMS_CLOUD_OCI_DNS_RESOLVER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-41D2ADCF-62E4-4E9A-863E-0A26BB802D05)
- [DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-89BA3938-8524-4295-B3F0-DE81404ECD43)
- [DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-624D9F95-D36E-4E9B-8793-D2753AC1E212)
- [DBMS_CLOUD_OCI_DNS_UPDATE_RESOLVER_VNIC_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-963A40BD-31E5-40C2-88C3-069EBD148014)
- [DBMS_CLOUD_OCI_DNS_UPDATE_STEERING_POLICY_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-D1F5D25C-3704-4D5F-A8DE-27FE40833531)
- [DBMS_CLOUD_OCI_DNS_UPDATE_STEERING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-C818C374-A4C9-4802-80B2-1D6F13DFC311)
- [DBMS_CLOUD_OCI_DNS_UPDATE_TSIG_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-4FC79CFE-14CF-4E21-BD57-FD367C7FD1F6)
- [DBMS_CLOUD_OCI_DNS_UPDATE_VIEW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-01A7CBEB-333A-4225-816A-4ECE38314716)
- [DBMS_CLOUD_OCI_DNS_UPDATE_ZONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-DCD6AE99-E5F2-4C90-9B72-DE99ACF0BE4E)
- [DBMS_CLOUD_OCI_DNS_UPDATE_ZONE_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-88DF8810-8119-4361-8579-A575764B3CF1)
- [DBMS_CLOUD_OCI_DNS_VIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-92CEA67F-5A90-49A6-B874-95902441AF22)
- [DBMS_CLOUD_OCI_DNS_VIEW_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-B982F440-3F57-426E-9C8E-17F88440563F)
- [DBMS_CLOUD_OCI_DNS_ZONE_TRANSFER_SERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-06E911E9-86B9-4DAE-AAC7-13AA05327D77)
- [DBMS_CLOUD_OCI_DNS_NAMESERVER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-19F2AA15-D677-4596-899C-E65849CB11CE)
- [DBMS_CLOUD_OCI_DNS_ZONE_TRANSFER_SERVER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-A618703E-00C6-4C9B-8FF7-6939EF1E074D)
- [DBMS_CLOUD_OCI_DNS_ZONE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-A3E6D744-5115-4854-BB6A-EB993D7A6088)
- [DBMS_CLOUD_OCI_DNS_ZONE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dns_t.html#ADSDK-GUID-B7527F46-857E-46CD-87D5-0EB8AAEAEF3A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
