# VN Monitoring Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#dcoc-content-body)

## VN Monitoring Common Types

### DBMS_CLOUD_OCI_VN_MONITORING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_PROTOCOL_PARAMETERS_T Type

Defines the traffic protocol parameters for the traffic in a `PathAnalysisResult`.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the `TrafficProtocolParameters` object.

Allowed values are: 'TCP', 'UDP', 'ICMP'

### DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_TRAFFIC_SPEC_T Type

Defines the traffic configuration that leaves the traffic node.

Syntax
```

```

Fields

Field Description

`protocol`

(required) The IP protocol to use for the traffic path analysis.

`source_address`

(required) The IPv4 address of the source node.

`destination_address`

(required) The IPv4 address of the destination node.

`traffic_protocol_parameters`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ROUTING_ACTION_T Type

Defines the details for routing actions taken on the traffic flow.

Syntax
```

```

Fields

Field Description

`action`

(required) The routing action taken on the traffic flow.

Allowed values are: 'FORWARDED', 'NO_ROUTE', 'INDETERMINATE'

`action_type`

(required) The type of the routing support for the traffic flow.

Allowed values are: 'EXPLICIT', 'IMPLICIT', 'NOT_SUPPORTED'

### DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_ACTION_T Type

Defines the security action details taken on the traffic.

Syntax
```

```

Fields

Field Description

`action`

(required) Action taken on the traffic.

Allowed values are: 'ALLOWED', 'DENIED'

`action_type`

(required) Type of the `SecurityAction`.

Allowed values are: 'EXPLICIT', 'IMPLICIT'

### DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_NODE_T Type

Defines the configuration of the OCI entity that represents a traffic node in `PathAnalysisResult`.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the `TrafficNode`.

Allowed values are: 'VISIBLE', 'ACCESS_DENIED'

`egress_traffic`

(optional)

`next_hop_routing_action`

(optional)

`egress_security_action`

(optional)

`ingress_security_action`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ACCESS_DENIED_TRAFFIC_NODE_T Type

Defines the configuration of a traffic node to which the user is denied access.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_access_denied_traffic_node_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_traffic_node_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The match criteria in a route distribution statement. The match criteria outlines which routes should be imported or exported.

Syntax
```

```

Fields

Field Description

`match_type`

(required) The type of the match criteria for a route distribution statement.

Allowed values are: 'DRG_ATTACHMENT_TYPE', 'DRG_ATTACHMENT_ID', 'MATCH_ALL'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_drg_route_distribution_match_criteria_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type

Details used to add a route distribution statement.

Syntax
```

```

Fields

Field Description

`match_criteria`

(required) The action is applied only if all of the match criteria is met.

`action`

(required) Accept: import/export the route \"as is\"

Allowed values are: 'ACCEPT'

`priority`

(required) This field is used to specify the priority of each statement in a route distribution. The priority will be represented as a number between 0 and 65535 where a lower number indicates a higher priority. When a route is processed, statements are applied in the order defined by their priority. The first matching rule dictates the action that will be taken on the route.

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_add_drg_route_distribution_statement_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to add statements to a route distribution.

Syntax
```

```

Fields

Field Description

`statements`

(required) The collection of route distribution statements to insert into the route distribution.

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULE_DETAILS_T Type

Details needed when adding a DRG route rule.

Syntax
```

```

Fields

Field Description

`destination_type`

(required) Type of destination for the rule. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

Allowed values are: 'CIDR_BLOCK'

`destination`

(required) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed. Potential values: * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.

`next_hop_drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_add_drg_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULES_DETAILS_T Type

Details used in a request to add static routes to a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rules`

(optional) The collection of static rules used to insert routes into the DRG route table.

