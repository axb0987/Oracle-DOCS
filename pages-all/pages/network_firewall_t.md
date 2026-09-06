# Network Firewall Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#dcoc-content-body)

## Network Firewall Common Types

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_T Type

List of addresses with a reference name. The value of an entry is a list of IP addresses or prefixes in CIDR notation or FQDNs. The associated key is the identifier by which the IP address list is referenced.

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name to identify the group of addresses to be used in the policy rules.

`l_type`

(required) Type of address List. The accepted values are - * FQDN * IP

Allowed values are: 'FQDN', 'IP'

`addresses`

(required) List of addresses.

`total_addresses`

(required) Count of total Addresses in the AddressList

`parent_resource_id`

(required) OCID of the Network Firewall Policy this Address List belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_T Type

Address List Summary in the network firewall policy

Syntax
```

```

Fields

Field Description

`name`

(required) Name of Address List

`l_type`

(required) Type of address List. The accepted values are - * FQDN * IP

Allowed values are: 'FQDN', 'IP'

`total_addresses`

(required) Count of total Addresses in the AddressList

`parent_resource_id`

(required) OCID of the Network Firewall Policy this address list belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_address_list_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_COLLECTION_T Type

Collection of Address Lists in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of address lists.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_T Type

A protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range).

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Application.

Allowed values are: 'ICMP', 'ICMP_V6'

`name`

(required) Name of the application.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_T Type

A group of applications.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the application Group.

`apps`

(required) List of apps in the group.

`total_apps`

(required) Count of total applications in the given application group.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application group belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_T Type

Summary object for application list in the network firewall policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the application groups.

`total_apps`

(required) Count of total applications in the given application group.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application group belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_application_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_COLLECTION_T Type

Collection of Application Lists in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) List of application lists.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_T Type

Summary object for application element in the network firewall policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Application.

Allowed values are: 'ICMP', 'ICMP_V6'

`name`

(required) Name of the application.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_COLLECTION_T Type

Collection of Applications in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Applications.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLY_NETWORK_FIREWALL_POLICY_DETAILS_T Type

Request data required to clone a network firewall policy.

Syntax
```

```

Fields

Field Description

`firewalls`

(optional) Ordered priority list of firewall OCIDs on which the update needs to be applied in given order. If the list is a subset of the firewalls attached, then given firewalls would be deployed first with the change, followed by remaining firewalls.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CHANGE_NETWORK_FIREWALL_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the Network Firewalll resource should be moved.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CHANGE_NETWORK_FIREWALL_POLICY_COMPARTMENT_DETAILS_T Type

The request details required to move the resource to target compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CLONE_NETWORK_FIREWALL_POLICY_DETAILS_T Type

Request data required to clone a network firewall policy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly optional name for the cloned firewall policy. Avoid entering confidential information.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the NetworkFirewall Policy.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ADDRESS_LIST_DETAILS_T Type

The Request for creating the address List

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name to identify the group of addresses to be used in the policy rules.

`l_type`

(required) Type of address List. The accepted values are - * FQDN * IP

Allowed values are: 'FQDN', 'IP'

`addresses`

(required) List of addresses.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_APPLICATION_DETAILS_T Type

Request for creating a application against a policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the application

`l_type`

(optional) Describes the type of Application.

Allowed values are: 'ICMP', 'ICMP_V6'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_APPLICATION_GROUP_DETAILS_T Type

Request for creating a application list in a policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the application Group.

`apps`

(required) Collection of application names.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_DECRYPTION_PROFILE_DETAILS_T Type

Request for Decryption Profile used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

`name`

(required) Name of the decryption profile.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_MATCH_CRITERIA_T Type

Match criteria used in Decryption Rule used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`source_address`

(optional) An array of IP address list names to be evaluated against the traffic source address.

`destination_address`

(optional) An array of IP address list names to be evaluated against the traffic destination address.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_RULE_POSITION_T Type

An object which defines the position of the rule.

Syntax
```

```

Fields

Field Description

`before_rule`

(optional) Identifier for rule before which this rule lies.

`after_rule`

(optional) Identifier for rule after which this rule lies.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_DECRYPTION_RULE_DETAILS_T Type

Request for creating Decryption Rule used in the firewall policy rules. A Decryption Rule is used to define which traffic should be decrypted by the firewall, and how it should do so.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the decryption rule, must be unique within the policy.

`condition`

(required)

`action`

(required) Action: * NO_DECRYPT - Matching traffic is not decrypted. * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`.

Allowed values are: 'NO_DECRYPT', 'DECRYPT'

`decryption_profile`

(optional) The name of the decryption profile to use.

`secret`

(optional) The name of a mapped secret. Its `type` must match that of the specified decryption profile.

`position`

(optional)

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ICMP6_APPLICATION_DETAILS_T Type

Request for ICMP6 Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_icmp6_application_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_application_details_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP6 message Type field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

`icmp_code`

(optional) The value of the ICMP6 message Code (subtype) field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ICMP_APPLICATION_DETAILS_T Type

Request for ICMP Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_icmp_application_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_application_details_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP message Type field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

`icmp_code`

(optional) The value of the ICMP message Code (subtype) field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_MAPPED_SECRET_DETAILS_T Type

The Request for creating the Mapped Secret

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name to identify the group of urls to be used in the policy rules.

`source`

(required) Source of the secrets, where the secrets are stored.

`l_type`

(required) Type of the secrets mapped based on the policy. * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic. * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_NETWORK_FIREWALL_DETAILS_T Type

The information about new Network Firewall.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Network Firewall.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the Network Firewall.

`availability_domain`

(optional) Availability Domain where Network Firewall instance is created. To get a list of availability domains for a tenancy, use`LIST_AVAILABILITY_DOMAINS`Function operation. Example: `kIdk:PHX-AD-1`

`network_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall Policy.

`ipv4_address`

(optional) IPv4 address for the Network Firewall.

`ipv6_address`

(optional) IPv6 address for the Network Firewall.

`network_security_group_ids`

(optional) An array of network security groups[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the Network Firewall.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_NETWORK_FIREWALL_POLICY_DETAILS_T Type

Request data required to create a network firewall policy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly optional name for the firewall policy. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the NetworkFirewall Policy.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_MATCH_CRITERIA_T Type

Criteria to evaluate against network traffic. A match occurs when at least one item in the array associated with each specified property corresponds with the relevant aspect of the traffic.

Syntax
```

```

Fields

Field Description

`source_address`

(optional) An array of IP address list names to be evaluated against the traffic source address.

`destination_address`

(optional) An array of IP address list names to be evaluated against the traffic destination address.

`application`

(optional) An array of application list names to be evaluated against the traffic protocol and protocol-specific parameters.

`service`

(optional) An array of service list names to be evaluated against the traffic protocol and protocol-specific parameters.

`url`

(optional) An array of URL pattern list names to be evaluated against the HTTP(S) request target.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SECURITY_RULE_DETAILS_T Type

Reqeust for creating Security Rule used in the firewall policy rules. Security Rules determine whether to block or allow a session based on traffic attributes, such as the source and destination IP address, protocol/port, and the HTTP(S) target URL.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the Security rule, must be unique within the policy.

`condition`

(required)

`action`

(required) Types of Action on the Traffic flow. * ALLOW - Allows the traffic. * DROP - Silently drops the traffic, e.g. without sending a TCP reset. * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable. * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

Allowed values are: 'ALLOW', 'DROP', 'REJECT', 'INSPECT'

`inspection`

(optional) Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT. * INTRUSION_DETECTION - Intrusion Detection. * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

Allowed values are: 'INTRUSION_DETECTION', 'INTRUSION_PREVENTION'

`position`

(optional)

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SERVICE_DETAILS_T Type

Request for creating a service against a policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the service

`l_type`

(optional) Describes the type of Service.

Allowed values are: 'TCP_SERVICE', 'UDP_SERVICE'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SERVICE_LIST_DETAILS_T Type

Request for creating a service list in a policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the service Group.

`services`

(required) Collection of service names.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SSL_FORWARD_PROXY_PROFILE_DETAILS_T Type

Request for creating SSLForwardProxy used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_ssl_forward_proxy_profile_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_decryption_profile_details_t`type.

Fields

Field Description

`is_expired_certificate_blocked`

(optional) Whether to block sessions if server's certificate is expired.

`is_untrusted_issuer_blocked`

(optional) Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).

`is_revocation_status_timeout_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate does not succeed within the maximum allowed time (defaulting to 5 seconds).

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_unknown_revocation_status_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate results in \"unknown\".

`are_certificate_extensions_restricted`

(optional) Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.

`is_auto_include_alt_name`

(optional) Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SSL_INBOUND_INSPECTION_PROFILE_DETAILS_T Type

Request for creating SSLInboundInspection used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_ssl_inbound_inspection_profile_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_decryption_profile_details_t`type.

Fields

Field Description

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_PORT_RANGE_T Type

A Port Range which can be used for the running service. It uses port information.

Syntax
```

```

Fields

Field Description

`minimum_port`

(required) The minimum port in the range (inclusive), or the sole port of a single-port range.

`maximum_port`

(optional) The maximum port in the range (inclusive), which may be absent for a single-port range.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_PORT_RANGE_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_port_range_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_TCP_SERVICE_DETAILS_T Type

Request for TCP Service used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_tcp_service_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_service_details_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_UDP_SERVICE_DETAILS_T Type

Request for UDP Service used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_udp_service_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_service_details_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_PATTERN_T Type

Pattern describing a URL or set of URLs.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of pattern. * SIMPLE - A simple pattern with optional subdomain and/or path suffix wildcards.

Allowed values are: 'SIMPLE'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_PATTERN_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_url_pattern_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_URL_LIST_DETAILS_T Type

The Request for creating the URL List

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name to identify the group of urls to be used in the policy rules.

`urls`

(required) List of urls.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_VAULT_MAPPED_SECRET_DETAILS_T Type

The request details to be created in the Vault Mapped Secret for the policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_create_vault_mapped_secret_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_create_mapped_secret_details_t`type.

Fields

Field Description

`vault_secret_id`

(required) OCID for the Vault Secret to be used.

`version_number`

(required) Version number of the secret to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_T Type

Decryption Profile used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

`name`

(required) Unique Name of the decryption profile.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this decryption profile belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_T Type

Decryption Profile used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the secret.

`l_type`

(required) Type of the secrets mapped based on the policy. * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic. * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

`parent_resource_id`

(required) OCID of the Network Firewall Policy this decryption profile belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_decryption_profile_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_COLLECTION_T Type

Collection of Decryption Profiles in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Decryption Profiles.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_T Type

Decryption Rule used in the firewall policy rules. A Decryption Rule is used to define which traffic should be decrypted by the firewall, and how it should do so.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the decryption rule, must be unique within the policy.

`condition`

(required)

`action`

(required) Action: * NO_DECRYPT - Matching traffic is not decrypted. * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`.

Allowed values are: 'NO_DECRYPT', 'DECRYPT'

`decryption_profile`

(optional) The name of the decryption profile to use.

`secret`

(optional) The name of a mapped secret. Its `type` must match that of the specified decryption profile.

`position`

(optional)

`parent_resource_id`

(required) OCID of the Network Firewall Policy this decryption rule belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_T Type

Summary for Decryption Rule used in the firewall policy rules. A Decryption Rule is used to define which traffic should be decrypted by the firewall, and how it should do so.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the decryption rule, must be unique within the policy.

`action`

(required) Action: * NO_DECRYPT - Matching traffic is not decrypted. * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`.

Allowed values are: 'NO_DECRYPT', 'DECRYPT'

`decryption_profile`

(required) The name of the decryption profile to use.

`secret`

(required) The name of a mapped secret. Its `type` must match that of the specified decryption profile.

`priority_order`

(required) The priority order in which this rule should be evaluated.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_decryption_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_COLLECTION_T Type

Collection of Decryption Rule Summaries in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Decryption Rule Summaries.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ERROR_T Type

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

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP6_APPLICATION_T Type

ICMP6 Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_icmp6_application_t`is a subtype of the`dbms_cloud_oci_network_firewall_application_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP6 message Type field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

`icmp_code`

(optional) The value of the ICMP6 message Code (subtype) field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP6_APPLICATION_SUMMARY_T Type

Summary object for ICMP V6 application element in the network firewall policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_icmp6_application_summary_t`is a subtype of the`dbms_cloud_oci_network_firewall_application_summary_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP message Type field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

`icmp_code`

(optional) The value of the ICMP message Code (subtype) field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP_APPLICATION_T Type

ICMP Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_icmp_application_t`is a subtype of the`dbms_cloud_oci_network_firewall_application_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP message Type field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

`icmp_code`

(optional) The value of the ICMP message Code (subtype) field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP_APPLICATION_SUMMARY_T Type

Summary object for ICMP application element in the network firewall policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_icmp_application_summary_t`is a subtype of the`dbms_cloud_oci_network_firewall_application_summary_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP message Type field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

`icmp_code`

(optional) The value of the ICMP message Code (subtype) field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_T Type

Mapped secret used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the secret.

`source`

(required) Source of the secrets, where the secrets are stored.

Allowed values are: 'OCI_VAULT'

`l_type`

(required) Type of the secrets mapped based on the policy. * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic. * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

`parent_resource_id`

(required) OCID of the Network Firewall Policy this Mapped Secret belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_T Type

Mapped secret used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the secret.

`source`

(required) Source of the secrets, where the secrets are stored.

`l_type`

(required) Type of the secrets mapped based on the policy. * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic. * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

`parent_resource_id`

(required) OCID of the Network Firewall Policy this mapped secret belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_mapped_secret_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_COLLECTION_T Type

Collection of Mapped Secrets in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Mapped Secrets.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_T Type

A network firewall is a security resource that exists in a subnet of your choice and controls incoming and outgoing network traffic based on a set of security rules. Each firewall is associated with a policy. Traffic is routed to and from the firewall from resources such as internet gateways and dynamic routing gateways (DRGs). For more information, see[Overview of Network Firewall](https://docs.oracle.com/iaas/Content/network-firewall/overview.htm)

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Network Firewall.

`display_name`

(required) A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the Network Firewall.

`ipv4_address`

(optional) IPv4 address for the Network Firewall.

`ipv6_address`

(optional) IPv6 address for the Network Firewall.

`network_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall Policy.

`availability_domain`

(optional) Availability Domain where Network Firewall instance is created. To get a list of availability domains for a tenancy, use the`LIST_AVAILABILITY_DOMAINS`Function operation. Example: `kIdk:PHX-AD-1`

`network_security_group_ids`

(optional) An array of network security groups[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the Network Firewall.

`time_created`

(required) The time at which the Network Firewall was created in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The time at which the Network Firewall was updated in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the Network Firewall.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'FAILED' state.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_SUMMARY_T Type

Summary of the Network Firewall.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Network Firewall.

`display_name`

(required) A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the Network Firewall.

`availability_domain`

(optional) Availability Domain where Network Firewall instance is created. To get a list of availability domains for a tenancy, use`LIST_AVAILABILITY_DOMAINS`Function operation. Example: `kIdk:PHX-AD-1`

`ipv4_address`

(optional) IPv4 address for the Network Firewall.

`ipv6_address`

(optional) IPv6 address for the Network Firewall.

`network_firewall_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall Policy.

`time_created`

(required) The time instant at which the Network Firewall was created in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The time instant at which the Network Firewall was updated in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the Network Firewall.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_network_firewall_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_COLLECTION_T Type

A collection of NetworkFirewallSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of network firewalls.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_T Type

Description of NetworkFirewall Policy.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource - Network Firewall Policy.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the NetworkFirewall Policy.

`display_name`

(required) A user-friendly optional name for the firewall policy. Avoid entering confidential information.

`time_created`

(required) The time instant at which the Network Firewall Policy was created in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The time instant at which the Network Firewall Policy was updated in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the Network Firewall Policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`attached_network_firewall_count`

(optional) Count of number of Network Firewall attached to the Policy.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_T Type

Summary of the NetworkFirewall Policy.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource - Network Firewall Policy.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the NetworkFirewall Policy.

`display_name`

(required) A user-friendly optional name for the firewall policy. Avoid entering confidential information.

`time_created`

(required) The time instant at which the Network Firewall Policy was created in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The time instant at which the Network Firewall Policy was updated in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current lifecycle state of the Network Firewall Policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'ATTACHING', 'DETACHING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_network_firewall_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_COLLECTION_T Type

Collection of Network Firewall Policies.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of network Firewall Policies.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_T Type

Security Rule used in the firewall policy rules. Security Rules determine whether to block or allow a session based on traffic attributes, such as the source and destination IP address, protocol/port, and the HTTP(S) target URL.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the Security rule, must be unique within the policy.

`condition`

(required)

`action`

(required) Types of Action on the Traffic flow. * ALLOW - Allows the traffic. * DROP - Silently drops the traffic, e.g. without sending a TCP reset. * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable. * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

Allowed values are: 'ALLOW', 'DROP', 'REJECT', 'INSPECT'

`inspection`

(optional) Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT. * INTRUSION_DETECTION - Intrusion Detection. * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

Allowed values are: 'INTRUSION_DETECTION', 'INTRUSION_PREVENTION'

`position`

(optional)

`parent_resource_id`

(required) OCID of the Network Firewall Policy this security rule belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_T Type

Summary for the Security Rule used in the firewall policy rules. Security Rules determine whether to block or allow a session based on traffic attributes, such as the source and destination IP address, protocol/port, and the HTTP(S) target URL.

Syntax
```

```

Fields

Field Description

`name`

(required) Name for the Security rule, must be unique within the policy.

`action`

(required) Types of Action on the Traffic flow. * ALLOW - Allows the traffic. * DROP - Silently drops the traffic, e.g. without sending a TCP reset. * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable. * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

Allowed values are: 'ALLOW', 'DROP', 'REJECT', 'INSPECT'

`inspection`

(optional) Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT. * INTRUSION_DETECTION - Intrusion Detection. * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

Allowed values are: 'INTRUSION_DETECTION', 'INTRUSION_PREVENTION'

`priority_order`

(required) The priority order in which this rule should be evaluated.

`parent_resource_id`

(required) OCID of the network firewall policy this security rule belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_security_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_COLLECTION_T Type

Collection of Security Rule Summaries in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Security Rule Summaries.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_T Type

A Service which can be used to identify the running service. It uses port &amp; protocol information.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Service.

Allowed values are: 'TCP_SERVICE', 'UDP_SERVICE'

`name`

(required) Name of the service.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this service belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_T Type

A group of services.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the service Group.

`services`

(required) List of services in the group.

`total_services`

(required) Count of total services in the given service List.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this serviceList belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_T Type

Summary object for service list in the network firewall policy.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the service groups.

`total_services`

(required) Count of total services in the given service List.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this application belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_service_list_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_COLLECTION_T Type

Collection of Service Lists in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) List of service lists.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_T Type

Summary object for service element in the network firewall policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Service.

Allowed values are: 'TCP_SERVICE', 'UDP_SERVICE'

`name`

(required) Name of the service.

`parent_resource_id`

(required) OCID of the Network Firewall Policy this Service belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_COLLECTION_T Type

Collection of Services in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of Services.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SIMPLE_URL_PATTERN_T Type

Pattern describing an http/https URL or set thereof as a concatenation of optional host component and optional path component. `*.example.com` will match http://example.com/ and https://foo.example.com/foo?bar. `www.example.com/foo*` will match https://www.example.com/foo and http://www.exampe.com/foobar and https://www.example.com/foo/bar?baz, but not http://sub.www.example.com/foo or https://www.example.com/FOO. `*.example.com/foo*` will match http://example.com/foo and https://sub2.sub.example.com/foo/bar?baz, but not http://example.com/FOO.

Syntax
```

```

`dbms_cloud_oci_network_firewall_simple_url_pattern_t`is a subtype of the`dbms_cloud_oci_network_firewall_url_pattern_t`type.

Fields

Field Description

`pattern`

(required) A string consisting of a concatenation of optional host component and optional path component. The host component may start with `*.` to match the case-insensitive domain and all its subdomains. The path component must start with a `/`, and may end with `*` to match all paths of which it is a case-sensitive prefix. A missing host component matches all request domains, and a missing path component matches all request paths. An empty value matches all requests.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SSL_FORWARD_PROXY_PROFILE_T Type

SSLForwardProxy used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_ssl_forward_proxy_profile_t`is a subtype of the`dbms_cloud_oci_network_firewall_decryption_profile_t`type.

Fields

Field Description

`is_expired_certificate_blocked`

(optional) Whether to block sessions if server's certificate is expired.

`is_untrusted_issuer_blocked`

(optional) Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).

`is_revocation_status_timeout_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate does not succeed within the maximum allowed time (defaulting to 5 seconds).

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_unknown_revocation_status_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate results in \"unknown\".

`are_certificate_extensions_restricted`

(optional) Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.

`is_auto_include_alt_name`

(optional) Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_SSL_INBOUND_INSPECTION_PROFILE_T Type

SSLInboundInspection used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_ssl_inbound_inspection_profile_t`is a subtype of the`dbms_cloud_oci_network_firewall_decryption_profile_t`type.

Fields

Field Description

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_TCP_SERVICE_T Type

TCP Service used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_tcp_service_t`is a subtype of the`dbms_cloud_oci_network_firewall_service_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UDP_SERVICE_T Type

UDP Service used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_udp_service_t`is a subtype of the`dbms_cloud_oci_network_firewall_service_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ADDRESS_LIST_DETAILS_T Type

The request details to be updated in the address List for the policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of address List. The accepted values are - * FQDN * IP

Allowed values are: 'FQDN', 'IP'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_APPLICATION_DETAILS_T Type

Request for updating an existing application in context to the network firewall policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Application.

Allowed values are: 'ICMP', 'ICMP_V6'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_APPLICATION_GROUP_DETAILS_T Type

Request for updating an existing application in context to the network firewall policy.

Syntax
```

```

Fields

Field Description

`apps`

(required) Collection of application names.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_DECRYPTION_PROFILE_DETAILS_T Type

Update Request for Decryption Profile used on the firewall policy rules.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_DECRYPTION_RULE_DETAILS_T Type

Request for updating Decryption Rule used in the firewall policy rules. A Decryption Rule is used to define which traffic should be decrypted by the firewall, and how it should do so.

Syntax
```

```

Fields

Field Description

`condition`

(required)

`action`

(required) Action: * NO_DECRYPT - Matching traffic is not decrypted. * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`.

Allowed values are: 'NO_DECRYPT', 'DECRYPT'

`decryption_profile`

(optional) The name of the decryption profile to use.

`secret`

(optional) The name of a mapped secret. Its `type` must match that of the specified decryption profile.

`position`

(optional)

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_FQDN_ADDRESS_LIST_DETAILS_T Type

The request details to be updated in the address List for the policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_fqdn_address_list_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_address_list_details_t`type.

Fields

Field Description

`addresses`

(required) List of FQDN addresses.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ICMP6_APPLICATION_DETAILS_T Type

Request for updating ICMP6 Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_icmp6_application_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_application_details_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP6 message Type field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

`icmp_code`

(optional) The value of the ICMP6 message Code (subtype) field as defined by[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443.html#section-2.1).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ICMP_APPLICATION_DETAILS_T Type

Request for updating ICMP Application used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_icmp_application_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_application_details_t`type.

Fields

Field Description

`icmp_type`

(required) The value of the ICMP message Type field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

`icmp_code`

(optional) The value of the ICMP message Code (subtype) field as defined by[RFC 792](https://www.rfc-editor.org/rfc/rfc792.html).

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_IP_ADDRESS_LIST_DETAILS_T Type

The request details to be updated in the address List for the policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_ip_address_list_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_address_list_details_t`type.

Fields

Field Description

`addresses`

(required) List of IP addresses which could be IPv4 or IPv6 addresses or CIDR blocks.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_MAPPED_SECRET_DETAILS_T Type

The request details to be updated in the Mapped Secret for the policy.

Syntax
```

```

Fields

Field Description

`source`

(required) Source of the secrets, where the secrets are stored.

`l_type`

(required) Type of the secrets mapped based on the policy. * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic. * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

Allowed values are: 'SSL_INBOUND_INSPECTION', 'SSL_FORWARD_PROXY'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_NETWORK_FIREWALL_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`network_firewall_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Network Firewall Policy.

`network_security_group_ids`

(optional) An array of network security groups[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the Network Firewall.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_NETWORK_FIREWALL_POLICY_DETAILS_T Type

The request details to be updated in the firewall policy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SECURITY_RULE_DETAILS_T Type

Update Request for Security Rule used in the firewall policy rules. Security Rules determine whether to block or allow a session based on traffic attributes, such as the source and destination IP address, protocol/port, and the HTTP(S) target URL.

Syntax
```

```

Fields

Field Description

`condition`

(required)

`action`

(required) Types of Action on the Traffic flow. * ALLOW - Allows the traffic. * DROP - Silently drops the traffic, e.g. without sending a TCP reset. * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable. * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

Allowed values are: 'ALLOW', 'DROP', 'REJECT', 'INSPECT'

`inspection`

(optional) Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT. * INTRUSION_DETECTION - Intrusion Detection. * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

Allowed values are: 'INTRUSION_DETECTION', 'INTRUSION_PREVENTION'

`position`

(optional)

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SERVICE_DETAILS_T Type

Request for updating an existing service in context to the network firewall policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Describes the type of Service.

Allowed values are: 'TCP_SERVICE', 'UDP_SERVICE'

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SERVICE_LIST_DETAILS_T Type

Request for updating an existing service in context to the network firewall policy.

Syntax
```

```

Fields

Field Description

`services`

(required) Collection of service names.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SSL_FORWARD_PROXY_PROFILE_DETAILS_T Type

Update Request for SSLForwardProxy used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_ssl_forward_proxy_profile_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_decryption_profile_details_t`type.

Fields

Field Description

`is_expired_certificate_blocked`

(optional) Whether to block sessions if server's certificate is expired.

`is_untrusted_issuer_blocked`

(optional) Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).

`is_revocation_status_timeout_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate does not succeed within the maximum allowed time (defaulting to 5 seconds).

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_unknown_revocation_status_blocked`

(optional) Whether to block sessions if the revocation status check for server's certificate results in \"unknown\".

`are_certificate_extensions_restricted`

(optional) Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.

`is_auto_include_alt_name`

(optional) Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SSL_INBOUND_INSPECTION_PROFILE_DETAILS_T Type

Update Request for SSLInboundInspection used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_ssl_inbound_inspection_profile_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_decryption_profile_details_t`type.

Fields

Field Description

`is_unsupported_version_blocked`

(optional) Whether to block sessions if SSL version is not supported.

`is_unsupported_cipher_blocked`

(optional) Whether to block sessions if SSL cipher suite is not supported.

`is_out_of_capacity_blocked`

(optional) Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_TCP_SERVICE_DETAILS_T Type

Request for updating TCP Service.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_tcp_service_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_service_details_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_UDP_SERVICE_DETAILS_T Type

Request for updating UDP Service used on the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_udp_service_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_service_details_t`type.

Fields

Field Description

`port_ranges`

(required) List of port-ranges to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_URL_LIST_DETAILS_T Type

The request details to be updated in the URL List for the policy.

Syntax
```

```

Fields

Field Description

`urls`

(required) List of urls.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_VAULT_MAPPED_SECRET_DETAILS_T Type

The request details to be updated in the Vault Mapped Secret for the policy.

Syntax
```

```

`dbms_cloud_oci_network_firewall_update_vault_mapped_secret_details_t`is a subtype of the`dbms_cloud_oci_network_firewall_update_mapped_secret_details_t`type.

Fields

Field Description

`vault_secret_id`

(required) OCID for the Vault Secret to be used.

`version_number`

(required) Version number of the secret to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_T Type

URL pattern lists of the policy. The value of an entry is a list of URL patterns. The associated key/name is the identifier by which the URL pattern list is referenced.

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name identifier for the URL list.

`urls`

(required) List of urls.

`total_urls`

(required) Total count of URLs in the URL List

`parent_resource_id`

(required) OCID of the Network Firewall Policy this URL List belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_T Type

URL List Summary in the network firewall policy

Syntax
```

```

Fields

Field Description

`name`

(required) Name of URL List

`total_urls`

(required) Total count of URLs in the URL List

`parent_resource_id`

(required) OCID of the Network Firewall Policy this mapped secret belongs to.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_url_list_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_COLLECTION_T Type

Collection of URL Lists in the network firewall policy

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of url lists.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_VAULT_MAPPED_SECRET_T Type

Mapped secret stored in OCI vault used in the firewall policy rules.

Syntax
```

```

`dbms_cloud_oci_network_firewall_vault_mapped_secret_t`is a subtype of the`dbms_cloud_oci_network_firewall_mapped_secret_t`type.

Fields

Field Description

`vault_secret_id`

(required) OCID for the Vault Secret to be used.

`version_number`

(required) Version number of the secret to be used.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_NETWORK_FIREWALL', 'UPDATE_NETWORK_FIREWALL', 'DELETE_NETWORK_FIREWALL', 'MOVE_NETWORK_FIREWALL', 'CREATE_NETWORK_FIREWALL_POLICY', 'UPDATE_NETWORK_FIREWALL_POLICY', 'DELETE_NETWORK_FIREWALL_POLICY', 'MOVE_NETWORK_FIREWALL_POLICY'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_NETWORK_FIREWALL', 'UPDATE_NETWORK_FIREWALL', 'DELETE_NETWORK_FIREWALL', 'MOVE_NETWORK_FIREWALL', 'CREATE_NETWORK_FIREWALL_POLICY', 'UPDATE_NETWORK_FIREWALL_POLICY', 'DELETE_NETWORK_FIREWALL_POLICY', 'MOVE_NETWORK_FIREWALL_POLICY'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_firewall_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Network Firewall Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-DA72339C-306D-4F1D-A4B6-2A22372AF482)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-00AE16F5-FCA0-4474-B158-EE2EA9DBE72C)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9235C281-6807-4867-803F-07975255E9EA)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-1E027058-1DB8-4B68-A05B-E3D045744D7D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-DBC70C83-7B56-4AD7-AB20-BE8839EE5DCA)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ADDRESS_LIST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-AA249306-576A-44D7-A2FA-ADCEC106490F)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-2BFE7615-5E16-4BCF-AF83-F42A909A1650)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-427C805C-2377-4367-B6C2-E4F1EC69E90E)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-CC40D90C-B5E3-4607-AB04-40B8465EE3B2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0999AFDE-97D3-4105-A522-3F084BFB74C1)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_GROUP_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5D2068FC-3A47-4DB6-85D3-9A1CBE86343D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-005A3BF5-F306-4027-928C-821AB5AB6501)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A5F1E927-B092-4AF3-8E36-376EB61D70B3)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLICATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-76C0DE2D-8EA0-48F4-92A5-D0B1EA0C2E44)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_APPLY_NETWORK_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C3191978-060F-4889-BA2E-8EAE2CA50643)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CHANGE_NETWORK_FIREWALL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5689780C-95F4-4E67-AAD4-1F5A6C0405F0)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CHANGE_NETWORK_FIREWALL_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A9C2306C-845C-4D7D-B7D6-DEEF242B67CF)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CLONE_NETWORK_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8BB6ABD6-609F-4680-A214-763E1F72B56B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5D2AF37D-D126-4DF0-A8BE-9BAE568DC325)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-22540ADD-2DF4-4CF5-8BDA-5B1A758C20A2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_APPLICATION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-43E06BFA-CE32-4A2A-A3F0-634B5A241AF4)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_DECRYPTION_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5FB585A7-9D94-4416-BDC0-A706A35F91D1)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-CCE7E622-5476-4FD8-895A-E0779AD62959)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_RULE_POSITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-1EE6B5B6-0E16-48BA-839C-D26C2866B99D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_DECRYPTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C90B4EE9-C186-4F88-8FD7-84AC593A8B4D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ICMP6_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-23898521-2AE8-4E76-8555-4DC944C3B2F2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_ICMP_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-4D17E931-A792-438B-9F6D-BB38CE94D3A9)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_MAPPED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-ADDC1BCD-289D-4BE5-B7A7-C830F59B84BD)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_NETWORK_FIREWALL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-D0A1C02C-9A18-413D-90D7-FD911845657C)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_NETWORK_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0148B9A9-4F48-45AD-A061-2E0F90A77D0B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0D1185CD-81DD-4020-85F3-8FADA1985669)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-6B9F076B-3B95-48A0-9B65-6F2E6DD71A7F)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5777D64D-0BA2-4028-A17E-693929194E8E)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SERVICE_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-151E5679-5853-4AF0-AFE5-34469083AA18)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SSL_FORWARD_PROXY_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-239B135C-27D4-4910-A753-A90A920254EE)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_SSL_INBOUND_INSPECTION_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-50D6041B-739C-4FE8-841C-F3E9CE8E7538)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_PORT_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A5ADDD4D-28A2-470A-8EB9-A3CDED270476)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_PORT_RANGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-EC501D27-085E-4A79-B7FF-2322FBD28993)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_TCP_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-562D14F5-87C8-4A54-BB8A-BCF43F4EE07D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_UDP_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-1C8E4D84-E891-4A8C-B8A0-4DBE5058EF21)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_PATTERN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-01ABC8E8-83B2-45B8-B07F-CD73DC822E84)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_PATTERN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-6C3083F1-18F8-41F2-BA59-F8E07CFDE491)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_URL_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B5686244-EAE3-4AE4-9A02-1EB8A981BF54)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_CREATE_VAULT_MAPPED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-CEB1DD26-BA6F-4942-B39D-4958E42A5CBD)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-94C9FF20-3855-4D4F-8FA0-8B320801FD90)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-D7106128-E84B-4F0C-ADEB-8B22E4ADAAB0)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9736A38E-71D0-49E6-8F31-2421E4F7BF58)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_PROFILE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A490874D-D76D-4BC4-8348-80FDC96030D5)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-39C07AB6-0F1E-49EB-B5F9-0924994E3BF6)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-7FC58D72-D806-4B0B-9C9B-BCB8D37C9106)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-98AEDCCA-7C56-465F-BED7-367F6A8F97CE)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_DECRYPTION_RULE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-DBEE56F9-6B21-4F16-8088-38575ECD4D79)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9FC8CA81-6A70-4003-A0AB-AE4B4F6BD530)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP6_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0ED19A34-06D2-4755-A2C9-BAA1156A4C2F)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP6_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-3510CB04-8ED1-4DFD-9B37-4703B0142041)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9A143793-8E90-4D26-BB8B-C8D518464DD6)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_ICMP_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-625A14EF-28FE-4757-B4A3-037D5336E4B4)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-D3776924-BB7E-4079-9088-F57E67AEF126)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-DDD3610A-67E5-44E0-ACA5-485BE6F64FF1)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-D72C6E84-AEA3-47FB-B7D9-86CF4CBA14FB)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_MAPPED_SECRET_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-098B0ED8-5CAA-4A53-A060-584336DEF2E5)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B51A79B5-CB3F-428A-8FEE-9093A60BAA93)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-4A41E62B-2D53-489F-B7CD-6210719BF224)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9B06EAC5-99ED-4A96-B44A-63BFFF512A42)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-67520765-4E4A-472B-959F-8024F02DBB1B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C15BC73B-58BC-4DE6-98A6-168178737A47)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C977C81F-F27C-4559-9570-018CB66C490B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-338F89E7-250F-45E2-BDAE-9A43AA944E22)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_NETWORK_FIREWALL_POLICY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-AB074596-B806-4627-AD0A-69CBF797D073)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-91241932-104F-45A6-8152-F0E8C735A6BE)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-2C897509-EF89-4CAE-B7FB-CADABE462E59)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C62887F6-A5C5-4E32-BB14-2B19247F3B74)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SECURITY_RULE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-EF9AD732-CC3C-45BF-AFDC-A284B3DAAC6B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-1FDEB458-F839-4B2A-97D5-9860BAF73EE3)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9458F0F3-3A44-4136-8C34-D83ECBED78BB)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8088C713-1868-4141-895C-A7B7CC96EB78)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-7B15544D-2652-4717-B586-00656D5EA13D)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_LIST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-FDBA598E-E77C-4B8B-BB12-742154720F4F)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-84D6459D-4283-4FE4-93FF-48B1B4369BE3)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-767D410D-AFF2-4C09-A68D-BB01EFA7A362)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SERVICE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-26B4964D-8AE5-4120-B3D0-6364C5BDF4AA)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SIMPLE_URL_PATTERN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-75446865-8992-47E7-AFE6-A90F7FB474B7)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SSL_FORWARD_PROXY_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-633B3D9E-61B4-40B2-8CE4-5FB29828A35F)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_SSL_INBOUND_INSPECTION_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B468AB9C-53B7-4CBD-858C-BE23F9F5A5BA)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_TCP_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8B34B72A-B11D-4ADE-BCE1-92BAF7DC5554)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UDP_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-811632C5-3EF6-46AA-88CB-0DF3AC825409)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A5B51DA9-6BF2-4D99-9DED-3E902386B2D0)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-E035FEA6-C9D3-436E-8261-E510538C12CC)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_APPLICATION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-E7FE4DA4-22C6-426B-9A36-6D482E81C634)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_DECRYPTION_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-6DB310D1-DDC5-4629-B58F-E055D4FD47EF)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_DECRYPTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-2CDA84F0-F0A0-40EB-8E9D-F9041C9A96B6)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_FQDN_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-82F91431-4DFE-4113-BA39-B7B298B981A2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ICMP6_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-10FD29FF-68D4-42F8-BA8D-1D0AB9B34C29)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_ICMP_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-30094133-634D-4D97-80FB-F68E1DFF4428)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_IP_ADDRESS_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-6E696D5D-17B8-4A24-B16B-A3AAE6B718BE)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_MAPPED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-38DF0117-3937-4474-BEAA-4E094A23F1D2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_NETWORK_FIREWALL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C59F0D78-04CC-477C-AAAF-A710D928E515)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_NETWORK_FIREWALL_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-5AE0646C-C856-4FB7-97C7-244E2E47509B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-90E4E30F-74DB-41DF-9F5B-B18C43B16517)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B5F8E756-0A3C-4593-BA99-6EF78239A843)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SERVICE_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8809ADC7-B770-4EB4-8AD6-EC742D647CDA)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SSL_FORWARD_PROXY_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A3352DB7-5051-4353-8890-D8C861E4096B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_SSL_INBOUND_INSPECTION_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-EDB21CDB-D3A0-429E-A10C-91AAC1712B34)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_TCP_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-EE126610-6265-45C5-8A59-B271CACD0C2C)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_UDP_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-6BE4A606-1B66-4746-8F44-8B4177F5DBDD)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_URL_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B24DF501-1D55-40DB-8D95-2DDDF53C1BE2)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_UPDATE_VAULT_MAPPED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-985157A7-098B-4BFA-A505-FC2A6ED91113)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-74F7A6AF-31DD-4409-9D76-56469F78A532)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-CDC657A8-7F6E-4194-852B-B5C0ACE7C372)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0E7939A1-74DA-4AF1-8F72-9B747E83F0CB)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_URL_LIST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8D9FAA13-3E33-405E-9FDD-DD9596A9A0B0)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_VAULT_MAPPED_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A7C075AE-9345-47DA-9BC9-7A2E79BAB2B3)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-B4FA48C8-58F7-48F2-9D4E-26E8193BEAEB)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-AD866F72-97B5-4803-997D-576269A545AD)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-C8D1E442-C340-446A-A077-3925C01FD106)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-DBCABD0E-A8AE-4CF6-B19C-4D583AECD783)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-9FFD7187-89F6-4975-8445-5A4A27FD7502)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-0C64C650-84C5-42F2-B99E-DC47B173FE94)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-A89D6BBD-096B-4E0D-8FCC-284C5B1D83F4)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-8C1E94C2-7D82-4BF0-96E3-564D05C6D517)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-D51FFCE9-3FB9-46C9-9ECC-C8CF95AE0166)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-1986F7C1-8756-4381-9A6C-EBCB9832AACE)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-BA042D16-10BB-4EAD-8D30-198C28D2B98B)
- [DBMS_CLOUD_OCI_NETWORK_FIREWALL_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_firewall_t.html#ADSDK-GUID-899D50C3-C629-42ED-BDF0-40584C2F5B7B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