### DBMS_CLOUD_OCI_VN_MONITORING_ICMP_OPTIONS_T Type

Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code as defined in: -[ICMP Parameters](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)-[ICMPv6 Parameters](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\"Destination Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify multiple codes for a single type, create a separate security list rule for each.

Syntax
```

```

Fields

Field Description

`code`

(optional) The ICMP code (optional).

`l_type`

(required) The ICMP type.

### DBMS_CLOUD_OCI_VN_MONITORING_PORT_RANGE_T Type

Syntax
```

```

Fields

Field Description

`l_max`

(required) The maximum port number, which must not be less than the minimum port number. To specify a single port number, set both the min and max to the same value.

`l_min`

(required) The minimum port number, which must not be greater than the maximum port number.

### DBMS_CLOUD_OCI_VN_MONITORING_TCP_OPTIONS_T Type

Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.

Syntax
```

```

Fields

Field Description

`destination_port_range`

(optional)

`source_port_range`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_UDP_OPTIONS_T Type

Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.

Syntax
```

```

Fields

Field Description

`destination_port_range`

(optional)

`source_port_range`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_SECURITY_RULE_DETAILS_T Type

A rule for allowing inbound (INGRESS) or outbound (EGRESS) IP packets.

Syntax
```

```

Fields

Field Description

`description`

(optional) An optional description of your choice for the rule. Avoid entering confidential information.

`destination`

(optional) Conceptually, this is the range of IP addresses that a packet originating from the instance can go to. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`destination_type`

(optional) Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`direction`

(required) Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

Allowed values are: 'EGRESS', 'INGRESS'

`icmp_options`

(optional)

`is_stateless`

(optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`protocol`

(required) The transport protocol. Specify either `all` or an IPv4 protocol number as defined in[Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

`source`

(optional) Conceptually, this is the range of IP addresses that a packet coming into the instance can come from. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`source_type`

(optional) Type of source for the rule. Required if `direction` = `INGRESS`. * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic coming from a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`tcp_options`

(optional)

`udp_options`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_SECURITY_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_add_security_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules to add.

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type

The information used to add capacity to an IP pool.

Syntax
```

```

Fields

Field Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource to which the CIDR block belongs.

`cidr_block`

(required) The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange. Example: `10.0.1.0/24`

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_SUBNET_IPV6_CIDR_DETAILS_T Type

Details used when adding an IPv6 CIDR block to a subnet.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(required) This field is not required and should only be specified when adding an IPv6 CIDR to a subnet's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/64`

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_VCN_CIDR_DETAILS_T Type

Details used to add a CIDR block to a VCN.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to add.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIPV6_CIDR_DETAILS_T Type

The list of one or more BYOIPv6 CIDR blocks for the VCN that meets the following criteria: - The CIDR must from a BYOIPv6 range. - The IPv6 CIDR blocks must be valid. - Multiple CIDR blocks must not overlap each other or the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of IPv6 CIDR blocks allowed to a VCN.

Syntax
```

```

Fields

Field Description

`byoipv6_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource to which the CIDR block belongs.

`ipv6_cidr_block`

(required) An IPv6 CIDR block required to create a VCN with a BYOIP prefix. It could be the whole CIDR block identified in `byoipv6RangeId`, or a subrange. Example: `2001:0db8:0123::/48`

### DBMS_CLOUD_OCI_VN_MONITORING_ADD_VCN_IPV6_CIDR_DETAILS_T Type

Details used when adding a ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or a BYOIPv6 prefix. You can add only one of these per request.

Syntax
```

```

Fields

Field Description

`ipv6_private_cidr_block`

(optional) This field is not required and should only be specified if a ULA or private IPv6 prefix is desired for VCN's private IP address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/48` or `fd00:1000:0:1::/64`

`is_oracle_gua_allocation_enabled`

(optional) Indicates whether Oracle will allocate an IPv6 GUA. Only one prefix of /56 size can be allocated by Oracle as a GUA.

`byoipv6_cidr_detail`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_RULE_T Type

A security rule is one of the items in a`NETWORK_SECURITY_GROUP`Type. It is a virtual firewall rule for the VNICs in the network security group. A rule can be for either inbound (`direction`= INGRESS) or outbound (`direction`= EGRESS) IP packets.

Syntax
```

```

Fields

Field Description

`description`

(optional) An optional description of your choice for the rule.

`destination`

(optional) Conceptually, this is the range of IP addresses that a packet originating from the instance can go to. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`destination_type`

(optional) Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`direction`

(required) Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

Allowed values are: 'EGRESS', 'INGRESS'

`icmp_options`

(optional)

`id`

(optional) An Oracle-assigned identifier for the security rule. You specify this ID when you want to update or delete the rule. Example: `04ABEC`

`is_stateless`

(optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`is_valid`

(optional) Whether the rule is valid. The value is `True` when the rule is first created. If the rule's `source` or `destination` is a network security group, the value changes to `False` if that network security group is deleted.

`protocol`

(required) The transport protocol. Specify either `all` or an IPv4 protocol number as defined in[Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

`source`

(optional) Conceptually, this is the range of IP addresses that a packet coming into the instance can come from. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`source_type`

(optional) Type of source for the rule. Required if `direction` = `INGRESS`. * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic coming from a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`tcp_options`

(optional)

`time_created`

(optional) The date and time the security rule was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`udp_options`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_ADDED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules that were added.

### DBMS_CLOUD_OCI_VN_MONITORING_ENDPOINT_T Type

Information describing a source or destination in a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the `Endpoint`.

Allowed values are: 'IP_ADDRESS', 'SUBNET', 'COMPUTE_INSTANCE', 'VNIC', 'LOAD_BALANCER', 'LOAD_BALANCER_LISTENER', 'NETWORK_LOAD_BALANCER', 'NETWORK_LOAD_BALANCER_LISTENER', 'VLAN'

### DBMS_CLOUD_OCI_VN_MONITORING_PROTOCOL_PARAMETERS_T Type

Defines the IP protocol parameters for a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the `ProtocolParameters` object.

Allowed values are: 'TCP', 'UDP', 'ICMP'

### DBMS_CLOUD_OCI_VN_MONITORING_QUERY_OPTIONS_T Type

Defines the query options required for a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`is_bi_directional_analysis`

(optional) If true, a path analysis is done for both the forward and reverse routes.

### DBMS_CLOUD_OCI_VN_MONITORING_GET_PATH_ANALYSIS_DETAILS_T Type

Defines the configuration for getting a path analysis.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the `PathAnalysis` query.

Allowed values are: 'PERSISTED_QUERY', 'ADHOC_QUERY'

### DBMS_CLOUD_OCI_VN_MONITORING_ADHOC_GET_PATH_ANALYSIS_DETAILS_T Type

Defines the configuration for getting an ad-hoc path analysis.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_adhoc_get_path_analysis_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_get_path_analysis_details_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment.

`protocol`

(required) The IP protocol to used for the path analysis.

`source_endpoint`

(required)

`destination_endpoint`

(required)

`protocol_parameters`

(optional)

`query_options`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_PHASE_ONE_PARAMETERS_T Type

Allowed phase one parameters.

Syntax
```

```

Fields

Field Description

`encryption_algorithms`

(optional) Allowed phase one encryption algorithms.

`authentication_algorithms`

(optional) Allowed phase one authentication algorithms.

`dh_groups`

(optional) Allowed phase one Diffie-Hellman groups.

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_PHASE_TWO_PARAMETERS_T Type

Allowed phase two parameters.

Syntax
```

```

Fields

Field Description

`encryption_algorithms`

(optional) Allowed phase two encryption algorithms.

`authentication_algorithms`

(optional) Allowed phase two authentication algorithms.

`pfs_dh_groups`

(optional) Allowed perfect forward secrecy Diffie-Hellman groups.

### DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_PHASE_ONE_PARAMETERS_T Type

Default phase one parameters.

Syntax
```

```

Fields

Field Description

`default_encryption_algorithms`

(optional) Default phase one encryption algorithms.

`default_authentication_algorithms`

(optional) Default phase one authentication algorithms.

`default_dh_groups`

(optional) Default phase one Diffie-Hellman groups.

### DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_PHASE_TWO_PARAMETERS_T Type

Default phase two parameters.

Syntax
```

```

Fields

Field Description

`default_encryption_algorithms`

(optional) Default phase two encryption algorithms.

`default_authentication_algorithms`

(optional) Default phase two authentication algorithms.

`default_pfs_dh_group`

(optional) Default perfect forward secrecy Diffie-Hellman groups.

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_IKE_IP_SEC_PARAMETERS_T Type

Lists the current allowed and default IPSec tunnel parameters.

Syntax
```

```

Fields

Field Description

`allowed_phase_one_parameters`

(required)

`allowed_phase_two_parameters`

(required)

`default_phase_one_parameters`

(required)

`default_phase_two_parameters`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_CONFIGURATION_T Type

Defines the allowed security configuration for the traffic.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the allowed security configuration.

Allowed values are: 'NSG', 'STATEFUL_NSG', 'INGRESS_SECURITY_LIST', 'STATEFUL_INGRESS_SECURITY_LIST', 'EGRESS_SECURITY_LIST', 'STATEFUL_EGRESS_SECURITY_LIST'

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_ACTION_DETAILS_T Type

Defines details for the security action taken on allowed traffic.

Syntax
```

```

Fields

Field Description

`is_restricted_or_partial`

(required) If true, the allowed security configuration details are incomplete.

`allowed_security_configuration`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_ACTION_T Type

Defines the security action taken on allowed traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_allowed_security_action_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_security_action_t`type.

Fields

Field Description

`allowed_security_action_details`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_BGP_SESSION_INFO_T Type

Information for establishing a BGP session for the IPSec tunnel.

Syntax
```

```

Fields

Field Description

`oracle_interface_ip`

(optional) The IP address for the Oracle end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is required and used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address so you can troubleshoot or monitor the tunnel. The value must be a /30 or /31. Example: `10.0.0.4/31`

`customer_interface_ip`

(optional) The IP address for the CPE end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is required and used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address so you can troubleshoot or monitor the tunnel. The value must be a /30 or /31. Example: `10.0.0.5/31`

`oracle_interface_ipv6`

(optional) The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`customer_interface_ipv6`

(optional) The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`oracle_bgp_asn`

(optional) The Oracle BGP ASN.

`customer_bgp_asn`

(optional) If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this ASN is required and used for the tunnel's BGP session. This is the ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format. If the tunnel uses static routing, the `customerBgpAsn` must be null. Example: `12345` (2-byte) or `1587232876` (4-byte)

`bgp_state`

(optional) The state of the BGP session.

Allowed values are: 'UP', 'DOWN'

`bgp_ipv6_state`

(optional) The state of the BGP IPv6 session.

Allowed values are: 'UP', 'DOWN'

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) An individual public IP prefix (CIDR) to add to the public virtual circuit. All prefix sizes are allowed.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_create_virtual_circuit_public_prefix_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`public_prefixes`

(required) The public IP prefixes (CIDRs) to add to the public virtual circuit.

### DBMS_CLOUD_OCI_VN_MONITORING_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) An individual public IP prefix (CIDR) to remove from the public virtual circuit.

### DBMS_CLOUD_OCI_VN_MONITORING_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_delete_virtual_circuit_public_prefix_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`public_prefixes`

(required) The public IP prefixes (CIDRs) to remove from the public virtual circuit.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_SUMMARY_T Type

A summary of CIDR block subranges that are currently allocated to an IP pool.

Syntax
```

```

Fields

Field Description

`cidr_block`

(optional) The BYOIP CIDR block range or subrange allocated to an IP pool. This could be all or part of a BYOIP CIDR block.

`public_ip_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IP pool containing the CIDR block.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_byoip_allocated_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_COLLECTION_T Type

Results of a `ListByoipAllocatedRanges` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of subranges of a BYOIP CIDR block allocated to an IP pool.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_T Type

A summary of IPv6 CIDR block subranges currently allocated to a VCN.

Syntax
```

```

Fields

Field Description

`byoip_range_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource to which the CIDR block belongs.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the `ByoipRange`.

`ipv6_cidr_block`

(optional) The BYOIPv6 CIDR block range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 CIDR block. Each VCN allocation must be /64 or larger.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `Vcn` resource to which the ByoipRange belongs.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_byoip_range_vcn_ipv6_allocation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_T Type

Oracle offers the ability to Bring Your Own IP (BYOIP), importing public IP addresses or IPv6 addresses that you currently own to Oracle Cloud Infrastructure. A `ByoipRange` resource is a record of the imported address block (a BYOIP CIDR block) and also some associated metadata. The process used to[Bring Your Own IP](https://docs.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm)is explained in the documentation.

Syntax
```

```

Fields

Field Description

`byoip_range_vcn_ipv6_allocations`

(optional) A list of `ByoipRangeVcnIpv6AllocationSummary` objects.

`cidr_block`

(optional) The public IPv4 CIDR block being imported from on-premises to the Oracle cloud.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the BYOIP CIDR block.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource.

`ipv6_cidr_block`

(optional) The IPv6 CIDR block being imported to the Oracle cloud. This CIDR block must be /48 or larger, and can be subdivided into sub-ranges used across multiple VCNs. A BYOIPv6 prefix can be also assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.

`lifecycle_details`

(optional) The `ByoipRange` resource's current status.

Allowed values are: 'CREATING', 'VALIDATING', 'PROVISIONED', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'ADVERTISING', 'WITHDRAWING'

`lifecycle_state`

(required) The `ByoipRange` resource's current state.

Allowed values are: 'INACTIVE', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the `ByoipRange` resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_validated`

(optional) The date and time the `ByoipRange` resource was validated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_advertised`

(optional) The date and time the `ByoipRange` resource was advertised to the internet by BGP, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_withdrawn`

(optional) The date and time the `ByoipRange` resource was withdrawn from advertisement by BGP to the internet, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`validation_token`

(required) The validation token is an internally-generated ASCII string used in the validation process. See[Importing a CIDR block](https://docs.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr)for details.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_SUMMARY_T Type

Information about a `ByoipRange` resource.

Syntax
```

```

Fields

Field Description

`byoip_range_vcn_ipv6_allocations`

(optional) A list of `ByoipRangeVcnIpv6AllocationSummary` objects.

`cidr_block`

(optional) The public IPv4 address range you are importing to the Oracle cloud.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the `ByoipRange` resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource.

`ipv6_cidr_block`

(optional) The IPv6 CIDR block being imported to the Oracle cloud. This CIDR block must be /48 or larger, and can be subdivided into sub-ranges used across multiple VCNs. A BYOIPv6 prefix can be assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.

`lifecycle_state`

(optional) The `ByoipRange` resource's current state.

`lifecycle_details`

(optional) The Byoip Range's current lifeCycle substate.

`time_created`

(optional) The date and time the `ByoipRange` resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_byoip_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_COLLECTION_T Type

The results returned by a `ListByoipRange` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of `ByoipRange` resource summaries.

### DBMS_CLOUD_OCI_VN_MONITORING_VTAP_CAPTURE_FILTER_RULE_DETAILS_T Type

This resource contains the rules governing what traffic a VTAP mirrors.

Syntax
```

```

Fields

Field Description

`traffic_direction`

(required) The traffic direction the VTAP is configured to mirror.

Allowed values are: 'INGRESS', 'EGRESS'

`rule_action`

(optional) Include or exclude packets meeting this definition from mirrored traffic.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`source_cidr`

(optional) Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.

`destination_cidr`

(optional) Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.

`protocol`

(optional) The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter. Supported options are: * 1 = ICMP * 6 = TCP * 17 = UDP

`icmp_options`

(optional)

`tcp_options`

(optional)

`udp_options`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_T Type

The set of rules governing what traffic the flow log collects when creating a flow log capture filter.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Indicates whether a flow log capture filter rule is enabled.

`priority`

(optional) A lower number indicates a higher priority, range 0-9. Each rule must have a distinct priority.

`sampling_rate`

(optional) Sampling interval as 1 of X, where X is an integer not greater than 100000.

`source_cidr`

(optional) Traffic from this CIDR will be captured in the flow log.

`destination_cidr`

(optional) Traffic to this CIDR will be captured in the flow log.

`protocol`

(optional) The transport protocol the filter uses.

`icmp_options`

(optional)

`tcp_options`

(optional)

`udp_options`

(optional)

`flow_log_type`

(optional) Type or types of flow logs to store. `ALL` includes records for both accepted traffic and rejected traffic.

Allowed values are: 'ALL', 'REJECT', 'ACCEPT'

`rule_action`

(optional) Include or exclude a ruleAction object.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_VN_MONITORING_VTAP_CAPTURE_FILTER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_vtap_capture_filter_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_flow_log_capture_filter_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CAPTURE_FILTER_T Type

A capture filter contains a set of *`CAPTURE_FILTER_RULE_DETAILS`Function* governing what traffic a *`VTAP`Type* mirrors. The capture filter is created with no rules defined, and it must have at least one rule for the VTAP to start mirroring traffic.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the capture filter.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The capture filter's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The capture filter's current administrative state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED'

`filter_type`

(optional) Indicates which service will use this capture filter

Allowed values are: 'VTAP', 'FLOWLOG'

`time_created`

(optional) The date and time the capture filter was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2021-08-25T21:10:29.600Z`

`vtap_capture_filter_rules`

(optional) The set of rules governing what traffic a VTAP mirrors.

`flow_log_capture_filter_rules`

(optional) The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_BYOIP_RANGE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the BYOIP CIDR block move.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CAPTURE_FILTER_COMPARTMENT_DETAILS_T Type

These configuration details are used in the move operation when changing the compartment containing a virtual test access point (VTAP) capture filter.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the VTAP capture filter move.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CPE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the CPE object to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CROSS_CONNECT_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the cross-connect to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the cross-connect group to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_DHCP_OPTIONS_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the set of DHCP options to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_DRG_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the DRG to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_IP_SEC_CONNECTION_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the IPSec connection to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_INTERNET_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the internet gateway to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the local peering gateway to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_NAT_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the NAT gateway to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the network security group to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PATH_ANALYZER_TEST_COMPARTMENT_DETAILS_T Type

Details of the new `compartmentId` for the `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the `PathAnalyzerTest` resource should be moved.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PUBLIC_IP_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the public IP to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PUBLIC_IP_POOL_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the public IP pool move.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the remote peering connection to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the route table to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SECURITY_LIST_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the security list to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SERVICE_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the service gateway to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SUBNET_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the subnet to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VCN_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the VCN to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the virtual circuit to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VLAN_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the VLAN to.

### DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VTAP_COMPARTMENT_DETAILS_T Type

These configuration details are used in the move operation when changing the compartment containing a virtual test access point (VTAP).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the VTAP move.

### DBMS_CLOUD_OCI_VN_MONITORING_COMPARTMENT_INTERNAL_T Type

Helper definition required to perform authZ using SPLAT expressions on a Compartment

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_VN_MONITORING_COMPUTE_INSTANCE_ENDPOINT_T Type

Defines the details required for a COMPUTE_INSTANCE-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_compute_instance_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`address`

(required) The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute instance.

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC attached to the compute instance.

### DBMS_CLOUD_OCI_VN_MONITORING_CONNECT_LOCAL_PEERING_GATEWAYS_DETAILS_T Type

Information about the other local peering gateway (LPG).

Syntax
```

```

Fields

Field Description

`peer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the LPG you want to peer with.

### DBMS_CLOUD_OCI_VN_MONITORING_CONNECT_REMOTE_PEERING_CONNECTIONS_DETAILS_T Type

Information about the other remote peering connection (RPC).

Syntax
```

```

Fields

Field Description

`peer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the RPC you want to peer with.

`peer_region_name`

(required) The name of the region that contains the RPC you want to peer with. Example: `us-ashburn-1`

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_T Type

An object you create when setting up a Site-to-Site VPN between your on-premises network and VCN. The `Cpe` is a virtual representation of your customer-premises equipment, which is the actual router on-premises at your site at your end of the Site-to-Site VPN IPSec connection. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the CPE.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The CPE's Oracle ID (OCID).

`ip_address`

(required) The public IP address of the on-premises router.

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE's device type. The Networking service maintains a general list of CPE device types (for example, Cisco ASA). For each type, Oracle provides CPE configuration content that can help a network engineer configure the CPE. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)uniquely identifies the type of device. To get the OCIDs for the device types on the list, see`LIST_CPE_DEVICE_SHAPES`Function. For information about how to generate CPE configuration content for a CPE device type, see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function

`time_created`

(optional) The date and time the CPE was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`is_private`

(optional) Indicates whether this CPE is of type `private` or not.

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_ANSWER_T Type

An individual answer to a CPE device question. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of`CPE_DEVICE_SHAPE_DETAIL`Type).

Syntax
```

```

Fields

Field Description

`key`

(optional) A string that identifies the question to be answered. See the `key` attribute in`CPE_DEVICE_CONFIG_QUESTION`Function.

`value`

(optional) The answer to the question.

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_QUESTION_T Type

An individual question that the customer can answer about the CPE device. The customer provides answers to these questions in`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function.

Syntax
```

```

Fields

Field Description

`key`

(optional) A string that identifies the question.

`display_name`

(optional) A descriptive label for the question (for example, to display in a form in a graphical interface). Avoid entering confidential information.

`explanation`

(optional) A description or explanation of the question, to help the customer answer accurately.

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_INFO_T Type

Basic information about a particular CPE device type.

Syntax
```

```

Fields

Field Description

`vendor`

(optional) The vendor that makes the CPE device.

`platform_software_version`

(optional) The platform or software version of the CPE device.

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_QUESTION_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_cpe_device_config_question_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_SHAPE_DETAIL_T Type

The detailed information about a particular CPE device type. Compare with`CPE_DEVICE_SHAPE_SUMMARY`Type.

Syntax
```

```

Fields

Field Description

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device shape. This value uniquely identifies the type of CPE device.

`cpe_device_info`

(optional)

`parameters`

(optional) For certain CPE devices types, the customer can provide answers to questions that are specific to the device type. This attribute contains a list of those questions. The Networking service merges the answers with other information and renders a set of CPE configuration content. To provide the answers, use`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function.

`template`

(optional) A template of CPE device configuration information that will be merged with the customer's answers to the questions to render the final CPE device configuration content. Also see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_SHAPE_SUMMARY_T Type

A summary of information about a particular CPE device type. Compare with`CPE_DEVICE_SHAPE_DETAIL`Type.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device shape. This value uniquely identifies the type of CPE device.

`cpe_device_info`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_BYOIP_RANGE_DETAILS_T Type

The information used to create a `ByoipRange` resource.

Syntax
```

```

Fields

Field Description

`cidr_block`

(optional) The BYOIP CIDR block. You can assign some or all of it to a public IP pool after it is validated. Example: `10.0.1.0/24`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the BYOIP CIDR block.

`ipv6_cidr_block`

(optional) The BYOIPv6 CIDR block. You can assign some or all of it to a VCN after it is validated.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CAPTURE_FILTER_DETAILS_T Type

A capture filter contains a set of rules governing what traffic a VTAP mirrors.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the capture filter.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`filter_type`

(required) Indicates which service will use this capture filter

Allowed values are: 'VTAP', 'FLOWLOG'

`vtap_capture_filter_rules`

(optional) The set of rules governing what traffic a VTAP mirrors.

`flow_log_capture_filter_rules`

(optional) The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CPE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the CPE.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`ip_address`

(required) The public IP address of the on-premises router. Example: `203.0.113.2`

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device type. You can provide a value if you want to later generate CPE device configuration content for IPSec connections that use this CPE. You can also call`UPDATE_CPE`Function later to provide a value. For a list of possible values, see`LIST_CPE_DEVICE_SHAPES`Function. For more information about generating CPE device configuration content, see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function

`is_private`

(optional) Indicates whether this CPE is of type `private` or not.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_MACSEC_KEY_T Type

Defines the secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s held in Vault that represent the MACsec key.

Syntax
```

```

Fields

Field Description

`connectivity_association_name_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity association Key Name (CKN) of this MACsec key. NOTE: Only the latest secret version will be used.

`connectivity_association_key_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity Association Key (CAK) of this MACsec key. NOTE: Only the latest secret version will be used.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_MACSEC_PROPERTIES_T Type

Properties used to configure MACsec (if capable).

Syntax
```

```

Fields

Field Description

`state`

(required) Indicates whether or not MACsec is enabled.

Allowed values are: 'ENABLED', 'DISABLED'

`primary_key`

(optional)

`encryption_cipher`

(optional) Type of encryption cipher suite to use for the MACsec connection.

Allowed values are: 'AES128_GCM', 'AES128_GCM_XPN', 'AES256_GCM', 'AES256_GCM_XPN'

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CROSS_CONNECT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the cross-connect.

`cross_connect_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group to put this cross-connect in.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`far_cross_connect_or_cross_connect_group_id`

(optional) If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of that existing cross-connect or cross-connect group.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`location_name`

(required) The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see`LIST_CROSS_CONNECT_LOCATIONS`Function. Example: `CyrusOne, Chandler, AZ`

`near_cross_connect_or_cross_connect_group_id`

(optional) If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of that existing cross-connect or cross-connect group.

`port_speed_shape_name`

(required) The port speed for this cross-connect. To get a list of the available port speeds, see`LIST_CROSSCONNECT_PORT_SPEED_SHAPES`Function. Example: `10 Gbps`

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection that this cross-connect uses.

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CROSS_CONNECT_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the cross-connect group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection that this cross-connect group uses.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTION_T Type

A single DHCP option according to[RFC 1533](https://tools.ietf.org/html/rfc1533). The two options available to use are`DHCP_DNS_OPTION`Type and`DHCP_SEARCH_DOMAIN_OPTION`Type. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

Syntax
```

```

Fields

Field Description

`l_type`

(required) The specific DHCP option. Either `DomainNameServer` (for`DHCP_DNS_OPTION`Type) or `SearchDomain` (for`DHCP_SEARCH_DOMAIN_OPTION`Type).

### DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTION_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_dhcp_option_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DHCP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the set of DHCP options.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`options`

(required) A set of DHCP options.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the set of DHCP options belongs to.

`domain_name_type`

(optional) The search domain name type of DHCP options

Allowed values are: 'SUBNET_DOMAIN', 'VCN_DOMAIN', 'CUSTOM_DOMAIN'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

Allowed values are: 'VCN'

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network attached to the DRG.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ATTACHMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`drg_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table that is assigned to this attachment. The DRG route table manages traffic inside the DRG.

`network_details`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the DRG attachment. If you don't specify a route table here, the DRG attachment is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the DRG attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN. This field is deprecated. Instead, use the `networkDetails` field to specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the DRG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type

Details used to create a route distribution.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the DRG route table belongs to.

`distribution_type`

(required) Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments

Allowed values are: 'IMPORT'

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ROUTE_TABLE_DETAILS_T Type

Details used in a request to create a DRG route table.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the DRG route table belongs to.

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements through referenced attachments are inserted into the DRG route table.

`is_ecmp_enabled`

(optional) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-premises networks, enable ECMP on the DRG route table.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`oracle_interface_ip`

(optional) The IP address for the Oracle end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is required and used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address to troubleshoot or monitor the tunnel. The value must be a /30 or /31. Example: `10.0.0.4/31`

`customer_interface_ip`

(optional) The IP address for the CPE end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is required and used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address to troubleshoot or monitor the tunnel. The value must be a /30 or /31. Example: `10.0.0.5/31`

`oracle_interface_ipv6`

(optional) The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`customer_interface_ipv6`

(optional) The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`customer_bgp_asn`

(optional) If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this ASN is required and used for the tunnel's BGP session. This is the ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format. If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null. Example: `12345` (2-byte) or `1587232876` (4-byte)

### DBMS_CLOUD_OCI_VN_MONITORING_PHASE_ONE_CONFIG_DETAILS_T Type

Configuration details for IKE phase one (ISAKMP) configuration parameters.

Syntax
```

```

Fields

Field Description

`is_custom_phase_one_config`

(optional) Indicates whether custom configuration is enabled for phase one options.

`authentication_algorithm`

(optional) The custom authentication algorithm proposed during phase one tunnel negotiation.

Allowed values are: 'SHA2_384', 'SHA2_256', 'SHA1_96'

`encryption_algorithm`

(optional) The custom encryption algorithm proposed during phase one tunnel negotiation.

Allowed values are: 'AES_256_CBC', 'AES_192_CBC', 'AES_128_CBC'

`diffie_helman_group`

(optional) The custom Diffie-Hellman group proposed during phase one tunnel negotiation.

Allowed values are: 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP19', 'GROUP20', 'GROUP24'

`lifetime_in_seconds`

(optional) Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8 hours.

### DBMS_CLOUD_OCI_VN_MONITORING_PHASE_TWO_CONFIG_DETAILS_T Type

Configuration details for IPSec phase two configuration parameters.

Syntax
```

```

Fields

Field Description

`is_custom_phase_two_config`

(optional) Indicates whether custom configuration is enabled for phase two options.

`authentication_algorithm`

(optional) The authentication algorithm proposed during phase two tunnel negotiation.

Allowed values are: 'HMAC_SHA2_256_128', 'HMAC_SHA1_128'

`encryption_algorithm`

(optional) The encryption algorithm proposed during phase two tunnel negotiation.

Allowed values are: 'AES_256_GCM', 'AES_192_GCM', 'AES_128_GCM', 'AES_256_CBC', 'AES_192_CBC', 'AES_128_CBC'

`lifetime_in_seconds`

(optional) Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.

`is_pfs_enabled`

(optional) Indicates whether perfect forward secrecy (PFS) is enabled.

`pfs_dh_group`

(optional) The Diffie-Hellman group used for PFS, if PFS is enabled.

Allowed values are: 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP19', 'GROUP20', 'GROUP24'

### DBMS_CLOUD_OCI_VN_MONITORING_DPD_CONFIG_T Type

These configuration details are used for dead peer detection (DPD). DPD periodically checks the stability of the connection to the customer premises (CPE), and may be used to detect that the link to the CPE has gone down.

Syntax
```

```

Fields

Field Description

`dpd_mode`

(optional) This option defines whether DPD can be initiated from the Oracle side of the connection.

Allowed values are: 'INITIATE_AND_RESPOND', 'RESPOND_ONLY'

`dpd_timeout_in_sec`

(optional) DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it has lost contact with the CPE. The default is 20 seconds.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type

Request to enable a multi-encryption domain policy on the IPSec tunnel. There can't be more than 50 security associations in use at one time. See[Encryption domain for policy-based tunnels](https://docs.oracle.com/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for more.

Syntax
```

```

Fields

Field Description

`oracle_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.

`cpe_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your on-premises network.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`routing`

(optional) The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).

Allowed values are: 'BGP', 'STATIC', 'POLICY'

`ike_version`

(optional) Internet Key Exchange protocol version.

Allowed values are: 'V1', 'V2'

`shared_secret`

(optional) The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and spaces are allowed. If you don't provide a value, Oracle generates a value for you. You can specify your own shared secret later if you like with`UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Function.

`bgp_session_config`

(optional)

`oracle_initiation`

(optional) Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.

Allowed values are: 'INITIATOR_OR_RESPONDER', 'RESPONDER_ONLY'

`nat_translation_enabled`

(optional) By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500, and when it detects that the port used to forward packets has changed (most likely because a NAT device is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T. The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets. The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T even if it senses there may be a NAT device in use.

Allowed values are: 'ENABLED', 'DISABLED', 'AUTO'

`phase_one_config`

(optional)

`phase_two_config`

(optional)

`dpd_config`

(optional)

`oracle_tunnel_ip`

(optional) The headend IP that you can choose on the Oracle side to terminate your private IPSec tunnel.

`associated_virtual_circuits`

(optional) The list of virtual circuit[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s over which your network can reach this tunnel.

`drg_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table assigned to this attachment. The DRG route table manages traffic inside the DRG.

`encryption_domain_config`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_create_ip_sec_connection_tunnel_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the IPSec connection.

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CPE`Type object.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`cpe_local_identifier`

(optional) Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`. If you don't provide a value, the `ipAddress` attribute for the`CPE`Type object specified by `cpeId` is used as the `cpeLocalIdentifier`. For information about why you'd provide this value, see[If Your CPE Is Behind a NAT Device](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat). Example IP address: `10.0.3.3` Example hostname: `cpe.example.com`

`cpe_local_identifier_type`

(optional) The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.

Allowed values are: 'IP_ADDRESS', 'HOSTNAME'

`static_routes`

(required) Static routes to the CPE. A static route's CIDR must not be a multicast address or class E address. Used for routing a given IPSec tunnel's traffic only if the tunnel is using static routing. If you configure at least one tunnel to use static routing, then you must provide at least one valid static route. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. For more information, see the important note in`IP_SEC_CONNECTION`Type. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `10.0.1.0/24` Example: `2001:db8::/32`

`tunnel_configuration`

(optional) Information for creating the individual tunnels in the IPSec connection. You can provide a maximum of 2 `tunnelConfiguration` objects in the array (one for each of the two tunnels).

`tunnel_count`

(optional) The count of tunnels in the IPsec connection. This value should be equal to the number of `tunnelConfiguration` objects specified in the `CreateIPSecConnection` request.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_INTERNET_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the internet gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`is_enabled`

(required) Whether the gateway is enabled upon creation.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the Internet Gateway is attached to.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the Internet Gateway is using.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IPV6_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`ip_address`

(optional) An IPv6 address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns an IPv6 address from the subnet. The subnet is the one that contains the VNIC you specify in `vnicId`. Example: `2001:DB8::`

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to assign the IPv6 to. The IPv6 will be in the VNIC's subnet.

`ipv6_subnet_cidr`

(optional) The IPv6 CIDR allocated to the subnet. This is required if more than one IPv6 CIDR exists on the subnet.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the local peering gateway (LPG).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the LPG will use. If you don't specify a route table here, the LPG is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the LPG. For information about why you would associate a route table with an LPG, see[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the LPG belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_NAT_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the NAT gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`block_traffic`

(optional) Whether the NAT gateway blocks traffic through it. The default is `false`. Example: `true`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the gateway belongs to.

`public_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP address associated with the NAT gateway.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the NAT gateway. If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_NETWORK_SECURITY_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the network security group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to create the network security group in.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PATH_ANALYZER_TEST_DETAILS_T Type

Details used to create a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the `PathAnalyzerTest` resource's compartment.

`protocol`

(required) The IP protocol to use in the `PathAnalyzerTest` resource.

`source_endpoint`

(required)

`destination_endpoint`

(required)

`protocol_parameters`

(optional)

`query_options`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PRIVATE_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`ip_address`

(optional) A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. Example: `10.0.3.3`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to assign the private IP to. The VNIC and private IP must be in the same subnet.

`vlan_id`

(optional) Use this attribute only with the Oracle Cloud VMware Solution. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN from which the private IP is to be drawn. The IP address, *if supplied*, must be valid for the given VLAN. See`VLAN`Type.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PUBLIC_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the public IP. For ephemeral public IPs, you must set this to the private IP's compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`lifetime`

(required) Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public IP pool. For more information, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

Allowed values are: 'EPHEMERAL', 'RESERVED'

`private_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP to assign the public IP to. Required for an ephemeral public IP because it must always be assigned to a private IP (specifically a *primary* private IP). Optional for a reserved public IP. If you don't provide it, the public IP is created but not assigned to a private IP. You can later assign the public IP with`UPDATE_PUBLIC_IP`Function.

`public_ip_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PUBLIC_IP_POOL_DETAILS_T Type

The information used to create a public IP pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the public IP pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the RPC.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the RPC belongs to.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_RULE_T Type

A mapping between a destination IP address range and a virtual device to route matching packets to (a target).

Syntax
```

```

Fields

Field Description

`cidr_block`

(optional) Deprecated. Instead use `destination` and `destinationType`. Requests that include both `cidrBlock` and `destination` will be rejected. A destination IP address range in CIDR notation. Matching packets will be routed to the indicated network entity (the target). Cannot be an IPv6 CIDR. Example: `0.0.0.0/0`

`destination`

(optional) Conceptually, this is the range of IP addresses used for matching when routing traffic. Required if you provide a `destinationType`. Allowed values: * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`. If you set this to an IPv6 CIDR, the route rule's target can only be a DRG or internet gateway. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a route rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.

`destination_type`

(optional) Type of destination for the rule. Required if you provide a `destination`. * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway).

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK'

`network_entity_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the route rule's target. For information about the type of targets you can specify, see[Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

`description`

(optional) An optional description of your choice for the rule.

`route_type`

(optional) A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.

Allowed values are: 'STATIC', 'LOCAL'

### DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_RULE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_route_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_ROUTE_TABLE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the route table.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_rules`

(required) The collection of rules used for routing destination IPs to network devices.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the route table belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_RULE_T Type

A rule for allowing outbound IP packets.

Syntax
```

```

Fields

Field Description

`destination`

(required) Conceptually, this is the range of IP addresses that a packet originating from the instance can go to. Allowed values: * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` Note that IPv6 addressing is currently supported only in certain regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security list rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.

`destination_type`

(optional) Type of destination for the rule. The default is `CIDR_BLOCK`. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway).

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK'

`icmp_options`

(optional)

`is_stateless`

(optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`protocol`

(required) The transport protocol. Specify either `all` or an IPv4 protocol number as defined in[Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

`tcp_options`

(optional)

`udp_options`

(optional)

`description`

(optional) An optional description of your choice for the rule.

### DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_RULE_T Type

A rule for allowing inbound IP packets.

Syntax
```

```

Fields

Field Description

`icmp_options`

(optional)

`is_stateless`

(optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if ingress traffic allows TCP destination port 80, there should be an egress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`protocol`

(required) The transport protocol. Specify either `all` or an IPv4 protocol number as defined in[Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

`source`

(required) Conceptually, this is the range of IP addresses that a packet coming into the instance can come from. Allowed values: * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security list rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.

`source_type`

(optional) Type of source for the rule. The default is `CIDR_BLOCK`. * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic coming from a particular `Service` through a service gateway).

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK'

`tcp_options`

(optional)

`udp_options`

(optional)

`description`

(optional) An optional description of your choice for the rule.

### DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_egress_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_ingress_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SECURITY_LIST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the security list.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(required) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`ingress_security_rules`

(required) Rules for allowing ingress IP packets.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the security list belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_REQUEST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`SERVICE`Type.

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_REQUEST_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_service_id_request_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SERVICE_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the service gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the service gateway will use. If you don't specify a route table here, the service gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the service gateway. For information about why you would associate a route table with a service gateway, see[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

`services`

(required) List of the OCIDs of the`SERVICE`Type objects to enable for the service gateway. This list can be empty if you don't want to enable any `Service` objects when you create the gateway. You can enable a `Service` object later by using either`ATTACH_SERVICE_ID`Function or`UPDATE_SERVICE_GATEWAY`Function. For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See`ROUTE_TABLE`Type.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SUBNET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) Controls whether the subnet is regional or specific to an availability domain. Oracle recommends creating regional subnets because they're more flexible and make it easier to implement failover across availability domains. Originally, AD-specific subnets were the only kind available to use. To create a regional subnet, omit this attribute. Then any resources later created in this subnet (such as a Compute instance) can be created in any availability domain in the region. To instead create an AD-specific subnet, set this attribute to the availability domain you want this subnet to be in. Then any resources later created in this subnet can only be created in that availability domain. Example: `Uocm:PHX-AD-1`

`cidr_block`

(required) The CIDR IP address range of the subnet. The CIDR must maintain the following rules - a. The CIDR block is valid and correctly formatted. b. The new range is within one of the parent VCN ranges. Example: `10.0.1.0/24`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the subnet.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options the subnet will use. If you don't provide a value, the subnet uses the VCN's default set of DHCP options.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed. This value must be set if you want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It can only be set if the VCN itself was created with a DNS label. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `subnet123`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`ipv6_cidr_block`

(optional) Use this to enable IPv6 addressing for this subnet. The VCN must be enabled for IPv6. You can't change this subnet characteristic later. All subnets are /64 in size. The subnet portion of the IPv6 address is the fourth hextet from the left (1111 in the following example). For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 CIDR blocks (Oracle allocated IPv6 GUA, ULA or private IPv6 CIDR blocks, BYOIPv6 CIDR blocks) for the subnet that meets the following criteria: - The CIDR blocks must be valid. - Multiple CIDR blocks must not overlap each other or the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of IPv6 CIDR blocks allowed to a subnet.

`prohibit_internet_ingress`

(optional) Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false. For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default. `prohibitPublicIpOnVnic` will be set to the value of `prohibitInternetIngress` to dictate IPv4 behavior in this subnet. Only one or the other flag should be specified. Example: `true`

`prohibit_public_ip_on_vnic`

(optional) Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in`CREATE_VNIC_DETAILS`Type). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet). If you intend to use an IPv6 CIDR block, you should use the flag `prohibitInternetIngress` to specify ingress internet traffic behavior of the subnet. Example: `true`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the subnet will use. If you don't provide a value, the subnet uses the VCN's default route table.

`security_list_ids`

(optional) The OCIDs of the security list or lists the subnet will use. If you don't provide a value, the subnet uses the VCN's default security list. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to contain the subnet.

### DBMS_CLOUD_OCI_VN_MONITORING_BYOIPV6_CIDR_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_byoipv6_cidr_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VCN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`cidr_block`

(optional) **Deprecated.** Do *not* set this value. Use `cidrBlocks` instead. Example: `10.0.0.0/16`

`cidr_blocks`

(optional) The list of one or more IPv4 CIDR blocks for the VCN that meet the following criteria: - The CIDR blocks must be valid. - They must not overlap with each other or with the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of CIDR blocks allowed per VCN. **Important:** Do *not* specify a value for `cidrBlock`. Use this parameter instead.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the VCN.

`ipv6_private_cidr_blocks`

(optional) The list of one or more ULA or Private IPv6 CIDR blocks for the vcn that meets the following criteria: - The CIDR blocks must be valid. - Multiple CIDR blocks must not overlap each other or the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of IPv6 CIDR blocks allowed to a vcn. **Important:** Do *not* specify a value for `ipv6CidrBlock`. Use this parameter instead.

`is_oracle_gua_allocation_enabled`

(optional) Specifies whether to skip Oracle allocated IPv6 GUA. By default, Oracle will allocate one GUA of /56 size for an IPv6 enabled VCN.

`byoipv6_cidr_details`

(optional) The list of BYOIPv6 OCIDs and BYOIPv6 CIDR blocks required to create a VCN that uses BYOIPv6 ranges.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed. You must set this value if you want instances to be able to use hostnames to resolve other instances in the VCN. Otherwise the Internet and VCN Resolver will not work. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`is_ipv6_enabled`

(optional) Whether IPv6 is enabled for the VCN. Default is `false`. If enabled, Oracle will assign the VCN a IPv6 /56 CIDR block. You may skip having Oracle allocate the VCN a IPv6 /56 CIDR block by setting isOracleGuaAllocationEnabled to `false`. For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `true`

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_T Type

For use with Oracle Cloud Infrastructure FastConnect. Each`VIRTUAL_CIRCUIT`Type runs on one or more cross-connects or cross-connect groups. A `CrossConnectMapping` contains the properties for an individual cross-connect or cross-connect group associated with a given virtual circuit. The mapping includes information about the cross-connect or cross-connect group, the VLAN, and the BGP peering session. If you're a customer who is colocated with Oracle, that means you own both the virtual circuit and the physical connection it runs on (cross-connect or cross-connect group), so you specify all the information in the mapping. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. If you're a provider, then you own the physical connection that the customer's virtual circuit runs on, so you contribute information about the cross-connect or cross-connect group and VLAN. Who specifies the BGP peering information in the case of customer connection via provider? If the BGP session goes from Oracle to the provider's edge router, then the provider also specifies the BGP peering information. If the BGP session instead goes from Oracle to the customer's edge router, then the customer specifies the BGP peering information. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. Every `CrossConnectMapping` must have BGP IPv4 peering addresses. BGP IPv6 peering addresses are optional. If BGP IPv6 addresses are provided, the customer can exchange IPv6 routes with Oracle.

Syntax
```

```

Fields

Field Description

`bgp_md5_auth_key`

(optional) The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set (null), that means you don't use BGP MD5 authentication.

`cross_connect_or_cross_connect_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).

`customer_bgp_peering_ip`

(optional) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a subnet mask from /28 to /31. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. Example: `10.0.0.18/31`

`oracle_bgp_peering_ip`

(optional) The IPv4 address for Oracle's end of the BGP session. Must use a subnet mask from /28 to /31. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. Example: `10.0.0.19/31`

`customer_bgp_peering_ipv6`

(optional) The BGP IPv6 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv6 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv6 address of the provider's edge router. Only subnet masks from /64 up to /127 are allowed. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:db8::1/64`

`oracle_bgp_peering_ipv6`

(optional) The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses. Note that IPv6 addressing is currently supported only in certain regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:db8::2/64`

`vlan`

(optional) The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider). Example: `200`

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_cross_connect_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`bandwidth_shape_name`

(optional) The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see`LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES`Function. Example: `10 Gbps`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the virtual circuit.

`cross_connect_mappings`

(optional) Create a `CrossConnectMapping` for each cross-connect or cross-connect group this virtual circuit will run on.

`routing_policy`

(optional) The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit. Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`. See[Route Filtering](https://docs.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)for details. By default, routing information is shared for all routes in the same market.

Allowed values are: 'ORACLE_SERVICE_NETWORK', 'REGIONAL', 'MARKET_LEVEL', 'GLOBAL'

`bgp_admin_state`

(optional) Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.

Allowed values are: 'ENABLED', 'DISABLED'

`is_bfd_enabled`

(optional) Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.

`is_transport_mode`

(optional) Set to `true` for the virtual circuit to carry only encrypted traffic, or set to `false` for the virtual circuit to carry unencrypted traffic. If this is not set, the default is `false`.

`customer_bgp_asn`

(optional) Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.

`customer_asn`

(optional) Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format. Example: `12345` (2-byte) or `1587232876` (4-byte)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`gateway_id`

(optional) For private virtual circuits only. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`DRG`Type that this virtual circuit uses.

`provider_name`

(optional) Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see`LIST_FAST_CONNECT_PROVIDER_SERVICES`Function.

`provider_service_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see`LIST_FAST_CONNECT_PROVIDER_SERVICES`Function.

`provider_service_key_name`

(optional) The service key name offered by the provider (if the customer is connecting via a provider).

`provider_service_name`

(optional) Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see`LIST_FAST_CONNECT_PROVIDER_SERVICES`Function.

`public_prefixes`

(optional) For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.

`l_region`

(optional) The Oracle Cloud Infrastructure region where this virtual circuit is located. Example: `phx`

`l_type`

(required) The type of IP addresses used in this virtual circuit. PRIVATE means[RFC 1918](https://tools.ietf.org/html/rfc1918)addresses (10.0.0.0/8, 172.16/12, and 192.168/16).

Allowed values are: 'PUBLIC', 'PRIVATE'

`ip_mtu`

(optional) The layer 3 IP MTU to use with this virtual circuit.

Allowed values are: 'MTU_1500', 'MTU_9000'

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VLAN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) Controls whether the VLAN is regional or specific to an availability domain. A regional VLAN has the flexibility to implement failover across availability domains. Previously, all VLANs were AD-specific. To create a regional VLAN, omit this attribute. Resources created subsequently in this VLAN (such as a Compute instance) can be created in any availability domain in the region. To create an AD-specific VLAN, use this attribute to specify the availability domain. Resources created in this VLAN must be in that availability domain. Example: `Uocm:PHX-AD-1`

`cidr_block`

(required) The range of IPv4 addresses that will be used for layer 3 communication with hosts outside the VLAN. The CIDR must maintain the following rules - 1. The CIDR block is valid and correctly formatted. 2. The new range is within one of the parent VCN ranges. Example: `192.0.2.0/24`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the VLAN.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the VLAN will use. If you don't provide a value, the VLAN uses the VCN's default route table.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to contain the VLAN.

`vlan_tag`

(optional) The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all VLANs in the VCN. If you don't provide a value, Oracle assigns one. You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VNIC_DETAILS_T Type

Contains properties for a VNIC. You use this object when creating the primary VNIC during instance launch or when creating a secondary VNIC. For more information about VNICs, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

Syntax
```

```

Fields

Field Description

`assign_public_ip`

(optional) Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the`SUBNET`Type), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned. **Note:** This public IP address is associated with the primary private IP on the VNIC. For more information, see[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm). **Note:** There's a limit to the number of`PUBLIC_IP`Type a VNIC or instance can have. If you try to create a secondary VNIC with an assigned public IP for an instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm). Example: `false` If you specify a `vlanId`, then `assignPublicIp` must be set to false. See`VLAN`Type.

`assign_private_dns_record`

(optional) Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record registration for the VNIC. If set to true, the DNS record will be registered. The default value is true. If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). When launching an instance, use this `hostnameLabel` instead of the deprecated `hostnameLabel` in`LAUNCH_INSTANCE_DETAILS`Function. If you provide both, the values must match. Example: `bminstance1` If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN can not be assigned a hostname. See`VLAN`Type.

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type. If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId` indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs, all VNICs in the VLAN belong to the NSGs that are associated with the VLAN. See`VLAN`Type.

`private_ip`

(optional) A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's *primary* private IP address. The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. If you specify a `vlanId`, the `privateIp` cannot be specified. See`VLAN`Type. Example: `10.0.3.3`

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip). If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the source/destination check is always disabled for VNICs in a VLAN. See`VLAN`Type. Example: `true`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet to create the VNIC in. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in`LAUNCH_INSTANCE_DETAILS`Function. At least one of them is required; if you provide both, the values must match. If you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`. If you provide both a `vlanId` and `subnetId`, the request fails.

`vlan_id`

(optional) Provide this attribute only if you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN. The value is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN. See`VLAN`Type. Provide a `vlanId` instead of a `subnetId`. If you provide both a `vlanId` and `subnetId`, the request fails.

### DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VTAP_DETAILS_T Type

These details are included in a request to create a virtual test access point (VTAP).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the `Vtap` resource.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN containing the `Vtap` resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source point where packets are captured.

`target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination resource where mirrored packets are sent.

`target_ip`

(optional) The IP address of the destination resource where mirrored packets are sent.

`capture_filter_id`

(required) The capture filter's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`encapsulation_protocol`

(optional) Defines an encapsulation header type for the VTAP's mirrored traffic.

Allowed values are: 'VXLAN'

`vxlan_network_identifier`

(optional) The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.

`is_vtap_enabled`

(optional) Used to start or stop a `Vtap` resource. * `TRUE` directs the VTAP to start mirroring traffic. * `FALSE` (Default) directs the VTAP to stop mirroring traffic.

`source_type`

(optional) The source type for the VTAP.

Allowed values are: 'VNIC', 'SUBNET', 'LOAD_BALANCER', 'DB_SYSTEM', 'EXADATA_VM_CLUSTER', 'AUTONOMOUS_DATA_WAREHOUSE'

`traffic_mode`

(optional) Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT

Allowed values are: 'DEFAULT', 'PRIORITY'

`max_packet_size`

(optional) The maximum size of the packets to be included in the filter.

`target_type`

(optional) The target type for the VTAP.

Allowed values are: 'VNIC', 'NETWORK_LOAD_BALANCER', 'IP_ADDRESS'

`source_private_endpoint_ip`

(optional) The IP Address of the source private endpoint.

`source_private_endpoint_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that source private endpoint belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_MACSEC_KEY_T Type

An object defining the Secrets-in-Vault OCIDs representing the MACsec key.

Syntax
```

```

Fields

Field Description

`connectivity_association_name_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity association Key Name (CKN) of this MACsec key.

`connectivity_association_name_secret_version`

(optional) The secret version of the connectivity association name secret in Vault.

`connectivity_association_key_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity Association Key (CAK) of this MACsec key.

`connectivity_association_key_secret_version`

(optional) The secret version of the `connectivityAssociationKey` secret in Vault.

### DBMS_CLOUD_OCI_VN_MONITORING_MACSEC_PROPERTIES_T Type

Properties used for MACsec (if capable).

Syntax
```

```

Fields

Field Description

`state`

(required) Indicates whether or not MACsec is enabled.

Allowed values are: 'ENABLED', 'DISABLED'

`primary_key`

(optional)

`encryption_cipher`

(optional) Type of encryption cipher suite to use for the MACsec connection.

Allowed values are: 'AES128_GCM', 'AES128_GCM_XPN', 'AES256_GCM', 'AES256_GCM_XPN'

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_T Type

For use with Oracle Cloud Infrastructure FastConnect. A cross-connect represents a physical connection between an existing network and Oracle. Customers who are colocated with Oracle in a FastConnect location create and use cross-connects. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). Oracle recommends you create each cross-connect in a`CROSS_CONNECT_GROUP`Type so you can use link aggregation with the connection. **Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cross-connect group.

`cross_connect_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group this cross-connect belongs to (if any).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(optional) The cross-connect's Oracle ID (OCID).

`lifecycle_state`

(optional) The cross-connect's current state.

Allowed values are: 'PENDING_CUSTOMER', 'PROVISIONING', 'PROVISIONED', 'INACTIVE', 'TERMINATING', 'TERMINATED'

`location_name`

(optional) The name of the FastConnect location where this cross-connect is installed.

`port_name`

(optional) A string identifying the meet-me room port for this cross-connect.

`port_speed_shape_name`

(optional) The port speed for this cross-connect. Example: `10 Gbps`

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection that this cross-connect uses.

`time_created`

(optional) The date and time the cross-connect was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`macsec_properties`

(optional)

`oci_physical_device_name`

(optional) The FastConnect device that terminates the physical connection.

`oci_logical_device_name`

(optional) The FastConnect device that terminates the logical connection. This device might be different than the device that terminates the physical connection.

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_GROUP_T Type

For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group is a link aggregation group (LAG), which can contain one or more`CROSS_CONNECT`Type. Customers who are colocated with Oracle in a FastConnect location create and use cross-connect groups. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). **Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cross-connect group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(optional) The cross-connect group's Oracle ID (OCID).

`lifecycle_state`

(optional) The cross-connect group's current state.

Allowed values are: 'PROVISIONING', 'PROVISIONED', 'INACTIVE', 'TERMINATING', 'TERMINATED'

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection that this cross-connect group uses.

`time_created`

(optional) The date and time the cross-connect group was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`macsec_properties`

(optional)

`oci_physical_device_name`

(optional) The FastConnect device that terminates the physical connection.

`oci_logical_device_name`

(optional) The FastConnect device that terminates the logical connection. This device might be different than the device that terminates the physical connection.

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_LOCATION_T Type

An individual FastConnect location.

Syntax
```

```

Fields

Field Description

`description`

(required) A description of the location.

`name`

(required) The name of the location. Example: `CyrusOne, Chandler, AZ`

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_T Type

For use with Oracle Cloud Infrastructure FastConnect. Each`VIRTUAL_CIRCUIT`Type runs on one or more cross-connects or cross-connect groups. A `CrossConnectMappingDetails` contains the properties for an individual cross-connect or cross-connect group associated with a given virtual circuit. The details includes information about the cross-connect or cross-connect group, the VLAN, and the BGP peering session.

Syntax
```

```

Fields

Field Description

`bgp_md5_auth_key`

(optional) The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set (null), that means you don't use BGP MD5 authentication.

`cross_connect_or_cross_connect_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).

`customer_bgp_peering_ip`

(optional) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a subnet mask from /28 to /31. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. Example: `10.0.0.18/31`

`oracle_bgp_peering_ip`

(optional) The IPv4 address for Oracle's end of the BGP session. Must use a subnet mask from /28 to /31. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses. Example: `10.0.0.19/31`

`customer_bgp_peering_ipv6`

(optional) The BGP IPv6 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv6 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv6 address of the provider's edge router. Only subnet masks from /64 up to /127 are allowed. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses. Example: `2001:db8::1/64`

`oracle_bgp_peering_ipv6`

(optional) The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this. There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses. Example: `2001:db8::2/64`

`vlan`

(optional) The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider). Example: `200`

`ipv4_bgp_status`

(optional) The state of the Ipv4 BGP session.

Allowed values are: 'UP', 'DOWN'

`ipv6_bgp_status`

(optional) The state of the Ipv6 BGP session.

Allowed values are: 'UP', 'DOWN'

`oci_logical_device_name`

(optional) The FastConnect device that terminates the logical connection.

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_cross_connect_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_COLLECTION_T Type

An array of CrossConnectMappingDetails

Syntax
```

```

Fields

Field Description

`items`

(required) CrossConnectMappingDetails items

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_PORT_SPEED_SHAPE_T Type

An individual port speed level for cross-connects.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the port speed shape. Example: `10 Gbps`

`port_speed_in_gbps`

(required) The port speed in Gbps. Example: `10`

### DBMS_CLOUD_OCI_VN_MONITORING_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_STATUS_T Type

The status of the cross-connect.

Syntax
```

```

Fields

Field Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`interface_state`

(optional) Indicates whether Oracle's side of the interface is up or down.

Allowed values are: 'UP', 'DOWN'

`light_level_ind_bm`

(optional) The light level of the cross-connect (in dBm). Example: `14.0`

`light_level_indicator`

(optional) Status indicator corresponding to the light level. * **NO_LIGHT:** No measurable light * **LOW_WARN:** There's measurable light but it's too low * **HIGH_WARN:** Light level is too high * **BAD:** There's measurable light but the signal-to-noise ratio is bad * **GOOD:** Good light level

Allowed values are: 'NO_LIGHT', 'LOW_WARN', 'HIGH_WARN', 'BAD', 'GOOD'

`encryption_status`

(optional) Encryption status of this cross connect. Possible values: * **UP:** Traffic is encrypted over this cross-connect * **DOWN:** Traffic is not encrypted over this cross-connect * **CIPHER_MISMATCH:** The MACsec encryption cipher doesn't match the cipher on the CPE * **CKN_MISMATCH:** The MACsec Connectivity association Key Name (CKN) doesn't match the CKN on the CPE * **CAK_MISMATCH:** The MACsec Connectivity Association Key (CAK) doesn't match the CAK on the CPE

Allowed values are: 'UP', 'DOWN', 'CIPHER_MISMATCH', 'CKN_MISMATCH', 'CAK_MISMATCH'

`light_levels_in_d_bm`

(optional) The light levels of the cross-connect (in dBm). Example: `[14.0, -14.0, 2.1, -10.1]`

### DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_DRG_ROUTE_TABLES_T Type

The default DRG route table for this DRG. Each network type has a default DRG route table. You can update a network type to use a different DRG route table, but each network type must have a default DRG route table. You cannot delete a default DRG route table.

Syntax
```

```

Fields

Field Description

`vcn`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the default DRG route table to be assigned to DRG attachments of type VCN on creation.

`ipsec_tunnel`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the default DRG route table assigned to DRG attachments of type IPSEC_TUNNEL on creation.

`virtual_circuit`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the default DRG route table to be assigned to DRG attachments of type VIRTUAL_CIRCUIT on creation.

`remote_peering_connection`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the default DRG route table to be assigned to DRG attachments of type REMOTE_PEERING_CONNECTION on creation.

### DBMS_CLOUD_OCI_VN_MONITORING_DENIED_SECURITY_ACTION_DETAILS_T Type

Defines details for the security action taken on denied traffic.

Syntax
```

```

Fields

Field Description

`is_restricted_or_partial`

(required) If true, the evaluated security list and network security group ID details are incomplete.

`evaluated_security_list_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of evaluated security lists associcated with the OCI resource's subnet.

`evaluated_nsg_ids`

(optional) List of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of evaluated network security groups associated with the OCI resource's VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_DENIED_SECURITY_ACTION_T Type

Defines the security action taken on denied traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_denied_security_action_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_security_action_t`type.

Fields

Field Description

`denied_security_action_details`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_DHCP_DNS_OPTION_T Type

DHCP option for specifying how DNS (hostname resolution) is handled in the subnets in the VCN. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_dhcp_dns_option_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_dhcp_option_t`type.

Fields

Field Description

`custom_dns_servers`

(optional) If you set `serverType` to `CustomDnsServer`, specify the IP address of at least one DNS server of your choice (three maximum).

`server_type`

(required) * **VcnLocal:** Reserved for future use. * **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\". Instances can resolve internet hostnames (no internet gateway is required), and can resolve hostnames of instances in the VCN. This is the default value in the default set of DHCP options in the VCN. For the Internet and VCN Resolver to work across the VCN, there must also be a DNS label set for the VCN, a DNS label set for each subnet, and a hostname for each instance. The Internet and VCN Resolver also enables reverse DNS lookup, which lets you determine the hostname corresponding to the private IP address. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). * **CustomDnsServer:** Instances use a DNS server of your choice (three maximum).

Allowed values are: 'VcnLocal', 'VcnLocalPlusInternet', 'CustomDnsServer'

### DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTIONS_T Type

A set of DHCP options. Used by the VCN to automatically provide configuration information to the instances when they boot up. There are two options you can set: -`DHCP_DNS_OPTION`Type: Lets you specify how DNS (hostname resolution) is handled in the subnets in your VCN. -`DHCP_SEARCH_DOMAIN_OPTION`Type: Lets you specify a search domain name to use for DNS queries. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the set of DHCP options.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the set of DHCP options.

`lifecycle_state`

(required) The current state of the set of DHCP options.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`options`

(required) The collection of individual DHCP options.

`time_created`

(required) Date and time the set of DHCP options was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the set of DHCP options belongs to.

`domain_name_type`

(optional) The search domain name type of DHCP options

Allowed values are: 'SUBNET_DOMAIN', 'VCN_DOMAIN', 'CUSTOM_DOMAIN'

### DBMS_CLOUD_OCI_VN_MONITORING_DHCP_SEARCH_DOMAIN_OPTION_T Type

DHCP option for specifying a search domain name for DNS queries. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_dhcp_search_domain_option_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_dhcp_option_t`type.

Fields

Field Description

`search_domain_names`

(required) A single search domain name according to[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). During a DNS query, the OS will append this search domain name to the value being queried. If you set`DHCP_DNS_OPTION`Type to `VcnLocalPlusInternet`, and you assign a DNS label to the VCN during creation, the search domain name in the VCN's default set of DHCP options is automatically set to the VCN domain (for example, `vcn1.oraclevcn.com`). If you don't want to use a search domain name, omit this option from the set of DHCP options. Do not include this option with an empty list of search domain names, or with an empty string as the value for any search domain name.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_T Type

A dynamic routing gateway (DRG) is a virtual router that provides a path for private network traffic between networks. You use it with other Networking Service components to create a connection to your on-premises network using[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)or a connection that uses[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). For more information, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the DRG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The DRG's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The DRG's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(optional) The date and time the DRG was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`default_drg_route_tables`

(optional)

`default_export_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this DRG's default export route distribution for the DRG attachments.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

Allowed values are: 'VCN', 'IPSEC_TUNNEL', 'VIRTUAL_CIRCUIT', 'REMOTE_PEERING_CONNECTION'

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network attached to the DRG.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_T Type

A DRG attachment serves as a link between a DRG and a network resource. A DRG can be attached to a VCN, IPSec tunnel, remote peering connection, or virtual circuit. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the DRG attachment.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`id`

(required) The DRG attachment's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The DRG attachment's current state.

Allowed values are: 'ATTACHING', 'ATTACHED', 'DETACHING', 'DETACHED'

`time_created`

(optional) The date and time the DRG attachment was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`drg_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table that is assigned to this attachment. The DRG route table manages traffic inside the DRG.

`network_details`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the DRG attachment is using. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)This field is deprecated. Instead, use the `networkDetails` field to view the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN. This field is deprecated. Instead, use the `networkDetails` field to view the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

`export_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export route distribution used to specify how routes in the assigned DRG route table are advertised to the attachment. If this value is null, no routes are advertised through this attachment.

`is_cross_tenancy`

(optional) Indicates whether the DRG attachment and attached network live in a different tenancy than the DRG. Example: `false`

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_ID_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The criteria by which a specific attachment will import routes to the DRG.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_drg_attachment_id_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_route_distribution_match_criteria_t`type.

Fields

Field Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_INFO_T Type

The `DrgAttachmentInfo` resource contains the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle-assigned ID of the DRG attachment

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_MATCH_ALL_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

All routes are imported or exported.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_drg_attachment_match_all_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_route_distribution_match_criteria_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

Allowed values are: 'VCN'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_TYPE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The attachment type from which the DRG will import routes. Routes will be imported from all attachments of this type.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_drg_attachment_type_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_route_distribution_match_criteria_t`type.

Fields

Field Description

`attachment_type`

(required) The type of the network resource to be included in this match. A match for a network type implies that all DRG attachments of that type insert routes into the table.

Allowed values are: 'VCN', 'VIRTUAL_CIRCUIT', 'REMOTE_PEERING_CONNECTION', 'IPSEC_TUNNEL'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_REDUNDANCY_STATUS_T Type

The redundancy status of the DRG. For more information, see[Redundancy Remedies](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/drgredundancy.htm).

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`status`

(optional) The redundancy status of the DRG.

Allowed values are: 'NOT_AVAILABLE', 'REDUNDANT', 'NOT_REDUNDANT_SINGLE_IPSEC', 'NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT', 'NOT_REDUNDANT_MULTIPLE_IPSECS', 'NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS', 'NOT_REDUNDANT_MIX_CONNECTIONS', 'NOT_REDUNDANT_NO_CONNECTION'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_T Type

A route distribution establishes how routes get imported into DRG route tables and exported through the DRG attachments. A route distribution is a list of statements. Each statement consists of a set of matches, all of which must be `True` in order for the statement's action to take place. Each statement determines which routes are propagated. You can assign a route distribution as a route table's import distribution. The statements in an import route distribution specify how how incoming route advertisements through a referenced attachment or all attachments of a certain type are inserted into the route table. You can assign a route distribution as a DRG attachment's export distribution unless the attachment has the type VCN. Exporting routes through a VCN attachment is unsupported. Export route distribution statements specify how routes in a DRG attachment's assigned table are advertised out through the attachment. When a DRG is created, a route distribution is created with a single ACCEPT statement with match criteria MATCH_ALL. By default, all DRG attachments (except for those of type VCN), are assigned this distribution. The two auto-generated DRG route tables (one as the default for VCN attachments, and the other for all other types of attachments) are each assigned an auto generated import route distribution. The default VCN table's import distribution has a single statement with match criteria MATCH_ALL to import routes from each DRG attachment type. The other table's import distribution has a statement to import routes from attachments with the VCN type. The route distribution is always in the same compartment as the DRG.

Syntax
```

```

Fields

Field Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG that contains this route distribution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the route distribution.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The route distribution's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The route distribution's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(required) The date and time the route distribution was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`distribution_type`

(required) Whether this distribution defines how routes get imported into route tables or exported through DRG attachments.

Allowed values are: 'IMPORT', 'EXPORT'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_STATEMENT_T Type

A single statement within a route distribution. All match criteria in a statement must be met for the action to take place.

Syntax
```

```

Fields

Field Description

`match_criteria`

(required) The action is applied only if all of the match criteria is met. If there are no match criteria in a statement, any input is considered a match and the action is applied.

`action`

(required) `ACCEPT` indicates the route should be imported or exported as-is.

Allowed values are: 'ACCEPT'

`priority`

(required) This field specifies the priority of each statement in a route distribution. Priorities must be unique within a particular route distribution. The priority will be represented as a number between 0 and 65535 where a lower number indicates a higher priority. When a route is processed, statements are applied in the order defined by their priority. The first matching rule dictates the action that will be taken on the route.

`id`

(required) The Oracle-assigned ID of the route distribution statement.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_RULE_T Type

A DRG route rule is a mapping between a destination IP address range and a DRG attachment. The map is used to route matching packets. Traffic will be routed across the attachments using Equal-cost multi-path routing (ECMP) if there are multiple rules with identical destinations and none of the rules conflict.

Syntax
```

```

Fields

Field Description

`destination`

(required) Represents the range of IP addresses to match against when routing traffic. Potential values: * An IP address range (IPv4 or IPv6) in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`. * When you're setting up a security rule for traffic destined for a particular `Service` through a service gateway, this is the `cidrBlock` value associated with that`SERVICE`Type. For example: `oci-phx-objectstorage`.

`destination_type`

(required) The type of destination for the rule. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway).

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK'

`next_hop_drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next hop DRG attachment responsible for reaching the network destination. A value of `BLACKHOLE` means traffic for this route is discarded without notification.

`route_type`

(optional) You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.

Allowed values are: 'STATIC', 'DYNAMIC'

`is_conflict`

(optional) Indicates that the route was not imported due to a conflict between route rules.

`is_blackhole`

(optional) Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.

`id`

(required) The Oracle-assigned ID of the DRG route rule.

`route_provenance`

(required) The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment, and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`, because that is the earliest origin. No routes with a provenance `IPSEC_TUNNEL` or `VIRTUAL_CIRCUIT` will be exported to IPsec tunnel or virtual circuit attachments, regardless of the attachment's export distribution.

Allowed values are: 'STATIC', 'VCN', 'VIRTUAL_CIRCUIT', 'IPSEC_TUNNEL'

`attributes`

(optional) Additional properties for the route, computed by the service.

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_TABLE_T Type

All routing inside the DRG is driven by the contents of DRG route tables. DRG route tables contain rules which route packets to a particular network destination, represented as a DRG attachment. The routing decision for a packet entering a DRG is determined by the rules in the DRG route table assigned to the attachment-of-entry. Each DRG attachment can inject routes in any DRG route table, provided there is a statement corresponding to the attachment in the route table's `importDrgRouteDistribution`. You can also insert static routes into the DRG route tables. The DRG route table is always in the same compartment as the DRG. There must always be a default DRG route table for each attachment type.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the DRG is in. The DRG route table is always in the same compartment as the DRG.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the DRG that contains this route table.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`time_created`

(required) The date and time the DRG route table was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The DRG route table's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements from referenced attachments are inserted into the DRG route table.

`is_ecmp_enabled`

(required) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-premises network, enable ECMP on the DRG route table to which these attachments import routes.

### DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_CONFIGURATION_T Type

Defines the type of the resource that forwarded traffic.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the forwarded routing configuration.

Allowed values are: 'VCN', 'DRG'

### DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTING_CONFIGURATION_T Type

Identifies the DRG route table and rule that allowed the traffic to be forwarded.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_drg_routing_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_forwarded_routing_configuration_t`type.

Fields

Field Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table that allowed the traffic.

`route_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_LIST_CONFIGURATION_T Type

Defines the subnet egress security list configuration that allowed the traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_egress_security_list_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_ENCRYPTION_DOMAIN_CONFIG_T Type

Configuration information used by the encryption domain policy.

Syntax
```

```

Fields

Field Description

`oracle_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.

`cpe_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your on-premises network.

### DBMS_CLOUD_OCI_VN_MONITORING_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error message.

`original_message`

(optional) A human-readable error string in English. This value might be different from the `message` field.

`original_message_template`

(optional) The template for the `originalMessage` in ICU message format, but without the values to be substituted.

`message_arguments`

(optional) The values to be substituted into the `originalMessageTemplate`, expressed as a string-to-string map.

### DBMS_CLOUD_OCI_VN_MONITORING_FAST_CONNECT_PROVIDER_SERVICE_T Type

A service offering from a supported provider. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Syntax
```

```

Fields

Field Description

`description`

(optional) The location of the provider's website or portal. This portal is where you can get information about the provider service, create a virtual circuit connection from the provider to Oracle Cloud Infrastructure, and retrieve your provider service key for that virtual circuit connection. Example: `https://example.com`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service offered by the provider.

`private_peering_bgp_management`

(required) Who is responsible for managing the private peering BGP information.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`provider_name`

(required) The name of the provider.

`provider_service_name`

(required) The name of the service offered by the provider.

`public_peering_bgp_management`

(required) Who is responsible for managing the public peering BGP information.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`supported_virtual_circuit_types`

(optional) An array of virtual circuit types supported by this service.

Allowed values are: 'PUBLIC', 'PRIVATE'

`customer_asn_management`

(required) Who is responsible for managing the ASN information for the network at the other end of the connection from Oracle.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`provider_service_key_management`

(required) Who is responsible for managing the provider service key.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`bandwith_shape_management`

(required) Who is responsible for managing the virtual circuit bandwidth.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`required_total_cross_connects`

(required) Total number of cross-connect or cross-connect groups required for the virtual circuit.

`l_type`

(required) Provider service type.

Allowed values are: 'LAYER2', 'LAYER3'

### DBMS_CLOUD_OCI_VN_MONITORING_FAST_CONNECT_PROVIDER_SERVICE_KEY_T Type

A provider service key and its details. A provider service key is an identifier for a provider's virtual circuit.

Syntax
```

```

Fields

Field Description

`name`

(required) The service key that the provider gives you when you set up a virtual circuit connection from the provider to Oracle Cloud Infrastructure. Use this value as the `providerServiceKeyName` query parameter for`GET_FAST_CONNECT_PROVIDER_SERVICE_KEY`Function.

`bandwidth_shape_name`

(optional) The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see`LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES`Function. Example: `10 Gbps`

`peering_location`

(optional) The provider's peering location.

### DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_ACTION_DETAILS_T Type

Defines details for the forwarded routing action.

Syntax
```

```

Fields

Field Description

`is_restricted_or_partial`

(required) If true, the forwarded routing configuration details are incomplete.

`forwarded_routing_configuration`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_ACTION_T Type

Defines the routing actions taken for traffic that is forwarded.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_forwarded_routing_action_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_routing_action_t`type.

Fields

Field Description

`forwarded_routing_action_details`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_GET_PUBLIC_IP_BY_IP_ADDRESS_DETAILS_T Type

IP address of the public IP.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The public IP address. Example: 203.0.113.2

### DBMS_CLOUD_OCI_VN_MONITORING_GET_PUBLIC_IP_BY_PRIVATE_IP_ID_DETAILS_T Type

Details of the private IP that the public IP is assigned to.

Syntax
```

```

Fields

Field Description

`private_ip_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP.

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_T Type

A connection between a DRG and CPE. This connection consists of multiple IPSec tunnels. Creating this connection is one of the steps required when setting up a Site-to-Site VPN. **Important:** Each tunnel in an IPSec connection can use either static routing or BGP dynamic routing (see the`IP_SEC_CONNECTION_TUNNEL`Type object's `routing` attribute). Originally only static routing was supported and every IPSec connection was required to have at least one static route configured. To maintain backward compatibility in the API when support for BPG dynamic routing was introduced, the API accepts an empty list of static routes if you configure both of the IPSec tunnels to use BGP dynamic routing. If you switch a tunnel's routing from `BGP` to `STATIC`, you must first ensure that the IPSec connection is configured with at least one valid CIDR block static route. Oracle uses the IPSec connection's static routes when routing a tunnel's traffic *only* if that tunnel's `routing` attribute = `STATIC`. Otherwise the static routes are ignored. For more information about the workflow for setting up an IPSec connection, see[Site-to-Site VPN Overview](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the IPSec connection.

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CPE`Type object.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The IPSec connection's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The IPSec connection's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`cpe_local_identifier`

(optional) Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier here must correspond to the value for `cpeLocalIdentifierType`. If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute for the`CPE`Type object specified by `cpeId` is used as the `cpeLocalIdentifier`. For information about why you'd provide this value, see[If Your CPE Is Behind a NAT Device](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat). Example IP address: `10.0.3.3` Example hostname: `cpe.example.com`

`cpe_local_identifier_type`

(optional) The type of identifier for your CPE device. The value here must correspond to the value for `cpeLocalIdentifier`.

Allowed values are: 'IP_ADDRESS', 'HOSTNAME'

`static_routes`

(required) Static routes to the CPE. The CIDR must not be a multicast address or class E address. Used for routing a given IPSec tunnel's traffic only if the tunnel is using static routing. If you configure at least one tunnel to use static routing, then you must provide at least one valid static route. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `10.0.1.0/24` Example: `2001:db8::/32`

`time_created`

(optional) The date and time the IPSec connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`transport_type`

(optional) The transport type used for the IPSec connection.

Allowed values are: 'INTERNET', 'FASTCONNECT'

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CONFIG_T Type

Deprecated. For tunnel information, instead see: *`IP_SEC_CONNECTION_TUNNEL`Type *`IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Type

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The IP address of Oracle's VPN headend. Example: `203.0.113.50 `

`shared_secret`

(required) The shared secret of the IPSec tunnel.

`time_created`

(optional) The date and time the IPSec connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_tunnel_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_DEVICE_CONFIG_T Type

Deprecated. For tunnel information, instead see: *`IP_SEC_CONNECTION_TUNNEL`Type *`IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the IPSec connection.

`id`

(required) The IPSec connection's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`time_created`

(optional) The date and time the IPSec connection was created.

`tunnels`

(optional) Two`TUNNEL_CONFIG`Type objects.

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_STATUS_T Type

Deprecated. For tunnel information, instead see`IP_SEC_CONNECTION_TUNNEL`Type.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The IP address of Oracle's VPN headend. Example: `203.0.113.50`

`lifecycle_state`

(optional) The tunnel's current state.

Allowed values are: 'UP', 'DOWN', 'DOWN_FOR_MAINTENANCE', 'PARTIAL_UP'

`time_created`

(optional) The date and time the IPSec connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_state_modified`

(optional) When the state of the tunnel last changed, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_STATUS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_tunnel_status_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_DEVICE_STATUS_T Type

Deprecated. For tunnel information, instead see`IP_SEC_CONNECTION_TUNNEL`Type.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the IPSec connection.

`id`

(required) The IPSec connection's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`time_created`

(optional) The date and time the IPSec connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`tunnels`

(optional) Two`TUNNEL_STATUS`Type objects.

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_PHASE_ONE_DETAILS_T Type

IPSec tunnel details specific to ISAKMP phase one.

Syntax
```

```

Fields

Field Description

`is_custom_phase_one_config`

(optional) Indicates whether custom phase one configuration is enabled. If this option is not enabled, default settings are proposed.

`lifetime`

(optional) The total configured lifetime of the IKE security association.

`remaining_lifetime`

(optional) The remaining lifetime before the key is refreshed.

`custom_authentication_algorithm`

(optional) The proposed custom authentication algorithm.

`negotiated_authentication_algorithm`

(optional) The negotiated authentication algorithm.

`custom_encryption_algorithm`

(optional) The proposed custom encryption algorithm.

`negotiated_encryption_algorithm`

(optional) The negotiated encryption algorithm.

`custom_dh_group`

(optional) The proposed custom Diffie-Hellman group.

`negotiated_dh_group`

(optional) The negotiated Diffie-Hellman group.

`is_ike_established`

(optional) Indicates whether IKE phase one is established.

`remaining_lifetime_last_retrieved`

(optional) The date and time we retrieved the remaining lifetime, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_PHASE_TWO_DETAILS_T Type

IPsec tunnel detail information specific to phase two.

Syntax
```

```

Fields

Field Description

`is_custom_phase_two_config`

(optional) Indicates whether custom phase two configuration is enabled. If this option is not enabled, default settings are proposed.

`lifetime`

(optional) The total configured lifetime of the IKE security association.

`remaining_lifetime`

(optional) The remaining lifetime before the key is refreshed.

`custom_authentication_algorithm`

(optional) Phase two authentication algorithm proposed during tunnel negotiation.

`negotiated_authentication_algorithm`

(optional) The negotiated phase two authentication algorithm.

`custom_encryption_algorithm`

(optional) The proposed custom phase two encryption algorithm.

`negotiated_encryption_algorithm`

(optional) The negotiated encryption algorithm.

`dh_group`

(optional) The proposed Diffie-Hellman group.

`negotiated_dh_group`

(optional) The negotiated Diffie-Hellman group.

`is_esp_established`

(optional) Indicates that ESP phase two is established.

`is_pfs_enabled`

(optional) Indicates that PFS (perfect forward secrecy) is enabled.

`remaining_lifetime_last_retrieved`

(optional) The date and time the remaining lifetime was last retrieved, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_T Type

Information about a single IPSec tunnel in an IPSec connection. This object does not include the tunnel's shared secret (pre-shared key), which is found in the`IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Type object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the tunnel.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`vpn_ip`

(optional) The IP address of the Oracle VPN headend for the connection. Example: `203.0.113.21`

`cpe_ip`

(optional) The IP address of the CPE device's VPN headend. Example: `203.0.113.22`

`status`

(optional) The status of the tunnel based on IPSec protocol characteristics.

Allowed values are: 'UP', 'DOWN', 'DOWN_FOR_MAINTENANCE', 'PARTIAL_UP'

`ike_version`

(optional) Internet Key Exchange protocol version.

Allowed values are: 'V1', 'V2'

`lifecycle_state`

(required) The tunnel's lifecycle state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`bgp_session_info`

(optional)

`encryption_domain_config`

(optional)

`routing`

(optional) The type of routing used for this tunnel (BGP dynamic routing, static routing, or policy-based routing).

Allowed values are: 'BGP', 'STATIC', 'POLICY'

`time_created`

(optional) The date and time the IPSec tunnel was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_status_updated`

(optional) When the status of the IPSec tunnel last changed, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`oracle_can_initiate`

(optional) Indicates whether Oracle can only respond to a request to start an IPSec tunnel from the CPE device, or both respond to and initiate requests.

Allowed values are: 'INITIATOR_OR_RESPONDER', 'RESPONDER_ONLY'

`nat_translation_enabled`

(optional) By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500, and when it detects that the port used to forward packets has changed (most likely because a NAT device is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T. The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets. The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T even if it senses there may be a NAT device in use. .

Allowed values are: 'ENABLED', 'DISABLED', 'AUTO'

`dpd_mode`

(optional) Dead peer detection (DPD) mode set on the Oracle side of the connection. This mode sets whether Oracle can only respond to a request from the CPE device to start DPD, or both respond to and initiate requests.

Allowed values are: 'INITIATE_AND_RESPOND', 'RESPOND_ONLY'

`dpd_timeout_in_sec`

(optional) DPD timeout in seconds.

`phase_one_details`

(optional)

`phase_two_details`

(optional)

`associated_virtual_circuits`

(optional) The list of virtual circuit[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s over which your network can reach this tunnel.

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_ERROR_DETAILS_T Type

Details for an error on an IPSec tunnel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique ID generated for each error report.

`error_code`

(required) Unique code describes the error type.

`error_description`

(required) A detailed description of the error.

`solution`

(required) Resolution for the error.

`oci_resources_link`

(required) Link to more Oracle resources or relevant documentation.

`l_timestamp`

(required) Timestamp when the error occurred.

### DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_T Type

The tunnel's shared secret (pre-shared key).

Syntax
```

```

Fields

Field Description

`shared_secret`

(required) The tunnel's shared secret (pre-shared key).

### DBMS_CLOUD_OCI_VN_MONITORING_ICMP_PROTOCOL_PARAMETERS_T Type

Defines the configuration for the[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)protocol parameters.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_icmp_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_protocol_parameters_t`type.

Fields

Field Description

`icmp_code`

(optional) The[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)code.

`icmp_type`

(required) The[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)type.

### DBMS_CLOUD_OCI_VN_MONITORING_ICMP_TRAFFIC_PROTOCOL_PARAMETERS_T Type

Defines the `ProtocolParameters` configuration for the[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)protocol.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_icmp_traffic_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_traffic_protocol_parameters_t`type.

Fields

Field Description

`icmp_code`

(optional) The[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)code.

`icmp_type`

(required) The[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)type.

### DBMS_CLOUD_OCI_VN_MONITORING_INDETERMINATE_ROUTING_ACTION_T Type

Defines the routing action taken on a traffic node where the routing action is INDETERMINATE.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_indeterminate_routing_action_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_routing_action_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_LIST_CONFIGURATION_T Type

Defines the subnet ingress security list configuration that allowed the traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_ingress_security_list_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_INTERNET_GATEWAY_T Type

Represents a router that connects the edge of a VCN with the Internet. For an example scenario that uses an internet gateway, see[Typical Networking Service Scenarios](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#scenarios). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the internet gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The internet gateway's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`is_enabled`

(optional) Whether the gateway is enabled. When the gateway is disabled, traffic is not routed to/from the Internet, regardless of route rules.

`lifecycle_state`

(required) The internet gateway's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(optional) The date and time the internet gateway was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the Internet Gateway belongs to.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the Internet Gateway is using.

### DBMS_CLOUD_OCI_VN_MONITORING_IP_ADDRESS_ENDPOINT_T Type

Defines the details required for an IP_ADDRESS-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_ip_address_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`address`

(required) The IPv4 address of the `Endpoint`.

### DBMS_CLOUD_OCI_VN_MONITORING_IPSEC_TUNNEL_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the IPSec tunnel attached to the DRG.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_ipsec_tunnel_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_details_t`type.

Fields

Field Description

`ipsec_connection_id`

(optional) The IPSec connection that contains the attached IPSec tunnel.

`transport_attachment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit's DRG attachment.

### DBMS_CLOUD_OCI_VN_MONITORING_IPV6_T Type

An *IPv6* is a conceptual term that refers to an IPv6 address and related properties. The `IPv6` object is the API representation of an IPv6. You can create and assign an IPv6 to any VNIC that is in an IPv6-enabled subnet in an IPv6-enabled VCN. **Note:** IPv6 addressing is supported for all commercial and government regions. For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the IPv6. This is the same as the VNIC's compartment.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPv6.

`ip_address`

(required) The IPv6 address of the `IPv6` object. The address is within the IPv6 CIDR block of the VNIC's subnet (see the `ipv6CidrBlock` attribute for the`SUBNET`Type object. Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`

`lifecycle_state`

(required) The IPv6's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the VNIC is in.

`time_created`

(required) The date and time the IPv6 was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC the IPv6 is assigned to. The VNIC and IPv6 must be in the same subnet.

### DBMS_CLOUD_OCI_VN_MONITORING_LETTER_OF_AUTHORITY_T Type

The Letter of Authority for the cross-connect. You must submit this letter when requesting cabling for the cross-connect at the FastConnect location.

Syntax
```

```

Fields

Field Description

`authorized_entity_name`

(optional) The name of the entity authorized by this Letter of Authority.

`circuit_type`

(optional) The type of cross-connect fiber, termination, and optical specification.

Allowed values are: 'Single_mode_LC', 'Single_mode_SC'

`cross_connect_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`facility_location`

(optional) The address of the FastConnect location.

`port_name`

(optional) The meet-me room port for this cross-connect.

`time_expires`

(optional) The date and time when the Letter of Authority expires, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_issued`

(optional) The date and time the Letter of Authority was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_LOAD_BALANCER_ENDPOINT_T Type

Defines the details required for a LOAD_BALANCER-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_load_balancer_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer.

### DBMS_CLOUD_OCI_VN_MONITORING_LOAD_BALANCER_LISTENER_ENDPOINT_T Type

Defines the details required for a LOAD_BALANCER_LISTENER-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_load_balancer_listener_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer listener.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the listener's load balancer.

### DBMS_CLOUD_OCI_VN_MONITORING_LOCAL_PEERING_GATEWAY_T Type

A local peering gateway (LPG) is an object on a VCN that lets that VCN peer with another VCN in the same region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the LPG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The LPG's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`is_cross_tenancy_peering`

(required) Whether the VCN at the other end of the peering is in a different tenancy. Example: `false`

`lifecycle_state`

(required) The LPG's current lifecycle state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`peer_advertised_cidr`

(optional) The smallest aggregate CIDR that contains all the CIDR routes advertised by the VCN at the other end of the peering from this LPG. See `peerAdvertisedCidrDetails` for the individual CIDRs. The value is `null` if the LPG is not peered. Example: `192.168.0.0/16`, or if aggregated with `172.16.0.0/24` then `128.0.0.0/1`

`peer_advertised_cidr_details`

(optional) The specific ranges of IP addresses available on or via the VCN at the other end of the peering from this LPG. The value is `null` if the LPG is not peered. You can use these as destination CIDRs for route rules to route a subnet's traffic to this LPG. Example: [`192.168.0.0/16`, `172.16.0.0/24`]

`peering_status`

(required) Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been peered. `PENDING` means the peering is being established. `REVOKED` means the LPG at the other end of the peering has been deleted.

Allowed values are: 'INVALID', 'NEW', 'PEERED', 'PENDING', 'REVOKED'

`peering_status_details`

(optional) Additional information regarding the peering status, if applicable.

`peer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peered LPG.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the LPG is using. For information about why you would associate a route table with an LPG, see[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

`time_created`

(required) The date and time the LPG was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN that uses the LPG.

### DBMS_CLOUD_OCI_VN_MONITORING_LOOP_BACK_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the loopback attachment on the DRG. A loopback attachment can be used to terminate a virtual circuit that is carrying an IPSec tunnel, routing traffic directly to the IPSec tunnel attachment where the tunnel can terminate.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_loop_back_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_details_t`type.

Fields

Field Description

`ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target IPSec tunnel attachment.

### DBMS_CLOUD_OCI_VN_MONITORING_MODIFY_VCN_CIDR_DETAILS_T Type

Details for updating a CIDR block.

Syntax
```

```

Fields

Field Description

`original_cidr_block`

(required) The CIDR IP address to update.

`new_cidr_block`

(required) The new CIDR IP address.

### DBMS_CLOUD_OCI_VN_MONITORING_NAT_GATEWAY_T Type

A NAT (Network Address Translation) gateway, which represents a router that lets instances without public IPs contact the public internet without exposing the instance to inbound internet traffic. For more information, see[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the NAT gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the NAT gateway.

`block_traffic`

(required) Whether the NAT gateway blocks traffic through it. The default is `false`. Example: `true`

`lifecycle_state`

(required) The NAT gateway's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`nat_ip`

(required) The IP address associated with the NAT gateway.

`time_created`

(required) The date and time the NAT gateway was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the NAT gateway belongs to.

`public_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP address associated with the NAT gateway.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the NAT gateway. If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.

### DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_LOAD_BALANCER_ENDPOINT_T Type

Defines the details required for a NETWORK_LOAD_BALANCER-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_network_load_balancer_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer.

### DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_LOAD_BALANCER_LISTENER_ENDPOINT_T Type

Defines the details required for a NETWORK_LOAD_BALANCER_LISTENER-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_network_load_balancer_listener_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer listener.

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the listener's network load balancer.

### DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_SECURITY_GROUP_T Type

A *network security group* (NSG) provides virtual firewall rules for a specific set of`VNIC`Type in a VCN. Compare NSGs with`SECURITY_LIST`Type, which provide virtual firewall rules to all the VNICs in a *subnet*. A network security group consists of two items: * The set of`VNIC`Type that all have the same security rule needs (for example, a group of Compute instances all running the same application) * A set of NSG`SECURITY_RULE`Type that apply to the VNICs in the group After creating an NSG, you can add VNICs and security rules to it. For example, when you create an instance, you can specify one or more NSGs to add the instance to (see`CREATE_VNIC_DETAILS`Function). Or you can add an existing instance to an NSG with`UPDATE_VNIC`Function. To add security rules to an NSG, see`ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function. To list the VNICs in an NSG, see`LIST_NETWORK_SECURITY_GROUP_VNICS`Function. To list the security rules in an NSG, see`LIST_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function. For more information about network security groups, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). **Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure all of the following are set correctly: * Any security rules in any NSGs the instance's VNIC belongs to * Any`SECURITY_LIST`Type associated with the instance's subnet * The instance's OS firewall rules To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the network security group is in.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`lifecycle_state`

(required) The network security group's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(required) The date and time the network security group was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group's VCN.

### DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_SECURITY_GROUP_VNIC_T Type

Information about a VNIC that belongs to a network security group.

Syntax
```

```

Fields

Field Description

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent resource that the VNIC is attached to (for example, a Compute instance).

`time_associated`

(optional) The date and time the VNIC was added to the network security group, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ENTITY_RELATIONSHIP_T Type

Defines the relationship between Virtual Network topology entities.

Syntax
```

```

Fields

Field Description

`id1`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the first entity in the relationship.

`id2`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second entity in the relationship.

`l_type`

(required) The type of relationship between the entities.

Allowed values are: 'CONTAINS', 'ASSOCIATED_WITH', 'ROUTES_TO'

### DBMS_CLOUD_OCI_VN_MONITORING_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ENTITY_RELATIONSHIP_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_topology_entity_relationship_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_T Type

Defines the representation of a virtual network topology.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the topology object.

Allowed values are: 'NETWORKING', 'VCN', 'SUBNET', 'PATH'

`entities`

(required) Lists entities comprising the virtual network topology.

`relationships`

(required) Lists relationships between entities in the virtual network topology.

`limited_entities`

(required) Lists entities that are limited during ingestion. The values for the items in the list are the entity type names of the limitedEntities. Example: `vcn`

`time_created`

(required) Records when the virtual network topology was created, in[RFC3339](https://tools.ietf.org/html/rfc3339)format for date and time.

### DBMS_CLOUD_OCI_VN_MONITORING_NETWORKING_TOPOLOGY_T Type

Defines the representation of a virtual network topology for a region.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_networking_topology_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_NO_ROUTE_ROUTING_ACTION_DETAILS_T Type

Defines the routing action taken on traffic flow with no route found.

Syntax
```

```

Fields

Field Description

`is_restricted_or_partial`

(required) If true, the evaluated route table details are incomplete.

`evaluated_vcn_route_table_id`

(optional)[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the evaluated VCN route table.

`evaluated_drg_route_table_id`

(optional)[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of evaluated DRG route table.

### DBMS_CLOUD_OCI_VN_MONITORING_NO_ROUTE_ROUTING_ACTION_T Type

Defines the routing actions taken on traffic when no route is found.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_no_route_routing_action_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_routing_action_t`type.

Fields

Field Description

`no_route_routing_action_details`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_NSG_CONFIGURATION_T Type

Defines the network security group configuration that allowed the traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_nsg_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`nsg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_NODE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_traffic_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_ROUTE_T Type

Defines the traffic route taken in the path in `PathAnalysisResult`.

Syntax
```

```

Fields

Field Description

`reachability_status`

(required) Reachability status for the given traffic route.

Allowed values are: 'REACHABLE', 'UNREACHABLE', 'INDETERMINATE'

`nodes`

(required) The ordered sequence of nodes in the given the traffic route forming a path.

`route_analysis_description`

(optional) A description of the traffic route analysis. For example: \"Traffic might not reach a destination due to the LB backend being unhealthy\".

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_TOPOLOGY_T Type

Defines the representation of a virtual network topology for path analysis.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_path_topology_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_T Type

Defines the configuration of the traffic path in `PathAnalysisResult`.

Syntax
```

```

Fields

Field Description

`forward_route`

(required)

`return_route`

(optional)

`topology`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_T Type

Ephemeral data resulting from an asynchronous operation.

Syntax
```

```

Fields

Field Description

`result_type`

(required) Type of `WorkRequestResult`.

Allowed values are: 'PATH_ANALYSIS'

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_path_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYSIS_WORK_REQUEST_RESULT_T Type

Defines the configuration of the path analysis result.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_path_analysis_work_request_result_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_work_request_result_t`type.

Fields

Field Description

`paths`

(required) List of various paths from source node to destination node for a given `PathAnalysisQuery`.

`time_created`

(required) Time the `PathAnalysisResult` was generated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_T Type

Defines the details saved in a `PathAnalyzerTest` resource. These configuration details are used to run a[Network Path Analyzer](https://docs.oracle.com/iaas/Content/Network/Concepts/path_analyzer.htm)analysis.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier established when the resource is created. The identifier can't be changed later.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PathAnalyzerTest` resource's compartment.

`protocol`

(required) The IP protocol to use for the `PathAnalyzerTest` resource.

`source_endpoint`

(required)

`destination_endpoint`

(required)

`protocol_parameters`

(optional)

`query_options`

(required)

`time_created`

(required) The date and time the `PathAnalyzerTest` resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(required) The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The current state of the `PathAnalyzerTest` resource.

Allowed values are: 'ACTIVE', 'DELETED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_SUMMARY_T Type

Defines the summary of a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier established when the resource is created. The identifier can't be changed later.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PathAnalyzerTest` resource's compartment.

`protocol`

(required) The IP protocol to use for the `PathAnalyzerTest` resource.

`source_endpoint`

(required)

`destination_endpoint`

(required)

`protocol_parameters`

(optional)

`query_options`

(required)

`time_created`

(required) The date and time the `PathAnalyzerTest` resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(required) The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The current state of the `PathAnalyzerTest` resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_path_analyzer_test_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_COLLECTION_T Type

The results of a `ListPathAnalyzerTests` call in the current compartment.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of `PathAnalyzerTestSummary` items.

### DBMS_CLOUD_OCI_VN_MONITORING_PERSISTED_GET_PATH_ANALYSIS_DETAILS_T Type

Defines the configuration for getting a path analysis using the persisted `PathAnalyzerTest` resource.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_persisted_get_path_analysis_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_get_path_analysis_details_t`type.

Fields

Field Description

`path_analyzer_test_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PathAnalyzerTest` resource.

### DBMS_CLOUD_OCI_VN_MONITORING_PRIVATE_IP_T Type

A *private IP* is a conceptual term that refers to an IPv4 private IP address and related properties. The `privateIp` object is the API representation of a private IP. **Note:** For information about IPv6 addresses, see`IPV6`Type. Each instance has a *primary private IP* that is automatically created and assigned to the primary VNIC during instance launch. If you add a secondary VNIC to the instance, it also automatically gets a primary private IP. You can't remove a primary private IP from its VNIC. The primary private IP is automatically deleted when the VNIC is terminated. You can add *secondary private IPs* to a VNIC after it's created. For more information, see the `privateIp` operations and also[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm). **Note:** Only`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function work with *primary* private IPs. To create and update primary private IPs, you instead work with instance and VNIC operations. For example, a primary private IP's properties come from the values you specify in`CREATE_VNIC_DETAILS`Type when calling either`LAUNCH_INSTANCE`Function or`ATTACH_VNIC`Function. To update the hostname for a primary private IP, you use`UPDATE_VNIC`Function. `PrivateIp` objects that are created for use with the Oracle Cloud VMware Solution are assigned to a VLAN and not a VNIC in a subnet. See the descriptions of the relevant attributes in the `PrivateIp` object. Also see`VLAN`Type. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The private IP's availability domain. This attribute will be null if this is a *secondary* private IP assigned to a VNIC that is in a *regional* subnet. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the private IP.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`id`

(optional) The private IP's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ip_address`

(optional) The private IP address of the `privateIp` object. The address is within the CIDR of the VNIC's subnet. However, if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution, the address is from the range specified by the `cidrBlock` attribute for the VLAN. See`VLAN`Type. Example: `10.0.3.3`

`is_primary`

(optional) Whether this private IP is the primary one on the VNIC. Primary private IPs are unassigned and deleted automatically when the VNIC is terminated. Example: `true`

`vlan_id`

(optional) Applicable only if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution. The `vlanId` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN. See`VLAN`Type.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the VNIC is in. However, if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution, the `subnetId` is null.

`time_created`

(optional) The date and time the private IP was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC the private IP is assigned to. The VNIC and private IP must be in the same subnet. However, if the `PrivateIp` object is being used with a VLAN as part of the Oracle Cloud VMware Solution, the `vnicId` is null.

### DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_T Type

A *public IP* is a conceptual term that refers to a public IP address and related properties. The `publicIp` object is the API representation of a public IP. There are two types of public IPs: 1. Ephemeral 2. Reserved For more information and comparison of the two types, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

Syntax
```

```

Fields

Field Description

`assigned_entity_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the entity the public IP is assigned to, or in the process of being assigned to.

`assigned_entity_type`

(optional) The type of entity the public IP is assigned to, or in the process of being assigned to.

Allowed values are: 'PRIVATE_IP', 'NAT_GATEWAY'

`availability_domain`

(optional) The public IP's availability domain. This property is set only for ephemeral public IPs that are assigned to a private IP (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value is the availability domain of the assigned private IP. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the public IP. For an ephemeral public IP, this is the compartment of its assigned entity (which can be a private IP or a regional entity such as a NAT gateway). For a reserved public IP that is currently assigned, its compartment can be different from the assigned private IP's.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(optional) The public IP's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ip_address`

(optional) The public IP address of the `publicIp` object. Example: `203.0.113.2`

`lifecycle_state`

(optional) The public IP's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ASSIGNING', 'ASSIGNED', 'UNASSIGNING', 'UNASSIGNED', 'TERMINATING', 'TERMINATED'

`lifetime`

(optional) Defines when the public IP is deleted and released back to Oracle's public IP pool. * `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned entity. An ephemeral public IP must always be assigned to an entity. If the assigned entity is a private IP, the ephemeral public IP is automatically deleted when the private IP is deleted, when the VNIC is terminated, or when the instance is terminated. If the assigned entity is a`NAT_GATEWAY`Type, the ephemeral public IP is automatically deleted when the NAT gateway is terminated. * `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP whenever you like. It does not need to be assigned to a private IP at all times. For more information and comparison of the two types, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

Allowed values are: 'EPHEMERAL', 'RESERVED'

`private_ip_id`

(optional) Deprecated. Use `assignedEntityId` instead. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP that the public IP is currently assigned to, or in the process of being assigned to. **Note:** This is `null` if the public IP is not assigned to a private IP, or is in the process of being assigned to one.

`scope`

(optional) Whether the public IP is regional or specific to a particular availability domain. * `REGION`: The public IP exists within a region and is assigned to a regional entity (such as a`NAT_GATEWAY`Type), or can be assigned to a private IP in any availability domain in the region. Reserved public IPs and ephemeral public IPs assigned to a regional entity have `scope` = `REGION`. * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity it's assigned to, which is specified by the `availabilityDomain` property of the public IP object. Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.

Allowed values are: 'REGION', 'AVAILABILITY_DOMAIN'

`time_created`

(optional) The date and time the public IP was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`public_ip_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pool object created in the current tenancy.

### DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_T Type

A public IP pool is a set of public IP addresses represented as one or more IPv4 CIDR blocks. Resources like load balancers and compute instances can be allocated public IP addresses from a public IP pool.

Syntax
```

```

Fields

Field Description

`cidr_blocks`

(optional) The CIDR blocks added to this pool. This could be all or a portion of a BYOIP CIDR block.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`lifecycle_state`

(optional) The public IP pool's current state.

Allowed values are: 'INACTIVE', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the public IP pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_SUMMARY_T Type

Summary information about a public IP pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the public IP pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`lifecycle_state`

(optional) The public IP pool's current state.

`time_created`

(optional) The date and time the public IP pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_public_ip_pool_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_COLLECTION_T Type

Results of a `ListPublicIpPool` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of public IP pool summaries.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOTE_PEERING_CONNECTION_T Type

A remote peering connection (RPC) is an object on a DRG that lets the VCN that is attached to the DRG peer with a VCN in a different region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the RPC.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG that this RPC belongs to.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the RPC.

`is_cross_tenancy_peering`

(required) Whether the VCN at the other end of the peering is in a different tenancy. Example: `false`

`lifecycle_state`

(required) The RPC's current lifecycle state.

Allowed values are: 'AVAILABLE', 'PROVISIONING', 'TERMINATING', 'TERMINATED'

`peer_id`

(optional) If this RPC is peered, this value is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the other RPC.

`peer_region_name`

(optional) If this RPC is peered, this value is the region that contains the other RPC. Example: `us-ashburn-1`

`peer_tenancy_id`

(optional) If this RPC is peered, this value is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the other RPC's tenancy.

`peering_status`

(required) Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been peered. `PENDING` means the peering is being established. `REVOKED` means the RPC at the other end of the peering has been deleted.

Allowed values are: 'INVALID', 'NEW', 'PENDING', 'PEERED', 'REVOKED'

`time_created`

(required) The date and time the RPC was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_REMOTE_PEERING_CONNECTION_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the DRG attachment to another DRG.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_remote_peering_connection_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_details_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to remove statements from a route distribution.

Syntax
```

```

Fields

Field Description

`statement_ids`

(optional) The Oracle-assigned ID of each route distribution to remove.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_DRG_ROUTE_RULES_DETAILS_T Type

Details used in a request to remove static routes from a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rule_ids`

(optional) The Oracle-assigned ID of each DRG route rule to be deleted.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rule_ids`

(optional) The Oracle-assigned ID of each`SECURITY_RULE`Type to be deleted.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type

The information needed to remove capacity from a public IP pool.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to remove from the public IP pool. Example: `10.0.1.0/24`

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_SUBNET_IPV6_CIDR_DETAILS_T Type

Details object for removing an IPv6 CIDR Block from a Subnet.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(required) This field is not required and should only be specified when removing an IPv6 CIDR from a subnet's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/64`

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_VCN_CIDR_DETAILS_T Type

Details for removing a CIDR block from a VCN.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to remove.

### DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_VCN_IPV6_CIDR_DETAILS_T Type

Details used when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix. You can only remove one of these per request.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(optional) This field is not required and should only be specified when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix from a VCN's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/56`

### DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_TABLE_T Type

A collection of `RouteRule` objects, which are used to route packets based on destination IP to a particular network entity. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the route table.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The route table's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The route table's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`route_rules`

(required) The collection of rules for routing destination IPs to network devices.

`time_created`

(optional) The date and time the route table was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the route table list belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_LIST_T Type

A set of virtual firewall rules for your VCN. Security lists are configured at the subnet level, but the rules are applied to the ingress and egress traffic for the individual instances in the subnet. The rules can be stateful or stateless. For more information, see[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). **Note:** Compare security lists to`NETWORK_SECURITY_GROUP`Types, which let you apply a set of security rules to a *specific set of VNICs* instead of an entire subnet. Oracle recommends using network security groups instead of security lists, although you can use either or both together. **Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure both the security lists associated with the instance's subnet and the instance's firewall rules are set correctly. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the security list.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(required) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The security list's Oracle Cloud ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ingress_security_rules`

(required) Rules for allowing ingress IP packets.

`lifecycle_state`

(required) The security list's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(required) The date and time the security list was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the security list belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_T Type

An object that represents one or multiple Oracle services that you can enable for a`SERVICE_GATEWAY`Type. In the User Guide topic[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm), the term *service CIDR label* is used to refer to the string that represents the regional public IP address ranges of the Oracle service or services covered by a given `Service` object. That unique string is the value of the `Service` object's `cidrBlock` attribute.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) A string that represents the regional public IP address ranges for the Oracle service or services covered by this `Service` object. Also known as the `Service` object's *service CIDR label*. When you set up a route rule to route traffic to the service gateway, use this value as the rule's destination. See`ROUTE_TABLE`Type. Also, when you set up a security list rule to cover traffic with the service gateway, use the `cidrBlock` value as the rule's destination (for an egress rule) or the source (for an ingress rule). See`SECURITY_LIST`Type. Example: `oci-phx-objectstorage`

`description`

(required) Description of the Oracle service or services covered by this `Service` object. Example: `OCI PHX Object Storage`

`id`

(required) The `Service` object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) Name of the `Service` object. This name can change and is not guaranteed to be unique. Example: `OCI PHX Object Storage`

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_RESPONSE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service.

`service_name`

(required) The name of the service.

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_RESPONSE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_service_id_response_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_GATEWAY_T Type

Represents a router that lets your VCN privately access specific Oracle services such as Object Storage without exposing the VCN to the public internet. Traffic leaving the VCN and destined for a supported Oracle service (see`LIST_SERVICES`Function) is routed through the service gateway and does not traverse the internet. The instances in the VCN do not need to have public IP addresses nor be in a public subnet. The VCN does not need an internet gateway for this traffic. For more information, see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`block_traffic`

(required) Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules. Example: `true`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the service gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service gateway.

`lifecycle_state`

(required) The service gateway's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the service gateway is using. For information about why you would associate a route table with a service gateway, see[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

`services`

(required) List of the`SERVICE`Type objects enabled for this service gateway. The list can be empty. You can enable a particular `Service` by using`ATTACH_SERVICE_ID`Function or`UPDATE_SERVICE_GATEWAY`Function.

`time_created`

(optional) The date and time the service gateway was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the service gateway belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_EGRESS_SECURITY_LIST_CONFIGURATION_T Type

Defines the stateful subnet egress security list configuration that allowed the ingress traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_stateful_egress_security_list_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_INGRESS_SECURITY_LIST_CONFIGURATION_T Type

Defines the stateful subnet ingress security list configuration that allowed the egress traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_stateful_ingress_security_list_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_NSG_CONFIGURATION_T Type

Defines the stateful network security group configuration that allowed the traffic.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_stateful_nsg_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_allowed_security_configuration_t`type.

Fields

Field Description

`nsg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group that allowed the traffic.

`security_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_T Type

A logical subdivision of a VCN. Each subnet consists of a contiguous range of IP addresses that do not overlap with other subnets in the VCN. Example: 172.16.1.0/24. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)and[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The subnet's availability domain. This attribute will be null if this is a regional subnet instead of an AD-specific subnet. Oracle recommends creating regional subnets. Example: `Uocm:PHX-AD-1`

`cidr_block`

(required) The subnet's CIDR block. Example: `10.0.1.0/24`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the subnet.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options that the subnet uses.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed. The absence of this parameter means the Internet and VCN Resolver will not resolve hostnames of instances in this subnet. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `subnet123`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The subnet's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ipv6_cidr_block`

(optional) For an IPv6-enabled subnet, this is the IPv6 CIDR block for the subnet's IP address space. The subnet size is always /64. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 CIDR blocks (Oracle allocated IPv6 GUA, ULA or private IPv6 CIDR blocks, BYOIPv6 CIDR blocks) for the subnet.

`ipv6_virtual_router_ip`

(optional) For an IPv6-enabled subnet, this is the IPv6 address of the virtual router. Example: `2001:0db8:0123:1111:89ab:cdef:1234:5678`

`lifecycle_state`

(required) The subnet's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING'

`prohibit_internet_ingress`

(optional) Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false. For IPV4, `prohibitInternetIngress` behaves similarly to `prohibitPublicIpOnVnic`. If it is set to false, VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in`CREATE_VNIC_DETAILS`Type). If `prohibitInternetIngress` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a privatesubnet). For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default. Example: `true`

`prohibit_public_ip_on_vnic`

(optional) Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in`CREATE_VNIC_DETAILS`Type). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet). Example: `true`

`route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that the subnet uses.

`security_list_ids`

(optional) The OCIDs of the security list or lists that the subnet uses. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`subnet_domain_name`

(optional) The subnet's domain name, which consists of the subnet's DNS label, the VCN's DNS label, and the `oraclevcn.com` domain. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `subnet123.vcn1.oraclevcn.com`

`time_created`

(optional) The date and time the subnet was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the subnet is in.

`virtual_router_ip`

(required) The IP address of the virtual router. Example: `10.0.14.1`

`virtual_router_mac`

(required) The MAC address of the virtual router. Example: `00:00:00:00:00:01`

### DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_ENDPOINT_T Type

Defines the details required for a SUBNET-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_subnet_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`address`

(required) The IPv4 address of the `Endpoint`.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet containing the IP address. This can be used to disambiguate which subnet is intended, in case the IP address is used in more than one subnet (when there are subnets with overlapping IP ranges).

### DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_TOPOLOGY_T Type

Defines the visualization of a subnet in a VCN.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_subnet_topology_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_t`type.

Fields

Field Description

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet for which the visualization is generated.

### DBMS_CLOUD_OCI_VN_MONITORING_TCP_PROTOCOL_PARAMETERS_T Type

Defines the configuration for TCP protocol parameters.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_tcp_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_protocol_parameters_t`type.

Fields

Field Description

`source_port`

(optional) The source port to use in a `PathAnalyzerTest` resource.

`destination_port`

(required) The destination port to use in a `PathAnalyzerTest` resource.

### DBMS_CLOUD_OCI_VN_MONITORING_TCP_TRAFFIC_PROTOCOL_PARAMETERS_T Type

Defines the `TrafficProtocolParameters` configuration for the TCP protocol.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_tcp_traffic_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_traffic_protocol_parameters_t`type.

Fields

Field Description

`source_port`

(optional) The source port to use in a `PathAnalyzerTest`.

`destination_port`

(required) The destination port to use in a `PathAnalyzerTest`.

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ASSOCIATED_WITH_RELATIONSHIP_DETAILS_T Type

Defines association details for an `associatedWith` relationship.

Syntax
```

```

Fields

Field Description

`via`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the entities via which the relationship is created. For example an instance is associated with a network security group via the VNIC attachment and the VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ASSOCIATED_WITH_ENTITY_RELATIONSHIP_T Type

Defines the `AssociatedWith` relationship between virtual network topology entities. An `AssociatedWith` relationship is defined when there is no obvious `contains` relationship but entities are still related. For example, a DRG is associated with a VCN because a DRG is not managed by VCN but can be attached to a VCN.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_topology_associated_with_entity_relationship_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_entity_relationship_t`type.

Fields

Field Description

`associated_with_details`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_CONTAINS_ENTITY_RELATIONSHIP_T Type

Defines the `contains` relationship between virtual network topology entities. A `Contains` relationship is defined when an entity fully owns, contains or manages another entity. For example, a subnet is contained and managed in the scope of a VCN, therefore a VCN has a `contains` relationship to a subnet.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_topology_contains_entity_relationship_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_entity_relationship_t`type.

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ROUTES_TO_RELATIONSHIP_DETAILS_T Type

Defines route rule details for a `routesTo` relationship.

Syntax
```

```

Fields

Field Description

`destination_type`

(required) The destinationType can be set to one of two values: * Use `CIDR_BLOCK` if the rule's `destination` is an IP address range in CIDR notation. * Use `SERVICE_CIDR_BLOCK` if the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type.

`destination`

(required) An IP address range in CIDR notation or the `cidrBlock` value for a`SERVICE`Type.

`route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the routing table that contains the route rule.

`route_type`

(optional) A route rule can be `STATIC` if manually added to the route table or `DYNAMIC` if imported from another route table.

Allowed values are: 'STATIC', 'DYNAMIC'

### DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ROUTES_TO_ENTITY_RELATIONSHIP_T Type

Defines the `routesTo` relationship between virtual network topology entities. A `RoutesTo` relationship is defined when a routing table and a routing rule are used to govern how to route traffic from one entity to another. For example, a DRG might have a routing rule to send certain traffic to an LPG.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_topology_routes_to_entity_relationship_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_entity_relationship_t`type.

Fields

Field Description

`route_rule_details`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_ANSWER_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_cpe_device_config_answer_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CPE_DEVICE_CONFIG_T Type

The set of CPE configuration answers for the tunnel, which the customer provides in`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of`CPE_DEVICE_SHAPE_DETAIL`Type). See these related operations: *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_CPE_DEVICE_CONFIG_CONTENT`Function

Syntax
```

```

Fields

Field Description

`tunnel_cpe_device_config_parameter`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_ROUTE_SUMMARY_T Type

A summary of the routes advertised to and received from the on-premises network.

Syntax
```

```

Fields

Field Description

`prefix`

(optional) The BGP network layer reachability information.

`age`

(optional) The age of the route.

`is_best_path`

(optional) Indicates this is the best route.

`as_path`

(optional) A list of ASNs in AS_Path.

`advertiser`

(optional) The source of the route advertisement.

Allowed values are: 'CUSTOMER', 'ORACLE'

### DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_SECURITY_ASSOCIATION_SUMMARY_T Type

A summary of the IPSec tunnel security association details.

Syntax
```

```

Fields

Field Description

`cpe_subnet`

(optional) The IP address and mask of the partner subnet used in policy based VPNs or static routes.

`oracle_subnet`

(optional) The IP address and mask of the local subnet used in policy based VPNs or static routes.

`tunnel_sa_status`

(optional) The IPSec tunnel's phase one status.

Allowed values are: 'INITIATING', 'LISTENING', 'UP', 'DOWN', 'ERROR', 'UNKNOWN'

`tunnel_sa_error_info`

(optional) Current state if the IPSec tunnel status is not `UP`, including phase one and phase two details and a possible reason the tunnel is not `UP`.

`time`

(optional) Time in the current state, in seconds.

### DBMS_CLOUD_OCI_VN_MONITORING_UDP_PROTOCOL_PARAMETERS_T Type

Defines the configuration for UDP protocol parameters.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_udp_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_protocol_parameters_t`type.

Fields

Field Description

`source_port`

(optional) The source port to use in a `PathAnalyzerTest` resource.

`destination_port`

(required) The destination port to use in a `PathAnalyzerTest` resource.

### DBMS_CLOUD_OCI_VN_MONITORING_UDP_TRAFFIC_PROTOCOL_PARAMETERS_T Type

Defines the `TrafficProtocolParameters` configuration for the UDP protocol.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_udp_traffic_protocol_parameters_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_traffic_protocol_parameters_t`type.

Fields

Field Description

`source_port`

(optional) The source port to use in a `PathAnalyzerTest`.

`destination_port`

(required) The destination port to use in a `PathAnalyzerTest`.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_BYOIP_RANGE_DETAILS_T Type

The information used to update a `ByoipRange` resource.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CAPTURE_FILTER_DETAILS_T Type

These details can be included in a request to update a capture filter. A capture filter contains a set of rules governing what traffic a VTAP mirrors.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`vtap_capture_filter_rules`

(optional) The set of rules governing what traffic a VTAP mirrors.

`flow_log_capture_filter_rules`

(optional) The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CPE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device type. You can provide a value if you want to generate CPE device configuration content for IPSec connections that use this CPE. For a list of possible values, see`LIST_CPE_DEVICE_SHAPES`Function. For more information about generating CPE device configuration content, see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_MACSEC_KEY_T Type

An object defining the OCID of the Secret held in Vault that represent the MACsec key.

Syntax
```

```

Fields

Field Description

`connectivity_association_name_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity Association Key Name (CKN) of this MACsec key.

`connectivity_association_name_secret_version`

(required) The secret version of the connectivity association name secret in Vault.

`connectivity_association_key_secret_id`

(required) Secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)containing the Connectivity Association Key (CAK) of this MACsec key.

`connectivity_association_key_secret_version`

(required) The secret version of the connectivityAssociationKey secret in Vault.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_MACSEC_PROPERTIES_T Type

Properties used to update MACsec settings.

Syntax
```

```

Fields

Field Description

`state`

(required) Indicates whether or not MACsec is enabled.

Allowed values are: 'ENABLED', 'DISABLED'

`primary_key`

(optional)

`encryption_cipher`

(optional) Type of encryption cipher suite to use for the MACsec connection.

Allowed values are: 'AES128_GCM', 'AES128_GCM_XPN', 'AES256_GCM', 'AES256_GCM_XPN'

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CROSS_CONNECT_DETAILS_T Type

Update a CrossConnect

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`is_active`

(optional) Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready. Example: `true`

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection this cross-connect uses.

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CROSS_CONNECT_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection this cross-connect group uses.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DHCP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`options`

(optional)

`domain_name_type`

(optional) The search domain name type of DHCP options

Allowed values are: 'SUBNET_DOMAIN', 'VCN_DOMAIN', 'CUSTOM_DOMAIN'

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ATTACHMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table that is assigned to this attachment. The DRG route table manages traffic inside the DRG. You can't remove a DRG route table from a DRG attachment, but you can reassign which DRG route table it uses.

`network_details`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`export_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export route distribution used to specify how routes in the assigned DRG route table are advertised out through the attachment. If this value is null, no routes are advertised through this attachment.

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`default_drg_route_tables`

(optional)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type

Details used in a request to update a route distribution. You cannot assign a table to a virtual circuit or IPSec tunnel attachment if there is a static route rule for an RPC attachment.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type

Route distribution statements to update in the route distribution.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle-assigned ID of each route distribution statement to be updated.

`match_criteria`

(optional) The action is applied only if all of the match criteria is met.

`priority`

(optional) The priority of the statement you'd like to update.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_update_drg_route_distribution_statement_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to update statements in a route distribution.

Syntax
```

```

Fields

Field Description

`statements`

(required) The route distribution statements to update, and the details to be updated.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULE_DETAILS_T Type

Details used to update a route rule in the DRG route table.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle-assigned ID of each DRG route rule to update.

`destination`

(optional) The range of IP addresses used for matching when routing traffic. Potential values: * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.

`destination_type`

(optional) Type of destination for the rule. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

Allowed values are: 'CIDR_BLOCK'

`next_hop_drg_attachment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_update_drg_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULES_DETAILS_T Type

Details used to update route rules in a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rules`

(optional) The DRG rute rules to update.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_TABLE_DETAILS_T Type

Details used in a request to update a DRG route table. You can't assign a table to a virtual circuit or IPSec tunnel attachment if there is a static route rule for an RPC attachment.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements through referenced attachements are inserted into the DRG route table.

`is_ecmp_enabled`

(optional) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-prem networks, set this value to true on the route table.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`cpe_local_identifier`

(optional) Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`. For information about why you'd provide this value, see[If Your CPE Is Behind a NAT Device](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat). Example IP address: `10.0.3.3` Example hostname: `cpe.example.com`

`cpe_local_identifier_type`

(optional) The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.

Allowed values are: 'IP_ADDRESS', 'HOSTNAME'

`static_routes`

(optional) Static routes to the CPE. If you provide this attribute, it replaces the entire current set of static routes. A static route's CIDR must not be a multicast address or class E address. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `10.0.1.0/24` Example: `2001:db8::/32`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`oracle_interface_ip`

(optional) The IP address for the Oracle end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS`Function), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. The value must be a /30 or /31. If you are switching the tunnel from using BGP dynamic routing to static routing and want to remove the value for `oracleInterfaceIp`, you can set the value to an empty string. Example: `10.0.0.4/31`

`customer_interface_ip`

(optional) The IP address for the CPE end of the inside tunnel interface. If the tunnel's `routing` attribute is set to `BGP` (see`UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS`Function), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. The value must be a /30 or /31. If you are switching the tunnel from using BGP dynamic routing to static routing and want to remove the value for `customerInterfaceIp`, you can set the value to an empty string. Example: `10.0.0.5/31`

`oracle_interface_ipv6`

(optional) The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`customer_interface_ipv6`

(optional) The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional. If the tunnel's `routing` attribute is set to `BGP` (see`IP_SEC_CONNECTION_TUNNEL`Type), this IP address is used for the tunnel's BGP session. If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel. Only subnet masks from /64 up to /127 are allowed. Example: `2001:db8::1/64`

`customer_bgp_asn`

(optional) The BGP ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format. If you are switching the tunnel from using BGP dynamic routing to static routing, the `customerBgpAsn` must be null. Example: `12345` (2-byte) or `1587232876` (4-byte)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type

Request to update a multi-encryption domain policy on the IPSec tunnel. There can't be more than 50 security associations in use at one time. See[Encryption domain for policy-based tunnels](https://docs.oracle.com/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for more.

Syntax
```

```

Fields

Field Description

`oracle_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.

`cpe_traffic_selector`

(optional) Lists IPv4 or IPv6-enabled subnets in your on-premises network.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`routing`

(optional) The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).

Allowed values are: 'BGP', 'STATIC', 'POLICY'

`ike_version`

(optional) Internet Key Exchange protocol version.

Allowed values are: 'V1', 'V2'

`bgp_session_config`

(optional)

`oracle_initiation`

(optional) Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.

Allowed values are: 'INITIATOR_OR_RESPONDER', 'RESPONDER_ONLY'

`nat_translation_enabled`

(optional) By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500, and when it detects that the port used to forward packets has changed (most likely because a NAT device is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T. The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets. The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T even if it senses there may be a NAT device in use.

Allowed values are: 'ENABLED', 'DISABLED', 'AUTO'

`phase_one_config`

(optional)

`phase_two_config`

(optional)

`dpd_config`

(optional)

`encryption_domain_config`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`shared_secret`

(optional) The shared secret (pre-shared key) to use for the tunnel. Only numbers, letters, and spaces are allowed.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_INTERNET_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`is_enabled`

(optional) Whether the gateway is enabled.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the Internet Gateway is using.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IPV6_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to reassign the IPv6 to. The VNIC must be in the same subnet as the current VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the LPG will use. For information about why you would associate a route table with an LPG, see[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NAT_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`block_traffic`

(optional) Whether the NAT gateway blocks traffic through it. The default is `false`. Example: `true`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the NAT gateway. If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NETWORK_SECURITY_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_RULE_DETAILS_T Type

A rule for allowing inbound (`direction`= INGRESS) or outbound (`direction`= EGRESS) IP packets.

Syntax
```

```

Fields

Field Description

`description`

(optional) An optional description of your choice for the rule. Avoid entering confidential information.

`destination`

(optional) Conceptually, this is the range of IP addresses that a packet originating from the instance can go to. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`destination_type`

(optional) Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic destined for a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`direction`

(required) Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

Allowed values are: 'EGRESS', 'INGRESS'

`icmp_options`

(optional)

`id`

(required) The Oracle-assigned ID of the security rule that you want to update. You can't change this value. Example: `04ABEC`

`is_stateless`

(optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`protocol`

(required) The transport protocol. Specify either `all` or an IPv4 protocol number as defined in[Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

`source`

(optional) Conceptually, this is the range of IP addresses that a packet coming into the instance can come from. Allowed values: * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56` IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`. * The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type in the same VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control traffic between VNICs in the same NSG.

`source_type`

(optional) Type of source for the rule. Required if `direction` = `INGRESS`. * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation. * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a`SERVICE`Type (the rule is for traffic coming from a particular `Service` through a service gateway). * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a`NETWORK_SECURITY_GROUP`Type.

Allowed values are: 'CIDR_BLOCK', 'SERVICE_CIDR_BLOCK', 'NETWORK_SECURITY_GROUP'

`tcp_options`

(optional)

`udp_options`

(optional)

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_update_security_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules to update.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PATH_ANALYZER_TEST_DETAILS_T Type

Details to update a `PathAnalyzerTest` resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`protocol`

(optional) The IP protocol to use in the `PathAnalyzerTest` resource.

`source_endpoint`

(optional)

`destination_endpoint`

(optional)

`protocol_parameters`

(optional)

`query_options`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PRIVATE_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to reassign the private IP to. The VNIC must be in the same subnet as the current VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PUBLIC_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`private_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP to assign the public IP to. * If the public IP is already assigned to a different private IP, it will be unassigned and then reassigned to the specified private IP. * If you set this field to an empty string, the public IP will be unassigned from the private IP it is currently assigned to.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PUBLIC_IP_POOL_DETAILS_T Type

The data to update for a public IP pool.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_ROUTE_TABLE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_rules`

(optional) The collection of rules used for routing destination IPs to network devices.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_LIST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(optional) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`ingress_security_rules`

(optional) Rules for allowing ingress IP packets.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SERVICE_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`block_traffic`

(optional) Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules. Example: `true`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the service gateway will use. For information about why you would associate a route table with a service gateway, see[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

`services`

(optional) List of all the `Service` objects you want enabled on this service gateway. Sending an empty list means you want to disable all services. Omitting this parameter entirely keeps the existing list of services intact. You can also enable or disable a particular `Service` by using`ATTACH_SERVICE_ID`Function or`DETACH_SERVICE_ID`Function. For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See`ROUTE_TABLE`Type.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SUBNET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options the subnet will use.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the subnet will use.

`security_list_ids`

(optional) The OCIDs of the security list or lists the subnet will use. This replaces the entire current set of security lists. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`cidr_block`

(optional) The CIDR block of the subnet. The new CIDR block must meet the following criteria: - Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range. **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress. Example: `172.16.0.0/16`

`ipv6_cidr_block`

(optional) This is the IPv6 CIDR block for the subnet's IP address space. The subnet size is always /64. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). The provided CIDR must maintain the following rules - a. The IPv6 CIDR block is valid and correctly formatted. b. The IPv6 CIDR is within the parent VCN IPv6 range. Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 CIDR blocks (Oracle allocated IPv6 GUA, ULA or private IPv6 CIDR blocks, BYOIPv6 CIDR blocks) for the subnet that meets the following criteria: - The CIDR blocks must be valid. - Multiple CIDR blocks must not overlap each other or the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of IPv6 CIDR blocks allowed to a subnet.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_TUNNEL_CPE_DEVICE_CONFIG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`tunnel_cpe_device_config`

(optional) The set of configuration answers for a CPE device.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VCN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VIRTUAL_CIRCUIT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`bandwidth_shape_name`

(optional) The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see`LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES`Function. To be updated only by the customer who owns the virtual circuit.

`cross_connect_mappings`

(optional) An array of mappings, each containing properties for a cross-connect or cross-connect group associated with this virtual circuit. The customer and provider can update different properties in the mapping depending on the situation. See the description of the`CROSS_CONNECT_MAPPING`Type.

`routing_policy`

(optional) The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit. Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`. See[Route Filtering](https://docs.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)for details. By default, routing information is shared for all routes in the same market.

Allowed values are: 'ORACLE_SERVICE_NETWORK', 'REGIONAL', 'MARKET_LEVEL', 'GLOBAL'

`bgp_admin_state`

(optional) Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.

Allowed values are: 'ENABLED', 'DISABLED'

`is_bfd_enabled`

(optional) Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.

`is_transport_mode`

(optional) Set to `true` for the virtual circuit to carry only encrypted traffic, or set to `false` for the virtual circuit to carry unencrypted traffic. If this is not set, the default is `false`.

`customer_bgp_asn`

(optional) Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.

`customer_asn`

(optional) The BGP ASN of the network at the other end of the BGP session from Oracle. If the BGP session is from the customer's edge router to Oracle, the required value is the customer's ASN, and it can be updated only by the customer. If the BGP session is from the provider's edge router to Oracle, the required value is the provider's ASN, and it can be updated only by the provider. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`gateway_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`DRG`Type that this private virtual circuit uses. To be updated only by the customer who owns the virtual circuit.

`provider_state`

(optional) The provider's state in relation to this virtual circuit. Relevant only if the customer is using FastConnect via a provider. ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it. To be updated only by the provider.

Allowed values are: 'ACTIVE', 'INACTIVE'

`provider_service_key_name`

(optional) The service key name offered by the provider (if the customer is connecting via a provider).

`reference_comment`

(optional) Provider-supplied reference information about this virtual circuit. Relevant only if the customer is using FastConnect via a provider. To be updated only by the provider.

`ip_mtu`

(optional) The layer 3 IP MTU to use on this virtual circuit.

Allowed values are: 'MTU_1500', 'MTU_9000'

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VLAN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to use with this VLAN. All VNICs in the VLAN will belong to these NSGs. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the VLAN will use.

`cidr_block`

(optional) The CIDR block of the VLAN. The new CIDR block must meet the following criteria: - Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range. **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VNIC_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as an empty array removes the VNIC from all network security groups. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the VNIC belongs to the NSGs that are associated with the VLAN itself. See`VLAN`Type. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip). If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `skipSourceDestCheck` attribute is ignored. This is because the source/destination check is always disabled for VNICs in a VLAN. Example: `true`

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VTAP_DETAILS_T Type

These details can be included in a request to update a virtual test access point (VTAP).

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source point where packets are captured.

`target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination resource where mirrored packets are sent.

`target_ip`

(optional) The IP address of the destination resource where mirrored packets are sent.

`capture_filter_id`

(optional) The capture filter's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`encapsulation_protocol`

(optional) Defines an encapsulation header type for the VTAP's mirrored traffic.

Allowed values are: 'VXLAN'

`vxlan_network_identifier`

(optional) The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.

`is_vtap_enabled`

(optional) Used to start or stop a `Vtap` resource. * `TRUE` directs the VTAP to start mirroring traffic. * `FALSE` (Default) directs the VTAP to stop mirroring traffic.

`traffic_mode`

(optional) Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT

Allowed values are: 'DEFAULT', 'PRIORITY'

`max_packet_size`

(optional) The maximum size of the packets to be included in the filter.

`source_private_endpoint_ip`

(optional) The IP Address of the source private endpoint.

`source_private_endpoint_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that source private endpoint belongs to.

`target_type`

(optional) The target type for the VTAP.

Allowed values are: 'VNIC', 'NETWORK_LOAD_BALANCER', 'IP_ADDRESS'

`source_type`

(optional) The source type for the VTAP.

Allowed values are: 'VNIC', 'SUBNET', 'LOAD_BALANCER', 'DB_SYSTEM', 'EXADATA_VM_CLUSTER', 'AUTONOMOUS_DATA_WAREHOUSE'

### DBMS_CLOUD_OCI_VN_MONITORING_UPDATED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules that were updated.

### DBMS_CLOUD_OCI_VN_MONITORING_UPGRADE_STATUS_T Type

The upgrade status of a DRG.

Syntax
```

```

Fields

Field Description

`drg_id`

(required) The `drgId` of the upgraded DRG.

`status`

(required) The current upgrade status of the DRG attachment.

Allowed values are: 'NOT_UPGRADED', 'IN_PROGRESS', 'UPGRADED'

`upgraded_connections`

(required) The number of upgraded connections.

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_T Type

A virtual cloud network (VCN). For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`byoipv6_cidr_blocks`

(optional) The list of BYOIPv6 CIDR blocks required to create a VCN that uses BYOIPv6 ranges.

`ipv6_private_cidr_blocks`

(optional) For an IPv6-enabled VCN, this is the list of Private IPv6 CIDR blocks for the VCN's IP address space.

`cidr_block`

(required) Deprecated. The first CIDR IP address from cidrBlocks. Example: `172.16.0.0/16`

`cidr_blocks`

(required) The list of IPv4 CIDR blocks the VCN will use.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the VCN.

`default_dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the VCN's default set of DHCP options.

`default_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the VCN's default route table.

`default_security_list_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the VCN's default security list.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter. The value cannot be changed. The absence of this parameter means the Internet and VCN Resolver will not work for this VCN. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The VCN's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ipv6_cidr_blocks`

(optional) For an IPv6-enabled VCN, this is the list of IPv6 CIDR blocks for the VCN's IP address space. The CIDRs are provided by Oracle and the sizes are always /56.

`lifecycle_state`

(required) The VCN's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING'

`time_created`

(optional) The date and time the VCN was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_domain_name`

(optional) The VCN's domain name, which consists of the VCN's DNS label, and the `oraclevcn.com` domain. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1.oraclevcn.com`

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_DNS_RESOLVER_ASSOCIATION_T Type

The information about the VCN and the DNS resolver in the association.

Syntax
```

```

Fields

Field Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN in the association.

`dns_resolver_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DNS resolver in the association.

`lifecycle_state`

(required) The current state of the association.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type

Specifies the VCN Attachment

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vcn_drg_attachment_network_create_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_create_details_t`type.

Fields

Field Description

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see[Advanced Scenario: Transit Routing](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm). For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies details within the VCN.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vcn_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_details_t`type.

Fields

Field Description

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the DRG attachment is using. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

Allowed values are: 'VCN_CIDRS', 'SUBNET_CIDRS'

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type

Specifies the update details for the VCN attachment.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vcn_drg_attachment_network_update_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_update_details_t`type.

Fields

Field Description

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_ROUTING_CONFIGURATION_T Type

Identifies the VCN route table and rule that allowed the traffic to be forwarded.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vcn_routing_configuration_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_forwarded_routing_configuration_t`type.

Fields

Field Description

`vcn_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN route table that allowed the traffic.

`route_rule`

(required)

### DBMS_CLOUD_OCI_VN_MONITORING_VCN_TOPOLOGY_T Type

Defines the representation of a virtual network topology for a VCN.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vcn_topology_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_topology_t`type.

Fields

Field Description

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for which the topology is generated.

### DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_T Type

For use with Oracle Cloud Infrastructure FastConnect. A virtual circuit is an isolated network path that runs over one or more physical network connections to provide a single, logical connection between the edge router on the customer's existing network and Oracle Cloud Infrastructure. *Private* virtual circuits support private peering, and *public* virtual circuits support public peering. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). Each virtual circuit is made up of information shared between a customer, Oracle, and a provider (if the customer is using FastConnect via a provider). Who fills in a given property of a virtual circuit depends on whether the BGP session related to that virtual circuit goes from the customer's edge router to Oracle, or from the provider's edge router to Oracle. Also, in the case where the customer is using a provider, values for some of the properties may not be present immediately, but may get filled in as the provider and Oracle each do their part to provision the virtual circuit. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`bandwidth_shape_name`

(optional) The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see`LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES`Function. Example: `10 Gbps`

`bgp_management`

(optional) Deprecated. Instead use the information in`FAST_CONNECT_PROVIDER_SERVICE`Type.

Allowed values are: 'CUSTOMER_MANAGED', 'PROVIDER_MANAGED', 'ORACLE_MANAGED'

`bgp_session_state`

(optional) The state of the Ipv4 BGP session associated with the virtual circuit.

Allowed values are: 'UP', 'DOWN'

`bgp_ipv6_session_state`

(optional) The state of the Ipv6 BGP session associated with the virtual circuit.

Allowed values are: 'UP', 'DOWN'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the virtual circuit.

`cross_connect_mappings`

(optional) An array of mappings, each containing properties for a cross-connect or cross-connect group that is associated with this virtual circuit.

`routing_policy`

(optional) The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit. Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`. See[Route Filtering](https://docs.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)for details. By default, routing information is shared for all routes in the same market.

Allowed values are: 'ORACLE_SERVICE_NETWORK', 'REGIONAL', 'MARKET_LEVEL', 'GLOBAL'

`bgp_admin_state`

(optional) Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.

Allowed values are: 'ENABLED', 'DISABLED'

`is_bfd_enabled`

(optional) Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.

`is_transport_mode`

(optional) Set to `true` for the virtual circuit to carry only encrypted traffic, or set to `false` for the virtual circuit to carry unencrypted traffic. If this is not set, the default is `false`.

`customer_bgp_asn`

(optional) Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.

`customer_asn`

(optional) The BGP ASN of the network at the other end of the BGP session from Oracle. If the session is between the customer's edge router and Oracle, the value is the customer's ASN. If the BGP session is between the provider's edge router and Oracle, the value is the provider's ASN. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`gateway_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the customer's`DRG`Type that this virtual circuit uses. Applicable only to private virtual circuits.

`id`

(optional) The virtual circuit's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(optional) The virtual circuit's current state. For information about the different states, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Allowed values are: 'PENDING_PROVIDER', 'VERIFYING', 'PROVISIONING', 'PROVISIONED', 'FAILED', 'INACTIVE', 'TERMINATING', 'TERMINATED'

`oracle_bgp_asn`

(optional) The Oracle BGP ASN.

`provider_name`

(optional) Deprecated. Instead use `providerServiceId`.

`provider_service_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service offered by the provider (if the customer is connecting via a provider).

`provider_service_key_name`

(optional) The service key name offered by the provider (if the customer is connecting via a provider).

`provider_service_name`

(optional) Deprecated. Instead use `providerServiceId`.

`provider_state`

(optional) The provider's state in relation to this virtual circuit (if the customer is connecting via a provider). ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.

Allowed values are: 'ACTIVE', 'INACTIVE'

`public_prefixes`

(optional) For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection. All prefix sizes are allowed.

`reference_comment`

(optional) Provider-supplied reference information about this virtual circuit (if the customer is connecting via a provider).

`l_region`

(optional) The Oracle Cloud Infrastructure region where this virtual circuit is located.

`service_type`

(optional) Provider service type.

Allowed values are: 'COLOCATED', 'LAYER2', 'LAYER3'

`time_created`

(optional) The date and time the virtual circuit was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`l_type`

(optional) Whether the virtual circuit supports private or public peering. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Allowed values are: 'PUBLIC', 'PRIVATE'

`ip_mtu`

(optional) The layer 3 IP MTU to use on this virtual circuit.

Allowed values are: 'MTU_1500', 'MTU_9000'

### DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNEL_DETAILS_T Type

Detailed private tunnel info associated with the virtual circuit.

Syntax
```

```

Fields

Field Description

`tunnel_type`

(required) The type of the tunnel associated with the virtual circuit.

Allowed values are: 'IPSEC'

`ipsec_connection_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of IPSec connection associated with the virtual circuit.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec tunnel associated with the virtual circuit.

### DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPE_T Type

An individual bandwidth level for virtual circuits.

Syntax
```

```

Fields

Field Description

`bandwidth_in_mbps`

(optional) The bandwidth in Mbps. Example: `10000`

`name`

(required) The name of the bandwidth shape. Example: `10 Gbps`

### DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the virtual circuit attached to the DRG.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_virtual_circuit_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_drg_attachment_network_details_t`type.

Fields

Field Description

`transport_only_mode`

(optional) Boolean flag that determines wether all traffic over the virtual circuits is encrypted. Example: `true`

### DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_T Type

A public IP prefix and its details. With a public virtual circuit, the customer specifies the customer-owned public IP prefixes to advertise across the connection. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) Publix IP prefix (CIDR) that the customer specified.

`verification_state`

(required) Oracle must verify that the customer owns the public IP prefix before traffic for that prefix can flow across the virtual circuit. Verification can take a few business days. `IN_PROGRESS` means Oracle is verifying the prefix. `COMPLETED` means verification succeeded. `FAILED` means verification failed and traffic for this prefix will not flow across the connection.

Allowed values are: 'IN_PROGRESS', 'COMPLETED', 'FAILED'

### DBMS_CLOUD_OCI_VN_MONITORING_VISIBLE_TRAFFIC_NODE_T Type

Defines the configuration of a traffic node that is visible to the user.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_visible_traffic_node_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_traffic_node_t`type.

Fields

Field Description

`entity_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI entity that represents the traffic node (Instance, GW, LB, etc.).

`transformation_description`

(optional) Describes how the traffic was transformed. For example, if an address is translated by a NAT GW, the string will describe the translation: 'SNAT: 10.0.0.1-&gt;204.0.0.1'

### DBMS_CLOUD_OCI_VN_MONITORING_VLAN_T Type

A resource to be used only with the Oracle Cloud VMware Solution. Conceptually, a virtual LAN (VLAN) is a broadcast domain that is created by partitioning and isolating a network at the data link layer (a *layer 2 network*). VLANs work by using IEEE 802.1Q VLAN tags. Layer 2 traffic is forwarded within the VLAN based on MAC learning. In the Networking service, a VLAN is an object within a VCN. You use VLANs to partition the VCN at the data link layer (layer 2). A VLAN is analagous to a subnet, which is an object for partitioning the VCN at the IP layer (layer 3).

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The VLAN's availability domain. This attribute will be null if this is a regional VLAN rather than an AD-specific VLAN. Example: `Uocm:PHX-AD-1`

`cidr_block`

(required) The range of IPv4 addresses that will be used for layer 3 communication with hosts outside the VLAN. Example: `192.168.1.0/24`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the VLAN.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The VLAN's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The VLAN's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING'

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to use with this VLAN. All VNICs in the VLAN belong to these NSGs. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`vlan_tag`

(optional) The IEEE 802.1Q VLAN tag of this VLAN. Example: `100`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that the VLAN uses.

`time_created`

(optional) The date and time the VLAN was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the VLAN is in.

### DBMS_CLOUD_OCI_VN_MONITORING_VLAN_ENDPOINT_T Type

Defines the details required for a VLAN-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vlan_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`address`

(required) The IPv4 address of the `Endpoint`.

`vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN containing the IP address. This can be used to disambiguate which VLAN is queried, in case the endpoint IP address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).

### DBMS_CLOUD_OCI_VN_MONITORING_VNIC_T Type

A virtual network interface card. Each VNIC resides in a subnet in a VCN. An instance attaches to a VNIC to obtain a network connection into the VCN through that subnet. Each instance has a *primary VNIC* that is automatically created and attached during launch. You can add *secondary VNICs* to an instance after it's launched. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). Each VNIC has a *primary private IP* that is automatically assigned during launch. You can add *secondary private IPs* to a VNIC after it's created. For more information, see`CREATE_PRIVATE_IP`Function and[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm). If you are an Oracle Cloud VMware Solution customer, you will have secondary VNICs that reside in a VLAN instead of a subnet. These VNICs have other differences, which are called out in the descriptions of the relevant attributes in the `Vnic` object. Also see`VLAN`Type. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The VNIC's availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the VNIC.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

`is_primary`

(optional) Whether the VNIC is the primary VNIC (the VNIC that is automatically created and attached during instance launch).

`lifecycle_state`

(required) The current state of the VNIC.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`mac_address`

(optional) The MAC address of the VNIC. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution, the MAC address is learned. If the VNIC belongs to a subnet, the MAC address is a static, Oracle-provided value. Example: `00:00:00:00:00:01`

`nsg_ids`

(optional) A list of the OCIDs of the network security groups that the VNIC belongs to. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the VNIC belongs to the NSGs that are associated with the VLAN itself. See`VLAN`Type. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`vlan_id`

(optional) If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the `vlanId` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN the VNIC is in. See`VLAN`Type. If the VNIC is instead in a subnet, `subnetId` has a value.

`private_ip`

(optional) The private IP address of the primary `privateIp` object on the VNIC. The address is within the CIDR of the VNIC's subnet. Example: `10.0.3.3`

`public_ip`

(optional) The public IP address of the VNIC, if one is assigned.

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip). If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the `skipSourceDestCheck` attribute is `true`. This is because the source/destination check is always disabled for VNICs in a VLAN. Example: `true`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the VNIC is in.

`time_created`

(required) The date and time the VNIC was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_VN_MONITORING_VNIC_ENDPOINT_T Type

Defines the details required for a VNIC-type `Endpoint`.

Syntax
```

```

`dbms_cloud_oci_vn_monitoring_vnic_endpoint_t`is a subtype of the`dbms_cloud_oci_vn_monitoring_endpoint_t`type.

Fields

Field Description

`address`

(required) The IPv4 address of a VNIC type `Endpoint`.

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

### DBMS_CLOUD_OCI_VN_MONITORING_VTAP_T Type

A virtual test access point (VTAP) provides a way to mirror all traffic from a designated source to a selected target in order to facilitate troubleshooting, security analysis, and data monitoring. A VTAP is functionally similar to a test access point (TAP) you might deploy in your on-premises network. A *`CAPTURE_FILTER`Type* contains a set of *`CAPTURE_FILTER_RULE_DETAILS`Function* governing what traffic a VTAP mirrors.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the `Vtap` resource.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN containing the `Vtap` resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`id`

(required) The VTAP's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`lifecycle_state`

(required) The VTAP's administrative lifecycle state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED'

`lifecycle_state_details`

(optional) The VTAP's current running state.

Allowed values are: 'RUNNING', 'STOPPED'

`time_created`

(optional) The date and time the VTAP was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-08-25T21:10:29.600Z`

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source point where packets are captured.

`target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination resource where mirrored packets are sent.

`target_ip`

(optional) The IP address of the destination resource where mirrored packets are sent.

`capture_filter_id`

(required) The capture filter's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`encapsulation_protocol`

(optional) Defines an encapsulation header type for the VTAP's mirrored traffic.

Allowed values are: 'VXLAN'

`vxlan_network_identifier`

(optional) The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.

`is_vtap_enabled`

(optional) Used to start or stop a `Vtap` resource. * `TRUE` directs the VTAP to start mirroring traffic. * `FALSE` (Default) directs the VTAP to stop mirroring traffic.

`source_type`

(optional) The source type for the VTAP.

Allowed values are: 'VNIC', 'SUBNET', 'LOAD_BALANCER', 'DB_SYSTEM', 'EXADATA_VM_CLUSTER', 'AUTONOMOUS_DATA_WAREHOUSE'

`traffic_mode`

(optional) Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT

Allowed values are: 'DEFAULT', 'PRIORITY'

`max_packet_size`

(optional) The maximum size of the packets to be included in the filter.

`target_type`

(optional) The target type for the VTAP.

Allowed values are: 'VNIC', 'NETWORK_LOAD_BALANCER', 'IP_ADDRESS'

`source_private_endpoint_ip`

(optional) The IP Address of the source private endpoint.

`source_private_endpoint_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that source private endpoint belongs to.

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the `IN_PROGRESS` state until work is complete for that resource at which point it will transition to `CREATED`, `UPDATED`, or `DELETED`, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that you can do a GET operation on to access the resource metadata.

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_PATH_ANALYSIS_RESULT'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a `WorkRequestError` search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of `WorkRequestError` objects.

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a `WorkRequestLog` search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request log entries.

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_work_request_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_COLLECTION_T Type

Results of a `WorkRequestResult` search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of `WorkRequestResult` objects.

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_PATH_ANALYSIS_RESULT'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vn_monitoring_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a `WorkRequest` search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of `WorkRequestSummary` objects.

- [VN Monitoring Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-804518C9-2278-4ECA-A78D-E9FA10BDD334)
- [DBMS_CLOUD_OCI_VN_MONITORING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E324C538-B5F4-436B-85C7-D6430523F60E)
- [DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B66850C5-B222-470A-8FDA-F8A57A23DB75)
- [DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_TRAFFIC_SPEC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-16414EC8-A254-48E2-876B-4C04FAC4276E)
- [DBMS_CLOUD_OCI_VN_MONITORING_ROUTING_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-198BAD8A-ED1F-44D3-BC17-FD7F222AAC84)
- [DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-64AB7836-CE8F-48E6-8647-E44490E17A4D)
- [DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E699DF81-EAFE-43AC-A54C-4D1B9BB0C79D)
- [DBMS_CLOUD_OCI_VN_MONITORING_ACCESS_DENIED_TRAFFIC_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-944039DD-97DE-41CF-8D25-93BAB107ED12)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C2531862-497B-45D4-B5F6-F6380A732F6E)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1D99A916-4EAF-42D7-A340-4459C5937D63)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F26AEF0B-C630-4A13-BD73-EC6C330774F2)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-95A4C751-4398-4073-9D35-796E811E5F0B)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9B360AA3-10A6-4923-831B-CDECBDDCA31C)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8837D9B5-39DB-42CB-8FC8-F8C03025E344)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3750E23B-E403-4F79-82C7-48D4B29ADCFC)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D8506C40-0AFF-43D6-B70D-897836EFE40A)
- [DBMS_CLOUD_OCI_VN_MONITORING_ICMP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D9D3FD13-28E8-4D59-9C2E-5F366938F7F1)
- [DBMS_CLOUD_OCI_VN_MONITORING_PORT_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0F3B99AA-99CC-4CAD-A64F-AD24F3987452)
- [DBMS_CLOUD_OCI_VN_MONITORING_TCP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-02E87837-6209-497D-AD9D-FC9CE7BAA57E)
- [DBMS_CLOUD_OCI_VN_MONITORING_UDP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C232C06B-C339-4AFB-884E-B39F56DEF223)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6EF785D4-2EB8-4076-BB98-B974B1493122)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_SECURITY_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AB56124D-903F-459B-BBDF-E4D9BA8A8370)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-22E35D25-7697-453D-9AD7-4B5714568C98)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CF122ABD-62F4-44F9-BB82-CF2CC6BD3EA5)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_SUBNET_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DE68CD63-4125-431F-A4A7-50B391C50DE6)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9180D57D-8D0C-4388-956C-5692B0F39992)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D48E5035-5816-4D97-BD3C-0B119A9A66A1)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADD_VCN_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1B70B183-346D-4AA7-80F7-B92AA65E8A0D)
- [DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B03DF2F9-A1B2-4850-902F-5494FF5890CF)
- [DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-409E96F5-29D4-40C4-AF81-D6916768B9AA)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADDED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-660F20AC-5DC4-4A83-A3E8-391D5D125067)
- [DBMS_CLOUD_OCI_VN_MONITORING_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A90F1E81-7A6F-49F2-A633-DF303D29740A)
- [DBMS_CLOUD_OCI_VN_MONITORING_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F337D940-DEA8-49FB-8F13-1CBE10CF2D48)
- [DBMS_CLOUD_OCI_VN_MONITORING_QUERY_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-62096124-891E-49E8-81D9-9AF9FED85076)
- [DBMS_CLOUD_OCI_VN_MONITORING_GET_PATH_ANALYSIS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-74D5EF4C-D28B-472E-BDA0-C0F0A48781A4)
- [DBMS_CLOUD_OCI_VN_MONITORING_ADHOC_GET_PATH_ANALYSIS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EBDBBC53-F7A6-49FC-9AB9-DBB65A5E61C0)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_PHASE_ONE_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-74AF01BF-DA02-4492-BCBA-FBF66389295B)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_PHASE_TWO_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-66A4D198-505F-4145-B9C0-F0E8BC2EBA0C)
- [DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_PHASE_ONE_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-61D2D038-29B7-4B40-9E7E-C8B97609C3AD)
- [DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_PHASE_TWO_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-16EAF572-28DE-4223-A0D4-E64F69A50A1C)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_IKE_IP_SEC_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-ACD5F5CE-3C2E-41D7-95B1-B907D98EF124)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D7A23E32-7367-4CCB-911D-DE0AD46EB877)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9FDACDA4-B1D3-4215-B512-0076A80F0A43)
- [DBMS_CLOUD_OCI_VN_MONITORING_ALLOWED_SECURITY_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-92AEF9ED-764C-4231-A292-233000D0C391)
- [DBMS_CLOUD_OCI_VN_MONITORING_BGP_SESSION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3997A611-1A83-44D8-90C1-E1520397823F)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E4D580E6-747A-455B-9CA6-B855E50CB738)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1F062973-A9AF-4A44-B9F3-8A0D3EED0015)
- [DBMS_CLOUD_OCI_VN_MONITORING_BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-60206FA7-2EAC-4643-85EC-16FF98681FF3)
- [DBMS_CLOUD_OCI_VN_MONITORING_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BA7F0E11-8AE4-4178-972C-1BB6C554092B)
- [DBMS_CLOUD_OCI_VN_MONITORING_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3B07E2F1-4F69-4998-A24D-567C4A56C292)
- [DBMS_CLOUD_OCI_VN_MONITORING_BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E56300D2-89B1-41A3-8C6B-CF4885D6B105)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B88D006A-833C-4487-88D3-BE52DD35B5DD)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8586A9C6-B140-476C-A90B-F3B48C174BCE)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_ALLOCATED_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B4D2CD43-00EE-40CF-913B-F5EB8A507B3A)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-35089A6C-57C5-4345-A625-A3915B1FD720)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BAB5F5A2-FF15-46FC-909E-138A78745F06)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5F42C042-6012-4DEB-BB25-B306E5E18521)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1B28196A-DAB0-4665-8581-7E4E24415F9A)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-66BE9205-EF75-47AC-9081-D5CC6A11EB41)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIP_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-49E33BC8-477D-4EEB-BB87-83D4F6AB0B72)
- [DBMS_CLOUD_OCI_VN_MONITORING_VTAP_CAPTURE_FILTER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-899D5EC5-73AE-40A3-BF5F-83956DFC704A)
- [DBMS_CLOUD_OCI_VN_MONITORING_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-81B396A3-CAD6-451D-BBB7-611C985F865B)
- [DBMS_CLOUD_OCI_VN_MONITORING_VTAP_CAPTURE_FILTER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AD877C37-EB7E-4DDA-ADC2-2EFD6B410BA0)
- [DBMS_CLOUD_OCI_VN_MONITORING_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A53724C5-5E44-48AA-90A3-25036076D201)
- [DBMS_CLOUD_OCI_VN_MONITORING_CAPTURE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E4C8C627-82C5-421D-ACD5-5027473E8BA9)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_BYOIP_RANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FF47BF69-EDA4-416C-9702-34B831DEDE98)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CAPTURE_FILTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F82A1578-22E3-4173-98C3-1A2B1BF0B8F8)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CPE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4035450B-B2E4-4E1F-B03C-FE477E9FCAD9)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CROSS_CONNECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6BDAA6CA-3C38-4BD7-AD64-E55B5CC78187)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-80523992-2885-420E-A4F4-18A5BDA4D2FB)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_DHCP_OPTIONS_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F43243F8-B66E-4320-9296-5767D413D7CC)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_DRG_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FD04DBA4-D1C6-4D1E-9292-FFCDD9D22D3B)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_IP_SEC_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-584A7862-EC40-43AC-8148-F329BF1395EE)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_INTERNET_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8B7C3207-3BF4-4283-9826-12D2E6B7924C)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-485C3EC5-AB19-4380-A539-12255CA85BDD)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_NAT_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1896A09A-A577-4AB3-8729-1EBC7AD004FB)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DCE981F5-3152-4015-81FD-51092C820752)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PATH_ANALYZER_TEST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B716E847-D7BD-4164-900C-B5D15D697317)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PUBLIC_IP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EE925224-4A2D-469B-A1E4-6ADEFB2A08EE)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_PUBLIC_IP_POOL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-424B9C7C-952E-4652-9AA1-7B09D21C40DE)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3239ED8D-D907-4534-B6B8-D68AD4939875)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D99E5B0A-C7A7-4234-96A2-51CEC6CEED5B)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SECURITY_LIST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3402671C-7BB2-4BC9-AC0D-52BA65D8056A)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SERVICE_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B0A58F81-7AAB-43E3-A0EF-D1BE3546F1FD)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_SUBNET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3951FD04-3253-4C50-A4CD-E703D2080275)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VCN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8B46CCE2-EE23-44AA-A599-2287CBD9AB27)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B947919B-420F-4634-8F21-49C073D9C982)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VLAN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4B2F9FDD-DFCA-4A81-9DA5-B46D4D8A2D28)
- [DBMS_CLOUD_OCI_VN_MONITORING_CHANGE_VTAP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B8B4B573-2E53-4F3E-875C-1966A8C06794)
- [DBMS_CLOUD_OCI_VN_MONITORING_COMPARTMENT_INTERNAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F7B99489-7353-4C46-AD7D-F6AEE1033CFC)
- [DBMS_CLOUD_OCI_VN_MONITORING_COMPUTE_INSTANCE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-419C1D74-EF11-41E2-8B05-84B73600B14A)
- [DBMS_CLOUD_OCI_VN_MONITORING_CONNECT_LOCAL_PEERING_GATEWAYS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-45C97D6C-2FC4-4293-A1F8-20847C6FB6D4)
- [DBMS_CLOUD_OCI_VN_MONITORING_CONNECT_REMOTE_PEERING_CONNECTIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DAD72388-D5ED-4001-B99D-2674475E37BC)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-79228A22-83ED-4407-96EE-C4E235F704BA)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_ANSWER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3B2A4874-30EC-4CC7-9FB0-4E8A745B1FA7)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_QUESTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2CC9F733-A6B2-4620-BC6F-9498F89BBA7D)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-357D157A-97DB-4616-B5E6-27757FDB3ED6)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_QUESTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-470D03C4-4278-458D-9750-BFF4B6A1DCC5)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_SHAPE_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-69BBAE44-EFB6-4890-B1B1-8A716B06F777)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5A622670-7D84-4356-8985-7F987C903445)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_BYOIP_RANGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B0A7A47D-5468-42C4-9B94-57C34E82D6CA)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CAPTURE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4CB6CF67-9E4A-4805-9466-A31FEC2323B8)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3A8A7C26-89A0-4EF9-A642-53D926BB5EA6)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-54ED1261-265E-4BBA-AF08-03591BE403C8)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-20B7F932-C442-40D6-AC02-26654A37AB47)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CROSS_CONNECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1740A7BA-0979-46FA-8C24-6AFCACA56C7A)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_CROSS_CONNECT_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DC3F6E93-37DE-4F54-82AE-017E17401C4B)
- [DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2C4C63E3-5499-4F01-9380-BA69CF2D4AA4)
- [DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AA5F7EC0-D45A-45FB-A907-05EB2E0A5762)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DHCP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5FE2AA87-9377-4EA8-A7D2-116A2ABC3001)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9D9B321B-8CE6-4F93-86BF-ACE0D54714D3)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BD303217-F9E8-405B-B85F-3B7AB7667F5E)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-32EFF3DE-0F75-40F1-BBE2-7F5DC16BBDF3)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-50C7A67F-64EC-4206-9D50-AEE2D798FB29)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_DRG_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7C9C77E4-66DF-4F84-8BEA-EA4D5755F7A0)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7DE53604-D151-45BF-9E8F-3FDBB52AF4C6)
- [DBMS_CLOUD_OCI_VN_MONITORING_PHASE_ONE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2D91070F-E176-4834-87D0-014E59ACFB17)
- [DBMS_CLOUD_OCI_VN_MONITORING_PHASE_TWO_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-12AB3E7A-A77C-4C00-85BD-C0785E5DB7DB)
- [DBMS_CLOUD_OCI_VN_MONITORING_DPD_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3D08DC5A-730D-4A0D-871C-10C28FA33B27)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-09CB3952-5F50-47B5-936B-30869122C9AB)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6078B099-CFE8-4072-AB96-50F4EF3AF865)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3A7959E7-51C7-4281-B2E8-68C2E9F38440)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IP_SEC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6E07A552-73D2-447D-80FD-272E27B77C25)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_INTERNET_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6A9A27F6-8FE9-4C1B-8FC1-5F1F53D8BA21)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_IPV6_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B9C08372-4BDE-4458-8E39-B8B9A734F0FD)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7BAB7297-63BC-4D84-9384-87FB41FD5665)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_NAT_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B6A3E011-B18D-43DC-BE4A-7CC1F5117501)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_NETWORK_SECURITY_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C8C53261-CE2D-4737-8F02-FC259A4DE18E)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PATH_ANALYZER_TEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-197E7D3A-578A-4605-A47D-704A335ED27B)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PRIVATE_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4BC33A61-79EC-429B-A7D5-334A5E425641)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PUBLIC_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C90E912B-238B-4644-8463-09A68685E0E1)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_PUBLIC_IP_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-054E869B-3096-4C67-AC73-062521DE188C)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3A54C673-D12E-44CC-AEC2-7279F94C0131)
- [DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B67304F6-5D83-4CD8-82B4-93C5A202E775)
- [DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1345B287-9996-4706-8077-3E07BDDAB229)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F2682FE4-B028-42C7-B2CF-F4CBE2570C9B)
- [DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-46D4E054-4C16-4E59-8202-FF72D422BED6)
- [DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-39F707BC-0D2A-4478-A65C-699B12D5AFBC)
- [DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B86EF91A-152E-4304-8CED-77F15241DB9A)
- [DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CD0D443A-5D9C-4966-9AEF-DAF70DB16524)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SECURITY_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F1E08E1E-EBE9-4029-A6BA-DA4CAE5D8612)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1969885E-0CDC-42A4-8E20-F90029338F5F)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_REQUEST_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-735DDDB1-315B-4425-BB56-F2FBD69D43E7)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SERVICE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-068CBD6E-249E-4997-993F-52DB6FA42ECB)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0169379C-DBD7-48C7-A5D6-BB0842193A98)
- [DBMS_CLOUD_OCI_VN_MONITORING_BYOIPV6_CIDR_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BEBE8EBC-F318-4531-87CB-8F03E9ACD47B)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VCN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3CB84511-05A9-41BD-A72B-CFCF884E4ACD)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-47A40BFE-2A3E-4D19-8CED-4F415A1EE82E)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D2A66B4A-961F-465B-838D-13878A04ED22)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VIRTUAL_CIRCUIT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8F4377BA-0B39-483C-9C71-BA3055AF1CEF)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-96A961E2-0F6A-48AE-AB67-65C75F43425D)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CEAEBBC4-32A0-410F-9889-CA1E8794797A)
- [DBMS_CLOUD_OCI_VN_MONITORING_CREATE_VTAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-42B1059A-FF86-4C76-8417-42D33CEBC5F2)
- [DBMS_CLOUD_OCI_VN_MONITORING_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5BD182E0-B009-489E-89CF-EAC22787FF0C)
- [DBMS_CLOUD_OCI_VN_MONITORING_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8194C335-4554-41C9-88E1-D937EABA1CD3)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2FB28581-884F-496A-9A82-513BD5B75A3F)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1E8CE047-9DB9-4EB6-9BE3-B2B36D776685)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-535F821D-B48D-450F-A1F2-C5299946B0D2)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DCE0809C-8940-4D4F-BED2-8ACC47545910)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-428B7FE6-3E00-4AAD-9FE3-7D7C71C9A5E9)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_MAPPING_DETAILS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0CAC98D9-53D4-4E64-AD04-B7B6C97D78A0)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_PORT_SPEED_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C7323CF9-344A-48E3-9A45-E264E5A719E0)
- [DBMS_CLOUD_OCI_VN_MONITORING_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B73FED81-6AFA-47D7-9A71-576391D810D8)
- [DBMS_CLOUD_OCI_VN_MONITORING_CROSS_CONNECT_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C4727B1C-5CD2-457F-9822-BF81987084B3)
- [DBMS_CLOUD_OCI_VN_MONITORING_DEFAULT_DRG_ROUTE_TABLES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F0F35160-FAA9-4FDF-A27C-1116180FA257)
- [DBMS_CLOUD_OCI_VN_MONITORING_DENIED_SECURITY_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B706A0E1-BB47-4BBA-8F50-511AC5A2CD5C)
- [DBMS_CLOUD_OCI_VN_MONITORING_DENIED_SECURITY_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-79925BE3-8A26-48CE-8B60-3AC9D07F61A1)
- [DBMS_CLOUD_OCI_VN_MONITORING_DHCP_DNS_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-20ACBC80-7690-42A0-B89B-84C1CCAB37AA)
- [DBMS_CLOUD_OCI_VN_MONITORING_DHCP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-44450D01-ED8D-4193-BEB5-7475C2E27431)
- [DBMS_CLOUD_OCI_VN_MONITORING_DHCP_SEARCH_DOMAIN_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C6D94953-2095-4576-B0AA-EB1FBAA468B0)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CFBC3296-0D84-4939-9D84-51B6D3F24F2F)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-913C05D2-0CA2-409F-BDF0-EF2BE3353595)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D112E1A0-331C-4B55-9967-88EBE124B44E)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_ID_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-745CDD86-F359-4A01-A97C-C3C7B9F13E4F)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EED09FE2-BA35-42A4-B4DD-FB7308B6EABF)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_MATCH_ALL_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-59EAC1F7-7E73-472C-9839-274313B64620)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7398383D-6EB6-47EE-BD56-AAB0BA78919B)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ATTACHMENT_TYPE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B98B3DBB-3694-4110-9ED4-F395EF601EDC)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_REDUNDANCY_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-627002F1-F0F5-4301-A49C-1F8A7C3EF974)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FD3389E4-06DC-4DD3-AE2A-076CEB5829F9)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_DISTRIBUTION_STATEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EE1E7CBF-02BF-4A32-8500-821E9001A598)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9A91AB85-81A6-4AD2-8467-FF385AAD67B5)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-734E62D0-9782-4C23-B942-DFF42EFF08C4)
- [DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6AAA9C66-8BDC-4B3B-A394-F8B7FC9E5011)
- [DBMS_CLOUD_OCI_VN_MONITORING_DRG_ROUTING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D472F472-828D-41FA-85D6-2066E2DB3279)
- [DBMS_CLOUD_OCI_VN_MONITORING_EGRESS_SECURITY_LIST_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1C18F7F9-7BAC-495F-BE46-97F85129EABB)
- [DBMS_CLOUD_OCI_VN_MONITORING_ENCRYPTION_DOMAIN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A84EC3AF-D0AD-4189-A806-A98FEAF3C83F)
- [DBMS_CLOUD_OCI_VN_MONITORING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-763EC209-9E01-4070-BD62-ADD93679CCC2)
- [DBMS_CLOUD_OCI_VN_MONITORING_FAST_CONNECT_PROVIDER_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B6D9AB3D-4DD2-48EC-B5EF-F1BFC2EA7008)
- [DBMS_CLOUD_OCI_VN_MONITORING_FAST_CONNECT_PROVIDER_SERVICE_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8A7B4B72-5C5F-4AB7-A18D-F658A22E6461)
- [DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-434B5FE1-B2D3-4340-85EC-C31D4D8BC421)
- [DBMS_CLOUD_OCI_VN_MONITORING_FORWARDED_ROUTING_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-054E0233-0755-4DCB-A93A-211FBDECFED3)
- [DBMS_CLOUD_OCI_VN_MONITORING_GET_PUBLIC_IP_BY_IP_ADDRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5A788378-2906-4E5E-81C7-E8599011A285)
- [DBMS_CLOUD_OCI_VN_MONITORING_GET_PUBLIC_IP_BY_PRIVATE_IP_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D2017A62-77A7-4E58-BEDF-19223C425C0A)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-56FA06B6-B0B9-4DBD-8E33-F6B6E230EA9A)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-18F22721-C392-4B73-A21B-AFD9F3347365)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BCC00E08-39A2-463F-89AB-FD4B74C0F46E)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_DEVICE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B227E479-DE7B-4BD8-A210-14E5F4FB176D)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6FE6B5DA-19D9-4820-9FA5-9AB7CFBB22E6)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_STATUS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-453387A1-7429-47E4-89B2-E0363A147813)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_DEVICE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8CBCDE15-87BE-4957-8694-12C86605BA3A)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_PHASE_ONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E84C07E1-D9DC-4EB5-8983-E388BE661982)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_PHASE_TWO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0494AD00-328D-46A1-99E1-B0ED7F31EC5D)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0550FF36-DBE9-46B0-9BA5-852F97B06026)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_ERROR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0C63616D-04FA-4B9D-AFBE-4EF2DEE08A2E)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EC0D0FE6-8CD3-4F81-B20D-0EA60AD58965)
- [DBMS_CLOUD_OCI_VN_MONITORING_ICMP_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F7B4C5F9-2BD2-4F40-B22E-D208D7663848)
- [DBMS_CLOUD_OCI_VN_MONITORING_ICMP_TRAFFIC_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F9215B62-17B7-433F-B6C8-D4EBD50C9973)
- [DBMS_CLOUD_OCI_VN_MONITORING_INDETERMINATE_ROUTING_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C82F093A-DCC9-43B3-9E36-8B3B4ED60867)
- [DBMS_CLOUD_OCI_VN_MONITORING_INGRESS_SECURITY_LIST_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3AB48307-8AB9-47F5-B034-897B395E3EF8)
- [DBMS_CLOUD_OCI_VN_MONITORING_INTERNET_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D121BD4B-1E56-4A39-9E6F-F374CDD03A12)
- [DBMS_CLOUD_OCI_VN_MONITORING_IP_ADDRESS_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A494ACD2-8258-4D48-AE60-DA284240BEDC)
- [DBMS_CLOUD_OCI_VN_MONITORING_IPSEC_TUNNEL_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3838AF1D-32B0-4113-9BB9-7B7FC5426686)
- [DBMS_CLOUD_OCI_VN_MONITORING_IPV6_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-36D4F9B1-F9C2-4E11-A373-953A500E13C0)
- [DBMS_CLOUD_OCI_VN_MONITORING_LETTER_OF_AUTHORITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5F140396-C51D-4E5A-B293-B18A4B723974)
- [DBMS_CLOUD_OCI_VN_MONITORING_LOAD_BALANCER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-48CFDD4D-D9E5-4E05-939E-5EA9DC0BCFFC)
- [DBMS_CLOUD_OCI_VN_MONITORING_LOAD_BALANCER_LISTENER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7A88038C-77B5-4F2C-B005-4768630B2C33)
- [DBMS_CLOUD_OCI_VN_MONITORING_LOCAL_PEERING_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-74F6AB21-BA24-4A3A-8C26-03D4956F60A7)
- [DBMS_CLOUD_OCI_VN_MONITORING_LOOP_BACK_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8DE19140-2E90-4A43-A63A-316BEA236499)
- [DBMS_CLOUD_OCI_VN_MONITORING_MODIFY_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CC00EAEB-2EA8-47C3-B7C9-BE7B8673B081)
- [DBMS_CLOUD_OCI_VN_MONITORING_NAT_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E80595E2-E32E-4084-8B0A-50327B65FE1D)
- [DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_LOAD_BALANCER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F7745463-C8C0-44E6-840E-14C5E8250A5E)
- [DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_LOAD_BALANCER_LISTENER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BF136CA3-F5DD-4CE1-A133-340D74FACCC9)
- [DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_SECURITY_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6CD57F3D-8554-4A6C-AFC2-1A091447513A)
- [DBMS_CLOUD_OCI_VN_MONITORING_NETWORK_SECURITY_GROUP_VNIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8D609082-53E4-402E-9602-CFE1FFCD0424)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-5480F162-B745-4A6E-82ED-EA8F0F0CD4EA)
- [DBMS_CLOUD_OCI_VN_MONITORING_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7FA6D8E9-7CA8-4E7F-8876-CE706A8D29A6)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ENTITY_RELATIONSHIP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F1128DC5-2E5B-4E16-A707-0C166D51AD9A)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7732E249-9003-4A35-87AF-45B9DDEEB413)
- [DBMS_CLOUD_OCI_VN_MONITORING_NETWORKING_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-71686D6B-10B8-49F1-B535-4968CFBC2DD6)
- [DBMS_CLOUD_OCI_VN_MONITORING_NO_ROUTE_ROUTING_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-915CBE59-26E9-4AD5-8CE6-724040C05493)
- [DBMS_CLOUD_OCI_VN_MONITORING_NO_ROUTE_ROUTING_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-08CCB077-A8BC-427C-BC03-6ABEF0855835)
- [DBMS_CLOUD_OCI_VN_MONITORING_NSG_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9B12C829-329B-47CD-800A-9CB19ED6B56B)
- [DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7D58A9C5-C5E7-4B84-A8E0-05DC17617F84)
- [DBMS_CLOUD_OCI_VN_MONITORING_TRAFFIC_ROUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A2B93581-8EC7-4607-AAD5-2C0B4195869E)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EC74A138-58EF-4CB6-B3F5-BF682044F294)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B9B171A2-AD10-4556-9A41-1713EC57D1DA)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-41FD024E-AC10-4636-A204-4F8646E7C146)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9D96EE23-40B3-471D-A5A3-53B02DA2C04D)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYSIS_WORK_REQUEST_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-44406B83-DEF4-4C96-A15A-59D9354D84FC)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-855CEF4B-7406-418E-A27E-BBE814A27444)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-512F2EF5-54C4-4E1A-A2F0-A96C8304C475)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-ACAE102D-3B58-4D8D-921D-70E0BE03F714)
- [DBMS_CLOUD_OCI_VN_MONITORING_PATH_ANALYZER_TEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3EB69DD3-FDC9-4E01-A4EC-B7087C9DE30C)
- [DBMS_CLOUD_OCI_VN_MONITORING_PERSISTED_GET_PATH_ANALYSIS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0C368705-03F5-4BEF-9FFE-9160A368FCFD)
- [DBMS_CLOUD_OCI_VN_MONITORING_PRIVATE_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B3929FCF-3207-4BF8-ACF3-BE99928005A1)
- [DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-50C6DE92-B785-49A5-8308-31E1BD1A7982)
- [DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F13088CE-B29B-41AF-A179-7B52D654A3D1)
- [DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-34DAE7E6-4E75-4FA3-935E-77E76E38C19A)
- [DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FCC6E105-E70C-4F2A-9F55-0A31A0EB8E1B)
- [DBMS_CLOUD_OCI_VN_MONITORING_PUBLIC_IP_POOL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7ACD4A3E-9720-4605-B1E3-F731652ACCE5)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOTE_PEERING_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7FBADC82-CC63-47FC-AB6D-29D5250CC3A5)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOTE_PEERING_CONNECTION_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AC3B3ECD-A02B-473F-9DA0-4CC5B9E24331)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-653D77DB-A287-4B27-BB72-FDB5834800DE)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-391F9A8E-8BCD-4BBA-960C-BDFA50A23C37)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-556657C6-0DC6-41ED-9866-FAD011029122)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2B4BF183-30F7-424D-BCE4-81CB4413BB8A)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_SUBNET_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6DC5C331-EC4B-42B1-BCF6-57FC2B67E733)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8CC3B5C7-110A-4169-B88E-25AB732BCA7A)
- [DBMS_CLOUD_OCI_VN_MONITORING_REMOVE_VCN_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-68179A9D-4560-471E-B76A-939F1FFA17A9)
- [DBMS_CLOUD_OCI_VN_MONITORING_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-382A2EE6-DB4A-4AC4-BB42-CE1A020195EF)
- [DBMS_CLOUD_OCI_VN_MONITORING_SECURITY_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0D9C3021-C886-4843-89F5-1952574C0B13)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6B29E084-8947-40DA-B019-89B9B178E645)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4882F1F3-67EB-42D1-A9BA-5B02AB56A891)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_ID_RESPONSE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-10041D9F-24B3-4A2B-B8F9-2A9A9FA533DD)
- [DBMS_CLOUD_OCI_VN_MONITORING_SERVICE_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-853BCF3B-FCA3-4854-B663-FF08C99863C2)
- [DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_EGRESS_SECURITY_LIST_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E83EDE82-9C77-4414-AB3A-B4B33223060E)
- [DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_INGRESS_SECURITY_LIST_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3E90431B-E585-4C5E-9961-946607043C44)
- [DBMS_CLOUD_OCI_VN_MONITORING_STATEFUL_NSG_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AF5567C1-E95F-4714-92BE-847B080A5BB2)
- [DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2C5F074E-29F8-4EF5-B41A-EE1E44F8469B)
- [DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F2EC81CF-FB62-4354-A8A0-32DC3F505B62)
- [DBMS_CLOUD_OCI_VN_MONITORING_SUBNET_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B2A879C4-EBBC-4C4B-8137-C392477DE3A1)
- [DBMS_CLOUD_OCI_VN_MONITORING_TCP_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B87204EF-B779-4BBA-BA36-67343AA7DAB4)
- [DBMS_CLOUD_OCI_VN_MONITORING_TCP_TRAFFIC_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0D91B03F-CA43-4CC6-90A8-A12C92ABCDF6)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ASSOCIATED_WITH_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-661B3FEC-4800-4AB4-BC87-8AC48AC74135)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ASSOCIATED_WITH_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-17AAB871-892C-4411-9730-F87708C73187)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_CONTAINS_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AC2895E4-B506-4A36-A34A-F3821921E937)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ROUTES_TO_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A3CBCCEE-794A-4B71-83CF-768E85D5B208)
- [DBMS_CLOUD_OCI_VN_MONITORING_TOPOLOGY_ROUTES_TO_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-ED84202D-B95A-4B87-91A6-3815F7293939)
- [DBMS_CLOUD_OCI_VN_MONITORING_CPE_DEVICE_CONFIG_ANSWER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AB430720-33D3-41AC-88E7-C97CAFE02BD3)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_CPE_DEVICE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A6F58918-97CD-4C65-B0A0-46BC2600CB31)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_ROUTE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D8EB384A-D59B-47A6-895D-48D5EC33DA07)
- [DBMS_CLOUD_OCI_VN_MONITORING_TUNNEL_SECURITY_ASSOCIATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-441BA5DF-6BD2-446B-B31A-D3FE7A37E773)
- [DBMS_CLOUD_OCI_VN_MONITORING_UDP_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BA4C2F77-9E62-46D8-B6F6-D2BE0C39CFAC)
- [DBMS_CLOUD_OCI_VN_MONITORING_UDP_TRAFFIC_PROTOCOL_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-C336EBB7-5A09-48FB-854A-576281C270AB)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_BYOIP_RANGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FBAA74B5-ED50-4936-B42F-4A71E44699A6)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CAPTURE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6998E3B3-4BA8-4228-80C5-A546062A2F79)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7B3C7DEA-F946-4180-8844-B86A678C3C97)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E11955DE-93B0-4E2B-B31A-FB25639AD231)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-150B428D-E7A2-481B-AB87-6C6511232F45)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CROSS_CONNECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2A9FB2A1-8D58-4F6F-87F6-63CDCBF2B716)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_CROSS_CONNECT_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2A62AAE2-4B37-40B6-BF6E-4929AA19C696)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DHCP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-01BDA4E0-A666-43F8-9B9D-73FD53A078FE)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-97CDA9A9-0DFA-40D9-BE41-05A02C87B004)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-117BB09A-B057-44C4-B888-A184900795C4)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BCBCC9A4-1721-4A2F-BCEC-51B63FC4F86C)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-467CCE29-4116-4538-B438-EC611FA9A269)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-22434615-321D-40B3-8524-5B8ADF028E84)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CE76B1FA-9094-4074-B80D-3D70D94FE7F5)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8ED8B700-DBC6-4268-8604-F33C8A406E55)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F31F6F51-82E8-497D-A254-09B1A1A447B6)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-663DCA41-87CE-47A2-AA95-8D7C06E7A4D7)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_DRG_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-35499C3E-F4B1-4A44-86CD-5CF4B05CE58A)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E128D128-3673-4C01-8EE9-20AFDB578048)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0F084970-EC3E-49FC-8D4D-9DC5380F4C14)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D112552E-4E39-4C06-9E1B-72303E5D71DE)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-3A8CA6A6-25C5-4EDC-A016-2D6B28391027)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-071E9305-801E-4D20-97A7-04744AD55D7B)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_INTERNET_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-876FB96B-9BB1-4A87-8FBC-671983DE2850)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_IPV6_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A4DF378D-5247-4C67-85EB-351D88DE948A)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CA3F6698-BE1A-4BCE-9967-B1D0ED3430A1)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NAT_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-FF6832A2-273C-4EDE-83CC-12448A1BC1CC)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NETWORK_SECURITY_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-9ED5492B-FD34-4A6F-84DC-135AE4A329D6)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-4AEE9EF7-7222-4CA9-8520-E8A0A3471CF6)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-89B52626-BEEC-406E-B06F-925323500826)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-95A3301A-CD0A-4DCD-A5AE-9D346EAF3B37)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PATH_ANALYZER_TEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2D8CD56C-AF08-4151-8C7C-00A5A367865E)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PRIVATE_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-87FE1662-51CA-4192-803E-A4A362191166)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PUBLIC_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-89AA6B1D-3609-442F-BE2D-A380A74BB5AA)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_PUBLIC_IP_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F7E1D7F4-B474-46E8-826F-22249B845F22)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-25EBC54C-A296-47A3-8361-8309AE4B2D7B)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-384B16CD-DB20-4DBC-98C8-99F6C15DFE73)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SECURITY_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DEA4E1B6-6A37-4B60-9A2F-68BEB5A73561)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SERVICE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D5F4C1B5-34F0-47FF-9704-298B9D15F74A)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-648FF9B5-52CA-4702-B5BD-DAB94500F855)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_TUNNEL_CPE_DEVICE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-49CB269E-B361-4A20-A3FF-15F93E488D58)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VCN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-00B28DF6-D36A-4E37-8ED3-252225B210B9)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VIRTUAL_CIRCUIT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-516D9F8F-AD92-45CC-99A3-C1D9F1B12885)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-33517918-388B-48A8-A7D7-E8F1D7E198B7)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-725493AA-BFD9-41CC-8397-34301A7736FA)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATE_VTAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-8766F8EC-F002-45EA-A7C5-EC4F231F4B2C)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPDATED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B7F8EAF8-E289-4C2F-8047-D14149CE4402)
- [DBMS_CLOUD_OCI_VN_MONITORING_UPGRADE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-05414AF2-F7F8-4FFD-AEE0-DC212E941BC5)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0F69CCB6-F2B0-4C09-AC50-46D84667DED4)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_DNS_RESOLVER_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F091072D-8BE8-443C-BEEF-35CF4A3CC594)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D371EB98-E492-4841-9D06-073F79A84ACF)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-413520C9-C3B2-4105-9A37-FAEBDEE3E4CC)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6859B4CA-3C4B-41B4-A3F3-DE0CF238AAB5)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_ROUTING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-1B406049-8CAA-4809-BAE3-0370635CC3F5)
- [DBMS_CLOUD_OCI_VN_MONITORING_VCN_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A0AE7574-B918-4DF0-8BC2-E30C7CCDD697)
- [DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-758DAFD7-9E2E-4838-AD81-3F01F8C96186)
- [DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-36FE5B97-CF2B-48C9-A0D1-5FD7AD82269D)
- [DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-F0534D83-9C7E-41EE-BF22-EC7A0B63E1EA)
- [DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-6A333B72-D6B9-40C5-8C27-703204B96C95)
- [DBMS_CLOUD_OCI_VN_MONITORING_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-EC7A5432-884C-42E9-9AE7-E40687807EFA)
- [DBMS_CLOUD_OCI_VN_MONITORING_VISIBLE_TRAFFIC_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D1ACDE10-0868-4272-BB96-C553B2A1FA96)
- [DBMS_CLOUD_OCI_VN_MONITORING_VLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B53D21E1-65E3-44F6-BDE4-890EAF8B8F05)
- [DBMS_CLOUD_OCI_VN_MONITORING_VLAN_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-068936E2-DF13-446B-B01A-F454992E870F)
- [DBMS_CLOUD_OCI_VN_MONITORING_VNIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-AD45470F-5812-4370-AC28-1CFE26CBAC6D)
- [DBMS_CLOUD_OCI_VN_MONITORING_VNIC_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-CF557DD4-4C0D-49FC-97E3-91D9838B7EAD)
- [DBMS_CLOUD_OCI_VN_MONITORING_VTAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B2B2D558-9CB6-4E5E-A30B-6FD4964C399F)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E329014B-6D58-4C7E-9539-E47939DB58C8)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-B225E5C3-C20F-4208-9CBD-9E99864AFB6D)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-2A51C071-9F32-4C73-8197-82965ED5A404)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-7C05C0FE-473F-46FC-AC79-2C8CC628E63C)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-D26C5BDF-6CCF-4BC4-9082-FED0F564A3EF)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E3C8EB55-5436-44FF-8554-7F1E4A7BDEE8)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-0426DBA3-1DE5-4D49-8CAA-9F42E213C2F4)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-DB0DB2EC-7460-4616-8520-C6DF2D6871D1)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-125CE8E0-6278-4A74-B274-9F7C77330243)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-BC0506F4-5C8B-41DF-A023-F77451C891B1)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-E39EDCF9-247B-41F1-9CA3-A76BDBB35C68)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-A16C6F05-E70F-47C5-B99D-27901499FA1C)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-618EA610-C0C4-460B-8CFA-D9F6C343A88B)
- [DBMS_CLOUD_OCI_VN_MONITORING_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vn_monitoring_t.html#ADSDK-GUID-02B25BC7-EC9B-41B9-BFCE-2CEBD4AC8965)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
