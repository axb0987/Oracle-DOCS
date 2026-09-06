# Core Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#dcoc-content-body)

## Core Common Types

### DBMS_CLOUD_OCI_CORE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The match criteria in a route distribution statement. The match criteria outlines which routes should be imported or exported.

Syntax
```

```

Fields

Field Description

`match_type`

(required) The type of the match criteria for a route distribution statement.

Allowed values are: 'DRG_ATTACHMENT_TYPE', 'DRG_ATTACHMENT_ID', 'MATCH_ALL'

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_TBL Type

Nested table type of dbms_cloud_oci_core_drg_route_distribution_match_criteria_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_add_drg_route_distribution_statement_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to add statements to a route distribution.

Syntax
```

```

Fields

Field Description

`statements`

(required) The collection of route distribution statements to insert into the route distribution.

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULE_DETAILS_T Type

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

(required) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed. Potential values: * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.

`next_hop_drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_add_drg_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULES_DETAILS_T Type

Details used in a request to add static routes to a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rules`

(optional) The collection of static rules used to insert routes into the DRG route table.

### DBMS_CLOUD_OCI_CORE_IMAGE_MEMORY_CONSTRAINTS_T Type

For a flexible image and shape, the amount of memory supported for instances that use this image.

Syntax
```

```

Fields

Field Description

`min_in_g_bs`

(optional) The minimum amount of memory, in gigabytes.

`max_in_g_bs`

(optional) The maximum amount of memory, in gigabytes.

### DBMS_CLOUD_OCI_CORE_IMAGE_OCPU_CONSTRAINTS_T Type

OCPU options for an image and shape.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The minimum number of OCPUs supported for this image and shape.

`l_max`

(optional) The maximum number of OCPUs supported for this image and shape.

### DBMS_CLOUD_OCI_CORE_ADD_IMAGE_SHAPE_COMPATIBILITY_ENTRY_DETAILS_T Type

Image shape compatibility details.

Syntax
```

```

Fields

Field Description

`memory_constraints`

(optional)

`ocpu_constraints`

(optional)

### DBMS_CLOUD_OCI_CORE_ICMP_OPTIONS_T Type

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

### DBMS_CLOUD_OCI_CORE_PORT_RANGE_T Type

Syntax
```

```

Fields

Field Description

`l_max`

(required) The maximum port number, which must not be less than the minimum port number. To specify a single port number, set both the min and max to the same value.

`l_min`

(required) The minimum port number, which must not be greater than the maximum port number.

### DBMS_CLOUD_OCI_CORE_TCP_OPTIONS_T Type

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

### DBMS_CLOUD_OCI_CORE_UDP_OPTIONS_T Type

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

### DBMS_CLOUD_OCI_CORE_ADD_SECURITY_RULE_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_ADD_SECURITY_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_add_security_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules to add.

### DBMS_CLOUD_OCI_CORE_ADD_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_ADD_SUBNET_IPV6_CIDR_DETAILS_T Type

Details used when adding an IPv6 prefix to a subnet.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(required) This field is not required and should only be specified when adding an IPv6 prefix to a subnet's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/64`

### DBMS_CLOUD_OCI_CORE_ADD_VCN_CIDR_DETAILS_T Type

Details used to add a CIDR block to a VCN.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to add.

### DBMS_CLOUD_OCI_CORE_BYOIPV6_CIDR_DETAILS_T Type

The list of one or more BYOIPv6 prefixes for the VCN that meets the following criteria: - The prefix must be from a BYOIPv6 range. - The IPv6 prefixes must be valid. - Multiple prefix must not overlap each other or the on-premises network prefix. - The number of prefixes must not exceed the limit of IPv6 prefixes allowed to a VCN.

Syntax
```

```

Fields

Field Description

`byoipv6_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource to which the CIDR block belongs.

`ipv6_cidr_block`

(required) An IPv6 prefix required to create a VCN with a BYOIP prefix. It could be the whole prefix identified in `byoipv6RangeId`, or a subrange. Example: `2001:0db8:0123::/48`

### DBMS_CLOUD_OCI_CORE_ADD_VCN_IPV6_CIDR_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_SECURITY_RULE_T Type

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

### DBMS_CLOUD_OCI_CORE_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_core_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ADDED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules that were added.

### DBMS_CLOUD_OCI_CORE_ALLOWED_PHASE_ONE_PARAMETERS_T Type

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

### DBMS_CLOUD_OCI_CORE_ALLOWED_PHASE_TWO_PARAMETERS_T Type

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

### DBMS_CLOUD_OCI_CORE_DEFAULT_PHASE_ONE_PARAMETERS_T Type

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

### DBMS_CLOUD_OCI_CORE_DEFAULT_PHASE_TWO_PARAMETERS_T Type

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

### DBMS_CLOUD_OCI_CORE_ALLOWED_IKE_IP_SEC_PARAMETERS_T Type

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

### DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration requested for the instance. If you provide the parameter, the instance is created with the platform configuration that you specify. For any values that you omit, the instance uses the default configuration values for the `shape` that you specify. If you don't provide the parameter, the default values for the `shape` are used. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned. For more information about shielded instances, see[Shielded Instances](https://docs.oracle.com/iaas/Content/Compute/References/shielded-instances.htm). For more information about BIOS settings for bare metal instances, see[BIOS Settings for Bare Metal Instances](https://docs.oracle.com/iaas/Content/Compute/References/bios-settings.htm).

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of platform being configured.

Allowed values are: 'AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM', 'AMD_ROME_BM_GPU', 'GENERIC_BM', 'INTEL_ICELAKE_BM', 'INTEL_SKYLAKE_BM', 'AMD_VM', 'INTEL_VM'

`is_secure_boot_enabled`

(optional) Whether Secure Boot is enabled on the instance.

`is_trusted_platform_module_enabled`

(optional) Whether the Trusted Platform Module (TPM) is enabled on the instance.

`is_measured_boot_enabled`

(optional) Whether the Measured Boot feature is enabled on the instance.

`is_memory_encryption_enabled`

(optional) Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default value is `false`.

### DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal GPU instance with the following shape: BM.GPU.GM4.8 (also named BM.GPU.A100-v2.8) (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_milan_bm_gpu_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_PLATFORM_CONFIG_T Type

The platform configuration for the instance.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of platform being configured.

Allowed values are: 'AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM', 'AMD_ROME_BM_GPU', 'GENERIC_BM', 'INTEL_ICELAKE_BM', 'INTEL_SKYLAKE_BM', 'AMD_VM', 'INTEL_VM'

`is_secure_boot_enabled`

(optional) Whether Secure Boot is enabled on the instance.

`is_trusted_platform_module_enabled`

(optional) Whether the Trusted Platform Module (TPM) is enabled on the instance.

`is_measured_boot_enabled`

(optional) Whether the Measured Boot feature is enabled on the instance.

`is_memory_encryption_enabled`

(optional) Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default value is `false`.

### DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_GPU_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal GPU instance with the following shape: BM.GPU.GM4.8 (also named BM.GPU.A100-v2.8) (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_milan_bm_gpu_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with one of the following shapes: BM.Standard.E4.128 or BM.DenseIO.E4.128 (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_milan_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with one of the following shapes: BM.Standard.E4.128 or BM.DenseIO.E4.128 (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_milan_bm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal GPU instance with the BM.GPU4.8 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_rome_bm_gpu_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_GPU_PLATFORM_CONFIG_T Type

The platform configuration of a bare metal GPU instance that uses the BM.GPU4.8 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_rome_bm_gpu_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with the BM.Standard.E3.128 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_rome_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_PLATFORM_CONFIG_T Type

The platform configuration of a bare metal instance that uses the BM.Standard.E3.128 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_amd_rome_bm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_AMD_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a virtual machine instance with the AMD platform.

Syntax
```

```

`dbms_cloud_oci_core_amd_vm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_AMD_VM_PLATFORM_CONFIG_T Type

The platform configuration of a virtual machine instance that uses the AMD platform.

Syntax
```

```

`dbms_cloud_oci_core_amd_vm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_T Type

Listing details.

Syntax
```

```

Fields

Field Description

`contact_url`

(optional) Listing's contact URL.

`description`

(optional) Description of the listing.

`listing_id`

(optional) The OCID of the listing.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_published`

(optional) Date and time the listing was published, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

`publisher_logo_url`

(optional) Publisher's logo URL.

`publisher_name`

(optional) Name of the publisher who published this listing.

`summary`

(optional) Summary of the listing.

### DBMS_CLOUD_OCI_CORE_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_T Type

Listing Resource Version

Syntax
```

```

Fields

Field Description

`listing_id`

(optional) The OCID of the listing this resource version belongs to.

`time_published`

(optional) Date and time the listing resource version was published, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

`listing_resource_id`

(optional) OCID of the listing resource.

`listing_resource_version`

(optional) Resource Version.

`available_regions`

(optional) List of regions that this listing resource version is available. For information about regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example: `[\"us-ashburn-1\", \"us-phoenix-1\"]`

`compatible_shapes`

(optional) Array of shapes compatible with this resource. You can enumerate all available shapes by calling`LIST_SHAPES`Function. Example: `[\"VM.Standard1.1\", \"VM.Standard1.2\"]`

`accessible_ports`

(optional) List of accessible ports for instances launched with this listing resource version.

`allowed_actions`

(optional) Allowed actions for the listing resource.

Allowed values are: 'SNAPSHOT', 'BOOT_VOLUME_DETACH', 'PRESERVE_BOOT_VOLUME', 'SERIAL_CONSOLE_ACCESS', 'BOOT_RECOVERY', 'BACKUP_BOOT_VOLUME', 'CAPTURE_CONSOLE_HISTORY'

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_AGREEMENTS_T Type

Agreements for a listing resource version.

Syntax
```

```

Fields

Field Description

`listing_id`

(optional) The OCID of the listing associated with these agreements.

`listing_resource_version`

(optional) Listing resource version associated with these agreements.

`oracle_terms_of_use_link`

(optional) Oracle TOU link

`eula_link`

(optional) EULA link

`time_retrieved`

(optional) Date and time the agreements were retrieved, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

`signature`

(optional) A generated signature for this agreement retrieval operation which should be used in the create subscription call.

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_SUMMARY_T Type

Listing Resource Version summary

Syntax
```

```

Fields

Field Description

`listing_id`

(optional) The OCID of the listing this resource version belongs to.

`time_published`

(optional) Date and time the listing resource version was published, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

`listing_resource_id`

(optional) OCID of the listing resource.

`listing_resource_version`

(optional) Resource Version.

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_SUMMARY_T Type

A summary of a listing.

Syntax
```

```

Fields

Field Description

`listing_id`

(optional) the region free ocid of the listing resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`summary`

(optional) The short summary for the listing.

`publisher_name`

(optional) The name of the publisher who published this listing.

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_SUBSCRIPTION_T Type

a subscription for a listing resource version.

Syntax
```

```

Fields

Field Description

`publisher_name`

(optional) Name of the publisher who published this listing.

`listing_id`

(optional) The ocid of the listing resource.

`listing_resource_version`

(optional) Listing resource version.

`listing_resource_id`

(optional) Listing resource id.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`summary`

(optional) The short summary to the listing.

`compartment_id`

(optional) The compartmentID of the subscription.

`time_created`

(optional) Date and time at which the subscription was created, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

### DBMS_CLOUD_OCI_CORE_APP_CATALOG_SUBSCRIPTION_SUMMARY_T Type

a subscription summary for a listing resource version.

Syntax
```

```

Fields

Field Description

`publisher_name`

(optional) Name of the publisher who published this listing.

`listing_id`

(optional) The ocid of the listing resource.

`listing_resource_version`

(optional) Listing resource version.

`listing_resource_id`

(optional) Listing resource id.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`summary`

(optional) The short summary to the listing.

`compartment_id`

(optional) The compartmentID of the subscription.

`time_created`

(optional) Date and time at which the subscription was created, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

### DBMS_CLOUD_OCI_CORE_ATTACH_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`boot_volume_id`

(required) The OCID of the boot volume.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`instance_id`

(required) The OCID of the instance.

`encryption_in_transit_type`

(optional) Refer the top-level definition of encryptionInTransitType. The default value is NONE.

Allowed values are: 'NONE', 'BM_ENCRYPTION_IN_TRANSIT'

### DBMS_CLOUD_OCI_CORE_ATTACH_VOLUME_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`device`

(optional) The device name. To retrieve a list of devices for a given instance, see`LIST_INSTANCE_DEVICES`Function.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`instance_id`

(required) The OCID of the instance.

`is_read_only`

(optional) Whether the attachment was created in read-only mode.

`is_shareable`

(optional) Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.

`l_type`

(required) The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".

`volume_id`

(required) The OCID of the volume.

### DBMS_CLOUD_OCI_CORE_ATTACH_EMULATED_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_attach_emulated_volume_details_t`is a subtype of the`dbms_cloud_oci_core_attach_volume_details_t`type.

### DBMS_CLOUD_OCI_CORE_ATTACH_I_SCSI_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_attach_i_scsi_volume_details_t`is a subtype of the`dbms_cloud_oci_core_attach_volume_details_t`type.

Fields

Field Description

`use_chap`

(optional) Whether to use CHAP authentication for the volume attachment. Defaults to false.

`encryption_in_transit_type`

(optional) Refer the top-level definition of encryptionInTransitType. The default value is NONE.

Allowed values are: 'NONE', 'BM_ENCRYPTION_IN_TRANSIT'

`is_agent_auto_iscsi_login_enabled`

(optional) Whether to enable Oracle Cloud Agent to perform the iSCSI login and logout commands after the volume attach or detach operations for non multipath-enabled iSCSI attachments.

### DBMS_CLOUD_OCI_CORE_ATTACH_INSTANCE_POOL_INSTANCE_DETAILS_T Type

An instance that is to be attached to an instance pool.

Syntax
```

```

Fields

Field Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

### DBMS_CLOUD_OCI_CORE_ATTACH_LOAD_BALANCER_DETAILS_T Type

Represents a load balancer that is to be attached to an instance pool.

Syntax
```

```

Fields

Field Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to attach to the instance pool.

`backend_set_name`

(required) The name of the backend set on the load balancer to add instances to.

`port`

(required) The port value to use when creating the backend set.

`vnic_selection`

(required) Indicates which VNIC on each instance in the pool should be used to associate with the load balancer. Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance pool.

### DBMS_CLOUD_OCI_CORE_ATTACH_PARAVIRTUALIZED_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_attach_paravirtualized_volume_details_t`is a subtype of the`dbms_cloud_oci_core_attach_volume_details_t`type.

Fields

Field Description

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.

### DBMS_CLOUD_OCI_CORE_ATTACH_SERVICE_DETERMINED_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_attach_service_determined_volume_details_t`is a subtype of the`dbms_cloud_oci_core_attach_volume_details_t`type.

### DBMS_CLOUD_OCI_CORE_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_T Type

Details to assign an IPv6 subnet prefix and IPv6 address on VNIC creation.

Syntax
```

```

Fields

Field Description

`ipv6_subnet_cidr`

(optional) The IPv6 prefix allocated to the subnet.

`ipv6_address`

(optional) An IPv6 address of your choice. Must be an available IPv6 address within the subnet's prefix. If an IPv6 address is not provided: - Oracle will automatically assign an IPv6 address from the subnet's IPv6 prefix if and only if there is only one IPv6 prefix on the subnet. - Oracle will automatically assign an IPv6 address from the subnet's IPv6 Oracle GUA prefix if it exists on the subnet.

### DBMS_CLOUD_OCI_CORE_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_ipv6_address_ipv6_subnet_cidr_pair_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VNIC_DETAILS_T Type

Contains properties for a VNIC. You use this object when creating the primary VNIC during instance launch or when creating a secondary VNIC. For more information about VNICs, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

Syntax
```

```

Fields

Field Description

`assign_ipv6_ip`

(optional) Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled subnet. Default: False. When provided you may optionally provide an IPv6 prefix (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr` is not provided then an IPv6 prefix is chosen for you.

`assign_public_ip`

(optional) Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the`SUBNET`Type), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned. **Note:** This public IP address is associated with the primary private IP on the VNIC. For more information, see[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm). **Note:** There's a limit to the number of`PUBLIC_IP`Type a VNIC or instance can have. If you try to create a secondary VNIC with an assigned public IP for an instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm). Example: `false` If you specify a `vlanId`, then `assignPublicIp` must be set to false. See`VLAN`Type.

`assign_private_dns_record`

(optional) Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record registration for the VNIC. If set to true, the DNS record will be registered. The default value is true. If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). When launching an instance, use this `hostnameLabel` instead of the deprecated `hostnameLabel` in`LAUNCH_INSTANCE_DETAILS`Function. If you provide both, the values must match. Example: `bminstance1` If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN can not be assigned a hostname. See`VLAN`Type.

`ipv6_address_ipv6_subnet_cidr_pair_details`

(optional) A list of IPv6 prefix ranges from which the VNIC is assigned an IPv6 address. You can provide only the prefix ranges from which OCI selects an available address from the range. You can optionally choose to leave the prefix range empty and instead provide the specific IPv6 address within that range to use.

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

### DBMS_CLOUD_OCI_CORE_ATTACH_VNIC_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`create_vnic_details`

(required)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`instance_id`

(required) The OCID of the instance.

`nic_index`

(optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

### DBMS_CLOUD_OCI_CORE_AUTOTUNE_POLICY_T Type

An autotune policy automatically tunes the volume's performace based on the type of the policy.

Syntax
```

```

Fields

Field Description

`autotune_type`

(required) This specifies the type of autotunes supported by OCI.

Allowed values are: 'DETACHED_VOLUME', 'PERFORMANCE_BASED'

### DBMS_CLOUD_OCI_CORE_BGP_SESSION_INFO_T Type

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

### DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_T Type

An asynchronous replica of a block volume that can then be used to create a new block volume or recover a block volume. For more information, see[Overview of Cross-Region Volume Replication](https://docs.oracle.com/iaas/Content/Block/Concepts/volumereplication.htm)To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the block volume replica. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the block volume replica.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The block volume replica's Oracle ID (OCID).

`lifecycle_state`

(required) The current state of a block volume replica.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ACTIVATING', 'TERMINATING', 'TERMINATED', 'FAULTY'

`size_in_g_bs`

(required) The size of the source block volume, in GBs.

`time_created`

(required) The date and time the block volume replica was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_last_synced`

(required) The date and time the block volume replica was last synced from the source block volume. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`block_volume_id`

(required) The OCID of the source block volume.

`total_data_transferred_in_g_bs`

(optional) The total size of the data transferred from the source block volume to the block volume replica, in GBs.

`volume_group_replica_id`

(optional) The OCID of the volume group replica.

### DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_DETAILS_T Type

Contains the details for the block volume replica

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`availability_domain`

(required) The availability domain of the block volume replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_INFO_T Type

Information about the block volume replica in the destination availability domain.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`block_volume_replica_id`

(required) The block volume replica's Oracle ID (OCID).

`availability_domain`

(required) The availability domain of the block volume replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type

Image Capability Schema Descriptor is a type of capability for an image.

Syntax
```

```

Fields

Field Description

`descriptor_type`

(required) The image capability schema descriptor type for the capability

`source`

(required)

Allowed values are: 'GLOBAL', 'IMAGE'

### DBMS_CLOUD_OCI_CORE_BOOLEAN_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type

Boolean type ImageCapabilitySchemaDescriptor

Syntax
```

```

`dbms_cloud_oci_core_boolean_image_capability_schema_descriptor_t`is a subtype of the`dbms_cloud_oci_core_image_capability_schema_descriptor_t`type.

Fields

Field Description

`default_value`

(optional) the default value

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_INFO_T Type

Information about the boot volume replica in the destination availability domain.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`boot_volume_replica_id`

(required) The boot volume replica's Oracle ID (OCID).

`availability_domain`

(required) The availability domain of the boot volume replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_INFO_TBL Type

Nested table type of dbms_cloud_oci_core_boot_volume_replica_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_AUTOTUNE_POLICY_TBL Type

Nested table type of dbms_cloud_oci_core_autotune_policy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_T Type

A detachable boot volume device that contains the image used to boot a Compute instance. For more information, see[Overview of Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the boot volume. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the boot volume.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The boot volume's Oracle ID (OCID).

`image_id`

(optional) The image OCID used to create the boot volume.

`is_hydrated`

(optional) Specifies whether the boot volume's data has finished copying from the source boot volume or boot volume backup.

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this boot volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`lifecycle_state`

(required) The current state of a boot volume.

Allowed values are: 'PROVISIONING', 'RESTORING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY'

`size_in_g_bs`

(optional) The size of the boot volume in GBs.

`size_in_m_bs`

(required) The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Please use sizeInGBs.

`source_details`

(optional)

`time_created`

(required) The date and time the boot volume was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`volume_group_id`

(optional) The OCID of the source volume group.

`kms_key_id`

(optional) The OCID of the Vault service master encryption key assigned to the boot volume.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`auto_tuned_vpus_per_gb`

(optional) The number of Volume Performance Units per GB that this boot volume is effectively tuned to.

`boot_volume_replicas`

(optional) The list of boot volume replicas of this boot volume

`autotune_policies`

(optional) The list of autotune policies enabled for this volume.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_ATTACHMENT_T Type

Represents an attachment between a boot volume and an instance. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of an instance. Example: `Uocm:PHX-AD-1`

`boot_volume_id`

(required) The OCID of the boot volume.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The OCID of the boot volume attachment.

`instance_id`

(required) The OCID of the instance the boot volume is attached to.

`lifecycle_state`

(required) The current state of the boot volume attachment.

Allowed values are: 'ATTACHING', 'ATTACHED', 'DETACHING', 'DETACHED'

`time_created`

(required) The date and time the boot volume was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`is_pv_encryption_in_transit_enabled`

(optional) Whether in-transit encryption for the boot volume's paravirtualized attachment is enabled or not.

`encryption_in_transit_type`

(optional) Refer the top-level definition of encryptionInTransitType. The default value is NONE.

Allowed values are: 'NONE', 'BM_ENCRYPTION_IN_TRANSIT'

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_BACKUP_T Type

A point-in-time copy of a boot volume that can then be used to create a new boot volume or recover a boot volume. For more information, see[Overview of Boot Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm)To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`boot_volume_id`

(optional) The OCID of the boot volume.

`compartment_id`

(required) The OCID of the compartment that contains the boot volume backup.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`expiration_time`

(optional) The date and time the volume backup will expire and be automatically deleted. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). This parameter will always be present for backups that were created automatically by a scheduled-backup policy. For manually created backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the boot volume backup.

`image_id`

(optional) The image OCID used to create the boot volume the backup is taken from.

`kms_key_id`

(optional) The OCID of the Vault service master encryption assigned to the boot volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

`lifecycle_state`

(required) The current state of a boot volume backup.

Allowed values are: 'CREATING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY', 'REQUEST_RECEIVED'

`size_in_g_bs`

(optional) The size of the boot volume, in GBs.

`source_boot_volume_backup_id`

(optional) The OCID of the source boot volume backup.

`source_type`

(optional) Specifies whether the backup was created manually, or via scheduled backup policy.

Allowed values are: 'MANUAL', 'SCHEDULED'

`time_created`

(required) The date and time the boot volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_request_received`

(optional) The date and time the request to create the boot volume backup was received. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`l_type`

(optional) The type of a volume backup.

Allowed values are: 'FULL', 'INCREMENTAL'

`unique_size_in_g_bs`

(optional) The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space consumed on the boot volume and whether the backup is full or incremental.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_KMS_KEY_T Type

The Vault service master encryption key associated with this volume.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the Vault service key assigned to this volume. If the volume is not using Vault service, then the `kmsKeyId` will be a null string.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_T Type

An asynchronous replica of a boot volume that can then be used to create a new boot volume or recover a boot volume. For more information, see[Overview of Cross-Region Volume Replication](https://docs.oracle.com/iaas/Content/Block/Concepts/volumereplication.htm)To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the boot volume replica. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the boot volume replica.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The boot volume replica's Oracle ID (OCID).

`lifecycle_state`

(required) The current state of a boot volume replica.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ACTIVATING', 'TERMINATING', 'TERMINATED', 'FAULTY'

`size_in_g_bs`

(required) The size of the source boot volume, in GBs.

`time_created`

(required) The date and time the boot volume replica was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_last_synced`

(required) The date and time the boot volume replica was last synced from the source boot volume. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`boot_volume_id`

(required) The OCID of the source boot volume.

`image_id`

(optional) The image OCID used to create the boot volume the replica is replicated from.

`total_data_transferred_in_g_bs`

(optional) The total size of the data transferred from the source boot volume to the boot volume replica, in GBs.

`volume_group_replica_id`

(optional) The OCID of the volume group replica.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_DETAILS_T Type

Contains the details for the boot volume replica

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`availability_domain`

(required) The availability domain of the boot volume replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_BACKUP_DETAILS_T Type

Specifies the boot volume backup.

Syntax
```

```

`dbms_cloud_oci_core_boot_volume_source_from_boot_volume_backup_details_t`is a subtype of the`dbms_cloud_oci_core_boot_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the boot volume backup.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_DETAILS_T Type

Specifies the source boot volume.

Syntax
```

```

`dbms_cloud_oci_core_boot_volume_source_from_boot_volume_details_t`is a subtype of the`dbms_cloud_oci_core_boot_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the boot volume.

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_REPLICA_DETAILS_T Type

Specifies the source boot volume replica which the boot volume will be created from. The boot volume replica shoulbe be in the same availability domain as the boot volume. Only one volume can be created from a replica at the same time.

Syntax
```

```

`dbms_cloud_oci_core_boot_volume_source_from_boot_volume_replica_details_t`is a subtype of the`dbms_cloud_oci_core_boot_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the boot volume replica.

### DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) An individual public IP prefix (CIDR) to add to the public virtual circuit. All prefix sizes are allowed.

### DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_create_virtual_circuit_public_prefix_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`public_prefixes`

(required) The public IP prefixes (CIDRs) to add to the public virtual circuit.

### DBMS_CLOUD_OCI_CORE_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) An individual public IP prefix (CIDR) to remove from the public virtual circuit.

### DBMS_CLOUD_OCI_CORE_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_delete_virtual_circuit_public_prefix_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`public_prefixes`

(required) The public IP prefixes (CIDRs) to remove from the public virtual circuit.

### DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_byoip_allocated_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_COLLECTION_T Type

Results of a `ListByoipAllocatedRanges` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of subranges of a BYOIP CIDR block allocated to an IP pool.

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_T Type

A summary of IPv6 prefix subranges currently allocated to a VCN.

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

(optional) The BYOIPv6 prefix range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 prefix. Each VCN allocation must be /64 or larger.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `Vcn` resource to which the ByoipRange belongs.

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_byoip_range_vcn_ipv6_allocation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource.

`ipv6_cidr_block`

(optional) The IPv6 prefix being imported to the Oracle cloud. This prefix must be /48 or larger, and can be subdivided into sub-ranges used across multiple VCNs. A BYOIPv6 prefix can be also assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.

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

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_SUMMARY_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource.

`ipv6_cidr_block`

(optional) The IPv6 prefix being imported to the Oracle cloud. This prefix must be /48 or larger, and can be subdivided into sub-ranges used across multiple VCNs. A BYOIPv6 prefix can be assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.

`lifecycle_state`

(optional) The `ByoipRange` resource's current state.

`lifecycle_details`

(optional) The Byoip Range's current lifeCycle substate.

`time_created`

(optional) The date and time the `ByoipRange` resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_byoip_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_COLLECTION_T Type

The results returned by a `ListByoipRange` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of `ByoipRange` resource summaries.

### DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_INSTANCE_SHAPE_CONFIG_T Type

The shape configuration for a shape in a capacity report.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

`nvmes`

(optional) The number of NVMe drives to be used for storage.

### DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_SHAPE_AVAILABILITY_T Type

Information about the available capacity for a shape.

Syntax
```

```

Fields

Field Description

`fault_domain`

(optional) The fault domain for the capacity report. If you do not specify the fault domain, the capacity report includes information about all fault domains.

`instance_shape`

(optional) The shape that the capacity report was requested for.

`instance_shape_config`

(optional)

`available_count`

(optional) The total number of new instances that can be created with the specified shape configuration.

`availability_status`

(optional) A flag denoting whether capacity is available.

Allowed values are: 'OUT_OF_HOST_CAPACITY', 'HARDWARE_NOT_SUPPORTED', 'AVAILABLE'

### DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested when launching instances in a compute capacity reservation. If the parameter is provided, the reservation is created with the resources that you specify. If some properties are missing or the parameter is not provided, the reservation is created with the default configuration values for the `shape` that you specify. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned. For more information about customizing the resources that are allocated to flexible shapes, see[Flexible Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#flexible).

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

### DBMS_CLOUD_OCI_CORE_CAPACITY_RESERVATION_INSTANCE_SUMMARY_T Type

Condensed instance data when listing instances in a compute capacity reservation.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the instance.

`availability_domain`

(required) The availability domain the instance is running in.

`compartment_id`

(required) The OCID of the compartment that contains the instance.

`fault_domain`

(optional) The fault domain the instance is running in.

`shape_config`

(optional)

`shape`

(required) The shape of the instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can enumerate all available shapes by calling`LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPES`Function.

### DBMS_CLOUD_OCI_CORE_CAPACITY_SOURCE_T Type

A capacity source of bare metal hosts.

Syntax
```

```

Fields

Field Description

`capacity_type`

(required) The capacity type of bare metal hosts.

Allowed values are: 'DEDICATED'

### DBMS_CLOUD_OCI_CORE_CAPTURE_CONSOLE_HISTORY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_id`

(required) The OCID of the instance to get the console history from.

### DBMS_CLOUD_OCI_CORE_VTAP_CAPTURE_FILTER_RULE_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_T Type

The set of rules governing what traffic the VCN flow log collects.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Indicates whether a VCN flow log capture filter rule is enabled.

`priority`

(optional) A lower number indicates a higher priority, range 0-9. Each rule must have a distinct priority.

`sampling_rate`

(optional) Sampling interval as `1` of `X`, where `X` is an integer not greater than `100000`.

`source_cidr`

(optional) Traffic from this CIDR will be captured in the VCN flow log.

`destination_cidr`

(optional) Traffic to this CIDR will be captured in the VCN flow log.

`protocol`

(optional) The transport protocol the filter uses.

`icmp_options`

(optional)

`tcp_options`

(optional)

`udp_options`

(optional)

`flow_log_type`

(optional) Type or types of VCN flow logs to store. `ALL` includes records for both accepted traffic and rejected traffic.

Allowed values are: 'ALL', 'REJECT', 'ACCEPT'

`rule_action`

(optional) Include or exclude a `ruleAction` object.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_CORE_VTAP_CAPTURE_FILTER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_vtap_capture_filter_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_flow_log_capture_filter_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CAPTURE_FILTER_T Type

A capture filter contains a set of *`CAPTURE_FILTER_RULE_DETAILS`Function* governing what traffic is mirrored for a *`VTAP`Type* or captured for a *[VCN Flow Log](https://docs.oracle.com/iaas/Content/Network/Concepts/vcn-flow-logs.htm)*. The capture filter is created with no rules defined, and it must have at least one rule to mirror traffic for the VTAP or collect VCN flow logs.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the capture filter.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

(optional) The set of rules governing what traffic the VCN flow log collects.

### DBMS_CLOUD_OCI_CORE_CHANGE_BOOT_VOLUME_BACKUP_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the boot volume backup to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the boot volume backup to.

### DBMS_CLOUD_OCI_CORE_CHANGE_BOOT_VOLUME_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the boot volume to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the boot volume to.

### DBMS_CLOUD_OCI_CORE_CHANGE_BYOIP_RANGE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the BYOIP CIDR block move.

### DBMS_CLOUD_OCI_CORE_CHANGE_CAPTURE_FILTER_COMPARTMENT_DETAILS_T Type

These configuration details are used in the move operation when changing the compartment containing a capture filter.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the VTAP capture filter move.

### DBMS_CLOUD_OCI_CORE_CHANGE_CLUSTER_NETWORK_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CAPACITY_RESERVATION_COMPARTMENT_DETAILS_T Type

Specifies the compartment to move the compute capacity reservation to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the compute capacity reservation to.

### DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CAPACITY_TOPOLOGY_COMPARTMENT_DETAILS_T Type

Specifies the compartment to move the compute capacity topology to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the compute capacity topology to.

### DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the compute cluster to.

### DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the instance configuration to.

### DBMS_CLOUD_OCI_CORE_CHANGE_CPE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the CPE object to.

### DBMS_CLOUD_OCI_CORE_CHANGE_CROSS_CONNECT_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the cross-connect to.

### DBMS_CLOUD_OCI_CORE_CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the cross-connect group to.

### DBMS_CLOUD_OCI_CORE_CHANGE_DEDICATED_VM_HOST_COMPARTMENT_DETAILS_T Type

Specifies the compartment to move the dedicated virtual machine host to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the dedicated virtual machine host to.

### DBMS_CLOUD_OCI_CORE_CHANGE_DHCP_OPTIONS_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the set of DHCP options to.

### DBMS_CLOUD_OCI_CORE_CHANGE_DRG_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the DRG to.

### DBMS_CLOUD_OCI_CORE_CHANGE_IP_SEC_CONNECTION_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the IPSec connection to.

### DBMS_CLOUD_OCI_CORE_CHANGE_IMAGE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the image to.

### DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the instance to.

### DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_CONFIGURATION_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the instance configuration to.

### DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_POOL_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the instance pool to.

### DBMS_CLOUD_OCI_CORE_CHANGE_INTERNET_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the internet gateway to.

### DBMS_CLOUD_OCI_CORE_CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the local peering gateway to.

### DBMS_CLOUD_OCI_CORE_CHANGE_NAT_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the NAT gateway to.

### DBMS_CLOUD_OCI_CORE_CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the network security group to.

### DBMS_CLOUD_OCI_CORE_CHANGE_PUBLIC_IP_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the public IP to.

### DBMS_CLOUD_OCI_CORE_CHANGE_PUBLIC_IP_POOL_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the public IP pool move.

### DBMS_CLOUD_OCI_CORE_CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the remote peering connection to.

### DBMS_CLOUD_OCI_CORE_CHANGE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the route table to.

### DBMS_CLOUD_OCI_CORE_CHANGE_SECURITY_LIST_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the security list to.

### DBMS_CLOUD_OCI_CORE_CHANGE_SERVICE_GATEWAY_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the service gateway to.

### DBMS_CLOUD_OCI_CORE_CHANGE_SUBNET_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the subnet to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VCN_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the VCN to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the virtual circuit to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VLAN_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the VLAN to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_BACKUP_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the volume backup to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the volume backup to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the volume to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the volume to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_GROUP_BACKUP_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the volume group backup to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the volume group backup to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_GROUP_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the volume group to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the volume group to.

### DBMS_CLOUD_OCI_CORE_CHANGE_VTAP_COMPARTMENT_DETAILS_T Type

These configuration details are used in the move operation when changing the compartment containing a virtual test access point (VTAP).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment for the VTAP move.

### DBMS_CLOUD_OCI_CORE_CLUSTER_CONFIG_DETAILS_T Type

The HPC cluster configuration requested when launching instances in a compute capacity reservation. If the parameter is provided, the reservation is created with the HPC island and a list of HPC blocks that you specify. If a list of HPC blocks are missing or not provided, the reservation is created with any HPC blocks in the HPC island that you specify. If the values of HPC island or HPC block that you provide are not valid, an error is returned.

Syntax
```

```

Fields

Field Description

`hpc_island_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HPC island.

`network_block_ids`

(optional) The list of OCIDs of the network blocks.

### DBMS_CLOUD_OCI_CORE_CLUSTER_CONFIGURATION_DETAILS_T Type

The HPC cluster configuration requested when launching instances of a cluster network. If the parameter is provided, instances will only be placed within the HPC island and list of network blocks that you specify. If a list of network blocks are missing or not provided, the instances will be placed in any HPC blocks in the HPC island that you specify. If the values of HPC island or network block that you provide are not valid, an error is returned.

Syntax
```

```

Fields

Field Description

`network_block_ids`

(optional) The list of network block OCIDs.

`hpc_island_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HPC island.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_IPV6_ADDRESS_IPV6_SUBNET_CIDR_DETAILS_T Type

Optional. Used to specify from which subnet prefixes an IPv6 address should be allocated, or to assign valid available IPv6 addresses.

Syntax
```

```

Fields

Field Description

`ipv6_subnet_cidr`

(optional) Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_IPV6_ADDRESS_IPV6_SUBNET_CIDR_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_placement_ipv6_address_ipv6_subnet_cidr_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_PRIMARY_SUBNET_T Type

Details about the IPv6 primary subnet.

Syntax
```

```

Fields

Field Description

`is_assign_ipv6_ip`

(optional) Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled subnet. Default: False. When provided you may optionally provide an IPv6 prefix (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr` is not provided then an IPv6 prefix is chosen for you.

`ipv6_address_ipv6_subnet_cidr_pair_details`

(optional) A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address. You can provide only the prefix ranges and OCI will select an available address from the range. You can optionally choose to leave the prefix range empty and instead provide the specific IPv6 address that should be used from within that range.

`subnet_id`

(required) The subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the secondary VNIC.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SECONDARY_VNIC_SUBNET_T Type

The secondary VNIC object for the placement configuration for an instance pool.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the VNIC. This is also used to match against the instance configuration defined secondary VNIC.

`is_assign_ipv6_ip`

(optional) Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled subnet. Default: False. When provided you may optionally provide an IPv6 prefix (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr` is not provided then an IPv6 prefix is chosen for you.

`ipv6_address_ipv6_subnet_cidr_pair_details`

(optional) A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address. You can provide only the prefix ranges and OCI will select an available address from the range. You can optionally choose to leave the prefix range empty and instead provide the specific IPv6 address that should be used from within that range.

`subnet_id`

(required) The subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the secondary VNIC.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SECONDARY_VNIC_SUBNET_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_placement_secondary_vnic_subnet_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_T Type

The location for where an instance pool will place instances.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to place instances. Example: `Uocm:PHX-AD-1`

`primary_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary subnet in which to place instances. This field is deprecated. Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.

`fault_domains`

(optional) The fault domains to place instances. If you don't provide any values, the system makes a best effort to distribute instances across all fault domains based on capacity. To distribute the instances evenly across selected fault domains, provide a set of fault domains. For example, you might want instances to be evenly distributed if your applications require high availability. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`

`primary_vnic_subnets`

(optional)

`secondary_vnic_subnets`

(optional) The set of secondary VNIC data for instances in the pool.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_LOAD_BALANCER_ATTACHMENT_T Type

Represents a load balancer that is attached to an instance pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer attachment.

`instance_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance pool of the load balancer attachment.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer attached to the instance pool.

`backend_set_name`

(required) The name of the backend set on the load balancer.

`port`

(required) The port value used for the backends.

`vnic_selection`

(required) Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer. Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance pool.

`lifecycle_state`

(required) The status of the interaction between the instance pool and the load balancer.

Allowed values are: 'ATTACHING', 'ATTACHED', 'DETACHING', 'DETACHED'

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_placement_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_LOAD_BALANCER_ATTACHMENT_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_load_balancer_attachment_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_T Type

An instance pool is a set of instances within the same region that are managed as a group. For more information about instance pools and instance configurations, see[Managing Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance pool.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the instance pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration associated with the instance pool.

`lifecycle_state`

(required) The current state of the instance pool.

Allowed values are: 'PROVISIONING', 'SCALING', 'STARTING', 'STOPPING', 'TERMINATING', 'STOPPED', 'TERMINATED', 'RUNNING'

`placement_configurations`

(required) The placement configurations for the instance pool.

`l_size`

(required) The number of instances that should be in the instance pool.

`time_created`

(required) The date and time the instance pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`load_balancers`

(optional) The load balancers attached to the instance pool.

`instance_display_name_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance displaynames follow the format. The formatter does not retroactively change instance's displaynames, only instance displaynames in the future follow the format

`instance_hostname_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance hostnames follow the format. The formatter does not retroactively change instance's hostnames, only instance hostnames in the future follow the format

### DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_PLACEMENT_CONFIGURATION_DETAILS_T Type

The location for where the instance pools in a cluster network will place instances.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to place instances. Example: `Uocm:PHX-AD-1`

`placement_constraint`

(optional) The placement constraint when reserving hosts.

Allowed values are: 'SINGLE_TIER', 'SINGLE_BLOCK', 'PACKED_DISTRIBUTION_MULTI_BLOCK'

`primary_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary subnet to place instances. This field is deprecated. Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.

`primary_vnic_subnets`

(optional)

`secondary_vnic_subnets`

(optional) The set of secondary VNIC data for instances in the pool.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_T Type

A cluster network is a group of high performance computing (HPC), GPU, or optimized bare metal instances that are connected with an ultra low-latency remote direct memory access (RDMA) network.[Cluster networks with instance pools](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm)use instance pools to manage groups of identical instances. Use cluster networks with instance pools when you want predictable capacity for a specific number of identical instances that are managed as a group. If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, use compute clusters instead. For details, see`COMPUTE_CLUSTER`Type.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cluster network.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cluster network.

`hpc_island_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HPC island used by the cluster network.

`network_block_ids`

(optional) The list of network block OCIDs of the HPC island.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_pools`

(optional) The instance pools in the cluster network. Each cluster network can have one instance pool.

`placement_configuration`

(optional)

`lifecycle_state`

(required) The current state of the cluster network.

Allowed values are: 'PROVISIONING', 'SCALING', 'STARTING', 'STOPPING', 'TERMINATING', 'STOPPED', 'TERMINATED', 'RUNNING'

`time_created`

(required) The date and time the resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_SUMMARY_T Type

Summary information for an instance pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the instance pool.

`compartment_id`

(required) The OCID of the compartment containing the instance pool.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`instance_configuration_id`

(required) The OCID of the instance configuration associated with the instance pool.

`lifecycle_state`

(required) The current state of the instance pool.

Allowed values are: 'PROVISIONING', 'SCALING', 'STARTING', 'STOPPING', 'TERMINATING', 'STOPPED', 'TERMINATED', 'RUNNING'

`availability_domains`

(required) The availability domains for the instance pool.

`l_size`

(required) The number of instances that should be in the instance pool.

`time_created`

(required) The date and time the instance pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_SUMMARY_T Type

Summary information for a[cluster network with instance pools](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cluster network.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cluster netowrk.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_pools`

(optional) The instance pools in the cluster network.

`lifecycle_state`

(required) The current state of the cluster network.

Allowed values are: 'PROVISIONING', 'SCALING', 'STARTING', 'STOPPING', 'TERMINATING', 'STOPPED', 'TERMINATED', 'RUNNING'

`time_created`

(required) The date and time the resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPARTMENT_INTERNAL_T Type

Helper definition required to perform authZ using SPLAT expressions on a Compartment

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_T Type

A compute bare metal host.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`compute_hpc_island_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`compute_local_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute local block.

`compute_network_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute network block.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute bare metal host.

`instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute instance that runs on the compute bare metal host.

`instance_shape`

(required) The shape of the compute instance that runs on the compute bare metal host.

`lifecycle_details`

(optional) The lifecycle state details of the compute bare metal host.

Allowed values are: 'AVAILABLE', 'DEGRADED', 'UNAVAILABLE'

`lifecycle_state`

(required) The current state of the compute bare metal host.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time that the compute bare metal host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute bare metal host was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_SUMMARY_T Type

Summary information for a compute bare metal host.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`compute_hpc_island_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`compute_local_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute network block.

`compute_network_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute local block.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute bare metal host.

`instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute instance that runs on the compute bare metal host.

`instance_shape`

(required) The shape of the compute instance that runs on the compute bare metal host.

`lifecycle_details`

(optional) The lifecycle state details of the compute bare metal host.

`lifecycle_state`

(required) The current state of the compute bare metal host.

`time_created`

(required) The date and time that the compute bare metal host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute bare metal host was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_compute_bare_metal_host_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_COLLECTION_T Type

A list of compute bare metal hosts.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of compute bare metal hosts.

### DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_SHAPE_AVAILABILITY_TBL Type

Nested table type of dbms_cloud_oci_core_capacity_report_shape_availability_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_REPORT_T Type

A report of the host capacity within an availability domain that is available for you to create compute instances. Host capacity is the physical infrastructure that resources such as compute instances run on. Use the capacity report to determine whether sufficient capacity is available for a shape before you create an instance or change the shape of an instance.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment. This should always be the root compartment.

`availability_domain`

(required) The availability domain for the capacity report. Example: `Uocm:PHX-AD-1`

`shape_availabilities`

(required) Information about the available capacity for each shape in a capacity report.

`time_created`

(required) The date and time the capacity report was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_T Type

Data that defines the capacity configuration.

Syntax
```

```

Fields

Field Description

`fault_domain`

(optional) The fault domain of this capacity configuration. If a value is not supplied, this capacity configuration is applicable to all fault domains in the specified availability domain. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).

`cluster_config`

(optional)

`instance_shape`

(required) The shape to use when launching instances using compute capacity reservations. The shape determines the number of CPUs, the amount of memory, and other resources allocated to the instance. You can list all available shapes by calling`LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPES`Type.

`instance_shape_config`

(optional)

`reserved_count`

(required) The total number of instances that can be launched from the capacity configuration.

`used_count`

(required) The amount of capacity in use out of the total capacity reserved in this capacity configuration.

### DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_core_instance_reservation_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_T Type

A template that defines the settings to use when creating compute capacity reservations.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the compute capacity reservation. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the compute capacity reservation.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity reservation.

`is_default_reservation`

(optional) Whether this capacity reservation is the default. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`instance_reservation_configs`

(optional) The capacity configurations for the capacity reservation. To use the reservation for the desired shape, specify the shape, count, and optionally the fault domain where you want this configuration.

`lifecycle_state`

(required) The current state of the compute capacity reservation.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'MOVING', 'DELETED', 'DELETING'

`reserved_instance_count`

(optional) The number of instances for which capacity will be held with this compute capacity reservation. This number is the sum of the values of the `reservedCount` fields for all of the instance capacity configurations under this reservation. The purpose of this field is to calculate the percentage usage of the reservation.

`time_updated`

(optional) The date and time the compute capacity reservation was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_created`

(required) The date and time the compute capacity reservation was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`used_instance_count`

(optional) The total number of instances currently consuming space in this compute capacity reservation. This number is the sum of the values of the `usedCount` fields for all of the instance capacity configurations under this reservation. The purpose of this field is to calculate the percentage usage of the reservation.

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPE_SUMMARY_T Type

An available shape used to launch instances in a compute capacity reservation.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The shape's availability domain.

`instance_shape`

(required) The name of the available shape used to launch instances in a compute capacity reservation.

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_SUMMARY_T Type

Summary information for a compute capacity reservation.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the instance reservation configuration.

`compartment_id`

(optional) The OCID of the compartment.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`lifecycle_state`

(optional) The current state of the capacity reservation.

`availability_domain`

(required) The availability domain of the capacity reservation.

`reserved_instance_count`

(optional) The number of instances for which capacity will be held in this compute capacity reservation. This number is the sum of the values of the `reservedCount` fields for all of the instance capacity configurations under this reservation. The purpose of this field is to calculate the percentage usage of the reservation.

`used_instance_count`

(optional) The total number of instances currently consuming space in this compute capacity reservation. This number is the sum of the values of the `usedCount` fields for all of the instance capacity configurations under this reservation. The purpose of this field is to calculate the percentage usage of the reservation.

`is_default_reservation`

(optional) Whether this capacity reservation is the default. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`time_created`

(required) The date and time the capacity reservation was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_T Type

A compute capacity topology that allows you to query your bare metal hosts and their RDMA network topology.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the compute capacity topology. Example: `Uocm:US-CHICAGO-1-AD-2`

`capacity_source`

(required)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the compute capacity topology.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`lifecycle_state`

(required) The current state of the compute capacity topology.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'DELETED', 'DELETING'

`time_created`

(required) The date and time that the compute capacity topology was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute capacity topology was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_SUMMARY_T Type

Summary information for a compute capacity topology.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the compute capacity topology. Example: `Uocm:US-CHICAGO-1-AD-2`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the compute capacity topology.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`lifecycle_state`

(required) The current state of the compute capacity topology.

`time_created`

(required) The date and time that the compute capacity topology was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute capacity topology was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_compute_capacity_topology_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_COLLECTION_T Type

A list of compute capacity topologies.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of compute capacity topologies.

### DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_T Type

A remote direct memory access (RDMA) network group. A cluster network on a[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a group of high performance computing (HPC), GPU, or optimized instances that are connected with an ultra low-latency network. Use compute clusters when you want to manage instances in the cluster individually, or when you want to use different types of instances in the RDMA network group. For details about cluster networks that use instance pools to manage groups of identical instances, see`CLUSTER_NETWORK`Type.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the compute cluster is running in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the compute cluster.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster.

`lifecycle_state`

(required) The current state of the compute cluster.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) The date and time the compute cluster was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_SUMMARY_T Type

Summary information for a compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the compute cluster is running in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the compute cluster.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster.

`lifecycle_state`

(required) The current state of the compute cluster.

`time_created`

(required) The date and time the compute cluster was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_compute_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_COLLECTION_T Type

A list of compute clusters that match filter criteria, if any. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of compute clusters.

### DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_T Type

Compute Global Image Capability Schema is a container for a set of compute global image capability schema versions

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute global image capability schema

`compartment_id`

(optional) The OCID of the compartment that contains the resource.

`current_version_name`

(optional) The name of the global capabilities version resource that is considered the current version.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(required) The date and time the compute global image capability schema was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_SUMMARY_T Type

Summary information for a compute global image capability schema

Syntax
```

```

Fields

Field Description

`id`

(required) The compute global image capability schema[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The OCID of the compartment containing the compute global image capability schema

`current_version_name`

(optional) The name of the global capabilities version resource that is considered the current version.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(required) The date and time the compute global image capability schema was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION_T Type

Compute Global Image Capability Schema Version is a set of all possible capabilities for a collection of images.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the compute global image capability schema version

`compute_global_image_capability_schema_id`

(required) The ocid of the compute global image capability schema

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`schema_data`

(required) The map of each capability name to its ImageCapabilityDescriptor.

`time_created`

(required) The date and time the compute global image capability schema version was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION_SUMMARY_T Type

Summary information for a compute global image capability schema

Syntax
```

```

Fields

Field Description

`name`

(required) The compute global image capability schema version name

`compute_global_image_capability_schema_id`

(required) The OCID of the compute global image capability schema

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(required) The date and time the compute global image capability schema version was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_T Type

A compute HPC island.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`lifecycle_state`

(required) The current state of the compute HPC island.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time that the compute HPC island was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute HPC island was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`total_compute_bare_metal_host_count`

(required) The total number of compute bare metal hosts located in this compute HPC island.

### DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_SUMMARY_T Type

Summary information for a compute HPC island.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`lifecycle_state`

(required) The current state of the compute HPC island.

`time_created`

(required) The date and time that the compute HPC island was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute HPC island was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`total_compute_bare_metal_host_count`

(required) The total number of compute bare metal hosts located in this compute HPC island.

### DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_compute_hpc_island_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_COLLECTION_T Type

A list of compute HPC islands.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of compute HPC islands.

### DBMS_CLOUD_OCI_CORE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_T Type

Compute Image Capability Schema is a set of capabilities that filter the compute global capability schema version for an image.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the compute global image capability schema version

`compartment_id`

(optional) The OCID of the compartment that contains the resource.

`compute_global_image_capability_schema_id`

(required) The ocid of the compute global image capability schema

`compute_global_image_capability_schema_version_name`

(required) The name of the compute global image capability schema version

`image_id`

(required) The OCID of the image associated with this compute image capability schema

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`schema_data`

(required) The map of each capability name to its ImageCapabilityDescriptor.

`time_created`

(required) The date and time the compute image capability schema was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_SUMMARY_T Type

Summary information for a compute image capability schema

Syntax
```

```

Fields

Field Description

`id`

(required) The compute image capability schema[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The OCID of the compartment containing the compute global image capability schema

`compute_global_image_capability_schema_version_name`

(required) The name of the compute global image capability schema version

`image_id`

(required) The OCID of the image associated with this compute image capability schema

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`schema_data`

(optional) A mapping of each capability name to its ImageCapabilityDescriptor.

`time_created`

(required) The date and time the compute image capability schema was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VOLUME_DETAILS_T Type

Volume attachmentDetails. Please see`ATTACH_VOLUME_DETAILS`Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`is_read_only`

(optional) Whether the attachment should be created in read-only mode.

`device`

(optional) The device name.

`is_shareable`

(optional) Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.

`l_type`

(required) The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_REPLICA_DETAILS_T Type

Contains the details for the block volume replica

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the block volume replica. You may optionally specify a *display name* for the block volume replica, otherwise a default is provided.

`availability_domain`

(required) The availability domain of the block volume replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AUTOTUNE_POLICY_T Type

An autotune policy automatically tunes the volume's performace based on the type of the policy.

Syntax
```

```

Fields

Field Description

`autotune_type`

(required) This specifies the type of autotunes supported by OCI.

Allowed values are: 'DETACHED_VOLUME', 'PERFORMANCE_BASED'

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_REPLICA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_configuration_block_volume_replica_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AUTOTUNE_POLICY_TBL Type

Nested table type of dbms_cloud_oci_core_instance_configuration_autotune_policy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_CREATE_VOLUME_DETAILS_T Type

Creates a new block volume. Please see`CREATE_VOLUME_DETAILS`Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain of the volume. Example: `Uocm:PHX-AD-1`

`backup_policy_id`

(optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.

`compartment_id`

(optional) The OCID of the compartment that contains the volume.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated. Use the `InstanceConfigurationDetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`block_volume_replicas`

(optional) The list of block volume replicas to be enabled for this volume in the specified destination availability domains.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The OCID of the Vault service key to assign as the master encryption key for the volume.

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `0`: Represents Lower Cost option. * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`size_in_g_bs`

(optional) The size of the volume in GBs.

`source_details`

(optional)

`autotune_policies`

(optional) The list of autotune policies enabled for this volume.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_DETAILS_T Type

Create new block volumes or attach to an existing volume. Specify either createDetails or volumeId.

Syntax
```

```

Fields

Field Description

`attach_details`

(optional)

`create_details`

(optional)

`volume_id`

(optional) The OCID of the volume.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_T Type

Optional. Used to specify from which subnet prefixes an IPv6 address should be allocated, or to assign valid available IPv6 addresses.

Syntax
```

```

Fields

Field Description

`ipv6_subnet_cidr`

(optional) Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.

`ipv6_address`

(optional) Optional. An available IPv6 address of your subnet from a valid IPv6 prefix on the subnet (otherwise the IP address is automatically assigned).

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_configuration_ipv6_address_ipv6_subnet_cidr_pair_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_CREATE_VNIC_DETAILS_T Type

Contains the properties of the VNIC for an instance configuration. See`CREATE_VNIC_DETAILS`Type and[Instance Configurations](https://docs.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm#config)for more information.

Syntax
```

```

Fields

Field Description

`assign_ipv6_ip`

(optional) Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled subnet. Default: False. When provided you may optionally provide an IPv6 prefix (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr` is not provided then an IPv6 prefix is chosen for you.

`assign_public_ip`

(optional) Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of`CREATE_VNIC_DETAILS`Type for more information.

`assign_private_dns_record`

(optional) Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of`CREATE_VNIC_DETAILS`Type for more information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ipv6_address_ipv6_subnet_cidr_pair_details`

(optional) A list of IPv6 prefixes from which the VNIC should be assigned an IPv6 address. You can provide only the prefix and OCI selects an available address from the range. You can optionally choose to leave the prefix range empty and instead provide the specific IPv6 address that should be used from within that range.

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. See the `hostnameLabel` attribute of`CREATE_VNIC_DETAILS`Type for more information.

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`private_ip`

(optional) A private IP address of your choice to assign to the VNIC. See the `privateIp` attribute of`CREATE_VNIC_DETAILS`Type for more information.

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. See the `skipSourceDestCheck` attribute of`CREATE_VNIC_DETAILS`Type for more information.

`subnet_id`

(optional) The OCID of the subnet to create the VNIC in. See the `subnetId` attribute of`CREATE_VNIC_DETAILS`Type for more information.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested for the instance. If the parameter is provided, the instance is created with the resources that you specify. If some properties are missing or the entire parameter is not provided, the instance is created with the default configuration values for the `shape` that you specify. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`vcpus`

(optional) The total number of VCPUs available to the instance. This can be used instead of OCPUs, in which case the actual number of OCPUs will be calculated based on this value and the actual hardware. This must be a multiple of 2.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

`baseline_ocpu_utilization`

(optional) The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`. The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

`nvmes`

(optional) The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration requested for the instance. If you provide the parameter, the instance is created with the platform configuration that you specify. For any values that you omit, the instance uses the default configuration values for the `shape` that you specify. If you don't provide the parameter, the default values for the `shape` are used. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of platform being configured.

Allowed values are: 'AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM', 'AMD_ROME_BM_GPU', 'GENERIC_BM', 'INTEL_ICELAKE_BM', 'INTEL_SKYLAKE_BM', 'AMD_VM', 'INTEL_VM'

`is_secure_boot_enabled`

(optional) Whether Secure Boot is enabled on the instance.

`is_trusted_platform_module_enabled`

(optional) Whether the Trusted Platform Module (TPM) is enabled on the instance.

`is_measured_boot_enabled`

(optional) Whether the Measured Boot feature is enabled on the instance.

`is_memory_encryption_enabled`

(optional) Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default value is `false`.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_OPTIONS_T Type

Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.

Syntax
```

```

Fields

Field Description

`boot_volume_type`

(optional) Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.

Allowed values are: 'ISCSI', 'SCSI', 'IDE', 'VFIO', 'PARAVIRTUALIZED'

`firmware`

(optional) Firmware used to boot VM. Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the default for platform images.

Allowed values are: 'BIOS', 'UEFI_64'

`network_type`

(optional) Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

Allowed values are: 'E1000', 'VFIO', 'PARAVIRTUALIZED'

`remote_data_volume_type`

(optional) Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.

Allowed values are: 'ISCSI', 'SCSI', 'IDE', 'VFIO', 'PARAVIRTUALIZED'

`is_pv_encryption_in_transit_enabled`

(optional) Deprecated. Instead use `isPvEncryptionInTransitEnabled` in`INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_DETAILS`Function.

`is_consistent_volume_naming_enabled`

(optional) Whether to enable consistent volume naming feature. Defaults to false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_T Type

The configuration of plugins associated with this instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`desired_state`

(required) Whether the plugin should be enabled or disabled. To enable the monitoring and management plugins, the `isMonitoringDisabled` and `isManagementDisabled` attributes must also be set to false.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_agent_plugin_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type

Configuration options for the Oracle Cloud Agent software running on the instance.

Syntax
```

```

Fields

Field Description

`is_monitoring_disabled`

(optional) Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. Default value is false (monitoring plugins are enabled). These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.

`is_management_disabled`

(optional) Whether Oracle Cloud Agent can run all the available management plugins. Default value is false (management plugins are enabled). These are the management plugins: OS Management Service Agent and Compute Instance Run Command. The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.

`are_all_plugins_disabled`

(optional) Whether Oracle Cloud Agent can run all the available plugins. This includes the management and monitoring plugins. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`plugins_config`

(optional) The configuration of plugins associated with this instance.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_OPTIONS_T Type

Optional mutable instance options. As a part of Instance Metadata Service Security Header, This allows user to disable the legacy imds endpoints.

Syntax
```

```

Fields

Field Description

`are_legacy_imds_endpoints_disabled`

(optional) Whether to disable the legacy (/v1) instance metadata service endpoints. Customers who have migrated to /v2 should set this to true for added security. Default is false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AVAILABILITY_CONFIG_T Type

Options for defining the availabiity of a VM instance after a maintenance event that impacts the underlying hardware.

Syntax
```

```

Fields

Field Description

`is_live_migration_preferred`

(optional) Whether to live migrate supported VM instances to a healthy physical VM host without disrupting running instances during infrastructure maintenance events. If null, Oracle chooses the best option for migrating the VM during infrastructure maintenance events.

`recovery_action`

(optional) The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.

Allowed values are: 'RESTORE_INSTANCE', 'STOP_INSTANCE'

### DBMS_CLOUD_OCI_CORE_PREEMPTION_ACTION_T Type

The action to run when the preemptible instance is interrupted for eviction.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of action to run when the instance is interrupted for eviction.

Allowed values are: 'TERMINATE'

### DBMS_CLOUD_OCI_CORE_PREEMPTIBLE_INSTANCE_CONFIG_DETAILS_T Type

Configuration options for preemptible instances.

Syntax
```

```

Fields

Field Description

`preemption_action`

(required)

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_DETAILS_T Type

Instance launch details for creating an instance from an instance configuration. Use the `sourceDetails` parameter to specify whether a boot volume or an image should be used to launch a new instance. See`LAUNCH_INSTANCE_DETAILS`Type for more information.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain of the instance. Example: `Uocm:PHX-AD-1`

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation this instance is launched under.

`compartment_id`

(optional) The OCID of the compartment containing the instance. Instances created from instance configurations are placed in the same compartment as the instance that was used to create the instance configuration.

`create_vnic_details`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ipxe_script`

(optional) This is an advanced option. When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process. If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call. The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot. For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see[Bring Your Own Image](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm). For more information about iPXE, see http://ipxe.org.

`metadata`

(optional) Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance. A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to: * Provide information to[Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)to be used for various system initialization tasks. * Get information about the instance, including the custom metadata that you provide when you launch the instance. **Providing Cloud-Init Metadata** You can use the following metadata key names to provide information to Cloud-Init: **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the `authorized_keys` file, as shown in the example below. **\"user_data\"** - Provide your own base64-encoded data to be used by Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For information about how to take advantage of user data, see the[Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html). **Metadata Example** \"metadata\" : { \"quake_bot_level\" : \"Severe\", \"ssh_authorized_keys\" : \"ssh-rsa &lt;your_public_SSH_key&gt;== rsa-key-20160227\", \"user_data\" : \"&lt;your_public_SSH_key&gt;==\" } **Getting Metadata on the Instance** To get information about your instance, connect to the instance using SSH and issue any of the following GET requests: curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/ curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/ curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/&lt;any-key-name&gt; You'll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively. The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`shape`

(optional) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`shape_config`

(optional)

`platform_config`

(optional)

`source_details`

(optional)

`fault_domain`

(optional) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains. If you do not specify the fault domain, the system selects one for you. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`dedicated_vm_host_id`

(optional) The OCID of the dedicated virtual machine host to place the instance on. Dedicated VM hosts can be used when launching individual instances from an instance configuration. They cannot be used to launch instance pools.

`launch_mode`

(optional) Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

Allowed values are: 'NATIVE', 'EMULATED', 'PARAVIRTUALIZED', 'CUSTOM'

`launch_options`

(optional)

`agent_config`

(optional)

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.

`preferred_maintenance_action`

(optional) The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported. * `LIVE_MIGRATE` - Run maintenance using a live migration. * `REBOOT` - Run maintenance using a reboot.

Allowed values are: 'LIVE_MIGRATE', 'REBOOT'

`instance_options`

(optional)

`availability_config`

(optional)

`preemptible_instance_config`

(optional)

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VNIC_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`create_vnic_details`

(optional)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`nic_index`

(optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`instance_type`

(required) The type of instance details. Supported instanceType is compute

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_configuration_block_volume_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VNIC_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_configuration_attach_vnic_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_DETAILS_T Type

Compute Instance Configuration instance details.

Syntax
```

```

`dbms_cloud_oci_core_compute_instance_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_instance_details_t`type.

Fields

Field Description

`block_volumes`

(optional) Block volume parameters.

`launch_details`

(optional)

`secondary_vnics`

(optional) Secondary VNIC parameters.

### DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_compute_instance_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_OPTIONS_T Type

Multiple Compute Instance Configuration instance details.

Syntax
```

```

`dbms_cloud_oci_core_compute_instance_options_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_instance_details_t`type.

Fields

Field Description

`options`

(optional) The Compute Instance Configuration parameters.

### DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_T Type

A compute network block.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`compute_hpc_island_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute network block.

`lifecycle_state`

(required) The current state of the compute network block.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time that the compute network block was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute network block was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`total_compute_bare_metal_host_count`

(required) The total number of compute bare metal hosts located in this compute network block.

### DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_SUMMARY_T Type

Summary information for a compute network block.

Syntax
```

```

Fields

Field Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`compute_hpc_island_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute network block.

`lifecycle_state`

(required) The current state of the compute network block.

`time_created`

(required) The date and time that the compute network block was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time that the compute network block was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`total_compute_bare_metal_host_count`

(required) The total number of compute bare metal hosts located in the compute network block.

### DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_compute_network_block_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_COLLECTION_T Type

A list of compute network blocks.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of compute network blocks.

### DBMS_CLOUD_OCI_CORE_CONNECT_LOCAL_PEERING_GATEWAYS_DETAILS_T Type

Information about the other local peering gateway (LPG).

Syntax
```

```

Fields

Field Description

`peer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the LPG you want to peer with.

### DBMS_CLOUD_OCI_CORE_CONNECT_REMOTE_PEERING_CONNECTIONS_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_CONSOLE_HISTORY_T Type

An instance's serial console data. It includes configuration messages that occur when the instance boots, such as kernel and BIOS messages, and is useful for checking the status of the instance or diagnosing problems. The console data is minimally formatted ASCII text. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of an instance. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the console history metadata object.

`instance_id`

(required) The OCID of the instance this console history was fetched from.

`lifecycle_state`

(required) The current state of the console history.

Allowed values are: 'REQUESTED', 'GETTING-HISTORY', 'SUCCEEDED', 'FAILED'

`time_created`

(required) The date and time the history was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_COPY_BOOT_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`destination_region`

(required) The name of the destination region. Example: `us-ashburn-1`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`kms_key_id`

(optional) The OCID of the Vault service key in the destination region which will be the master encryption key for the copied boot volume backup. If you do not specify this attribute the boot volume backup will be encrypted with the Oracle-provided encryption key when it is copied to the destination region. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_COPY_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`destination_region`

(required) The name of the destination region. Example: `us-ashburn-1`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`kms_key_id`

(optional) The OCID of the Vault service key in the destination region which will be the master encryption key for the copied volume backup. If you do not specify this attribute the volume backup will be encrypted with the Oracle-provided encryption key when it is copied to the destination region. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_COPY_VOLUME_GROUP_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`destination_region`

(required) The name of the destination region. Example: `us-ashburn-1`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`kms_key_id`

(optional) The OCID of the Vault service key in the destination region which will be the master encryption key for the copied volume group backup. If you do not specify this attribute the volume group backup will be encrypted with the Oracle-provided encryption key when it is copied to the destination region. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_CPE_T Type

An object you create when setting up a Site-to-Site VPN between your on-premises network and VCN. The `Cpe` is a virtual representation of your customer-premises equipment, which is the actual router on-premises at your site at your end of the Site-to-Site VPN IPSec connection. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the CPE.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_ANSWER_T Type

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

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_QUESTION_T Type

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

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_INFO_T Type

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

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_QUESTION_TBL Type

Nested table type of dbms_cloud_oci_core_cpe_device_config_question_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_SHAPE_DETAIL_T Type

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

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_SHAPE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_APP_CATALOG_SUBSCRIPTION_DETAILS_T Type

details for creating a subscription for a listing resource version.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartmentID for the subscription.

`listing_id`

(required) The OCID of the listing.

`listing_resource_version`

(required) Listing resource version.

`oracle_terms_of_use_link`

(required) Oracle TOU link

`eula_link`

(optional) EULA link

`time_retrieved`

(required) Date and time the agreements were retrieved, in[RFC3339](https://tools.ietf.org/html/rfc3339)format. Example: `2018-03-20T12:32:53.532Z`

`signature`

(required) A generated signature for this listing resource version retrieved the agreements API.

### DBMS_CLOUD_OCI_CORE_CREATE_BOOT_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`boot_volume_id`

(required) The OCID of the boot volume that needs to be backed up.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`l_type`

(optional) The type of backup to create. If omitted, defaults to incremental.

Allowed values are: 'FULL', 'INCREMENTAL'

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_boot_volume_replica_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain of the volume. Omissible for cloning a volume. The new volume will be created in the availability domain of the source volume. Example: `Uocm:PHX-AD-1`

`backup_policy_id`

(optional) If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.

`compartment_id`

(required) The OCID of the compartment that contains the boot volume.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The OCID of the Vault service key to assign as the master encryption key for the boot volume.

`size_in_g_bs`

(optional) The size of the volume in GBs.

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents the Balanced option. * `20`: Represents the Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`source_details`

(required)

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`boot_volume_replicas`

(optional) The list of boot volume replicas to be enabled for this boot volume in the specified destination availability domains.

`autotune_policies`

(optional) The list of autotune policies to be enabled for this volume.

### DBMS_CLOUD_OCI_CORE_CREATE_BYOIP_RANGE_DETAILS_T Type

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

(optional) The BYOIPv6 prefix. You can assign some or all of it to a VCN after it is validated.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_REPORT_SHAPE_AVAILABILITY_DETAILS_T Type

Information about the shapes in a capacity report.

Syntax
```

```

Fields

Field Description

`fault_domain`

(optional) The fault domain for the capacity report. If you do not specify a fault domain, the capacity report includes information about all fault domains.

`instance_shape`

(required) The shape that you want to request a capacity report for. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`instance_shape_config`

(optional)

### DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_SOURCE_DETAILS_T Type

A capacity source of bare metal hosts.

Syntax
```

```

Fields

Field Description

`capacity_type`

(required) The capacity type of bare metal hosts.

### DBMS_CLOUD_OCI_CORE_CREATE_CAPTURE_FILTER_DETAILS_T Type

A capture filter contains a set of rules governing what traffic a VTAP mirrors or a VCN flow log collects.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the capture filter.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`filter_type`

(required) Indicates which service will use this capture filter

Allowed values are: 'VTAP', 'FLOWLOG'

`vtap_capture_filter_rules`

(optional) The set of rules governing what traffic a VTAP mirrors.

`flow_log_capture_filter_rules`

(optional) The set of rules governing what traffic the VCN flow log collects.

### DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_T Type

The data to create an instance pool in a cluster network.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration associated with the instance pool.

`l_size`

(required) The number of instances that should be in the instance pool.

### DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_create_cluster_network_instance_pool_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_DETAILS_T Type

The data to create a[cluster network with instance pools](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm). Use cluster networks with instance pools when you want predictable capacity for a specific number of identical instances that are managed as a group. For details about creating compute clusters, which let you manage instances in the RDMA network independently of each other or use different types of instances in the network group, see`CREATE_COMPUTE_CLUSTER_DETAILS`Function.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cluster network.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_pools`

(required) The data to create the instance pools in the cluster network. Each cluster network can have one instance pool.

`placement_configuration`

(required)

`cluster_configuration`

(optional)

### DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_REPORT_SHAPE_AVAILABILITY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_create_capacity_report_shape_availability_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_REPORT_DETAILS_T Type

The data to create a report of available Compute capacity.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment. This should always be the root compartment.

`availability_domain`

(required) The availability domain for the capacity report. Example: `Uocm:PHX-AD-1`

`shape_availabilities`

(required) Information about the shapes in the capacity report.

### DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_DETAILS_T Type

A template that contains the settings to use when defining the instance capacity configuration.

Syntax
```

```

Fields

Field Description

`instance_shape`

(required) The shape requested when launching instances using reserved capacity. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can list all available shapes by calling`LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPES`Type.

`instance_shape_config`

(optional)

`fault_domain`

(optional) The fault domain to use for instances created using this capacity configuration. For more information, see[Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). If you do not specify the fault domain, the capacity is available for an instance that does not specify a fault domain. To change the fault domain for a reservation, delete the reservation and create a new one in the preferred fault domain. To retrieve a list of fault domains, use the `ListFaultDomains` operation in the[Identity and Access Management Service API](https://docs.oracle.com/iaas/api/#/en/identity/20160918/). Example: `FAULT-DOMAIN-1`

`cluster_config`

(optional)

`reserved_count`

(required) The total number of instances that can be launched from the capacity configuration.

### DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_instance_reservation_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_RESERVATION_DETAILS_T Type

The details for creating a new compute capacity reservation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the capacity reservation.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`availability_domain`

(required) The availability domain of this compute capacity reservation. Example: `Uocm:PHX-AD-1`

`is_default_reservation`

(optional) Whether this capacity reservation is the default. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`instance_reservation_configs`

(optional) The capacity configurations for the capacity reservation. To use the reservation for the desired shape, specify the shape, count, and optionally the fault domain where you want this configuration.

### DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_TOPOLOGY_DETAILS_T Type

The details for creating a new compute capacity topology.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of this compute capacity topology. Example: `Uocm:US-CHICAGO-1-AD-2`

`capacity_source`

(required)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains this compute capacity topology.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CLUSTER_DETAILS_T Type

The data for creating a[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm). A compute cluster is an empty remote direct memory access (RDMA) network group After the compute cluster is created, you can use the compute cluster's OCID with the`LAUNCH_INSTANCE`Function operation to create instances in the compute cluster. The instances must be created in the same compartment and availability domain as the cluster. Use compute clusters when you want to manage instances in the cluster individually, or when you want to use different types of instances in the RDMA network group. For details about creating a cluster network that uses instance pools to manage groups of identical instances, see`CREATE_CLUSTER_NETWORK_DETAILS`Function.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to place the compute cluster in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_DETAILS_T Type

Create Image Capability Schema for an image.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the resource.

`compute_global_image_capability_schema_version_name`

(required) The name of the compute global image capability schema version

`image_id`

(required) The ocid of the image

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`schema_data`

(required) The map of each capability name to its ImageCapabilitySchemaDescriptor.

### DBMS_CLOUD_OCI_CORE_CREATE_CPE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the CPE.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ip_address`

(required) The public IP address of the on-premises router. Example: `203.0.113.2`

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device type. You can provide a value if you want to later generate CPE device configuration content for IPSec connections that use this CPE. You can also call`UPDATE_CPE`Function later to provide a value. For a list of possible values, see`LIST_CPE_DEVICE_SHAPES`Function. For more information about generating CPE device configuration content, see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function

`is_private`

(optional) Indicates whether this CPE is of type `private` or not.

### DBMS_CLOUD_OCI_CORE_CREATE_MACSEC_KEY_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_MACSEC_PROPERTIES_T Type

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

`is_unprotected_traffic_allowed`

(optional) Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails.

### DBMS_CLOUD_OCI_CORE_CREATE_CROSS_CONNECT_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`far_cross_connect_or_cross_connect_group_id`

(optional) If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of that existing cross-connect or cross-connect group.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_CREATE_CROSS_CONNECT_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the cross-connect group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection that this cross-connect group uses.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_CORE_CREATE_DEDICATED_CAPACITY_SOURCE_DETAILS_T Type

A capacity source of bare metal hosts that is dedicated to a customer.

Syntax
```

```

`dbms_cloud_oci_core_create_dedicated_capacity_source_details_t`is a subtype of the`dbms_cloud_oci_core_create_capacity_source_details_t`type.

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of this capacity source.

### DBMS_CLOUD_OCI_CORE_CREATE_DEDICATED_VM_HOST_DETAILS_T Type

The details for creating a new dedicated virtual machine host.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the dedicated virtual machine host. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment.

`dedicated_vm_host_shape`

(required) The dedicated virtual machine host shape. The shape determines the number of CPUs and other resources available for VM instances launched on the dedicated virtual machine host.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) The fault domain for the dedicated virtual machine host's assigned instances. For more information, see[Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host, delete it and create a new dedicated virtual machine host in the preferred fault domain. To get a list of fault domains, use the `ListFaultDomains` operation in the[Identity and Access Management Service API](https://docs.oracle.com/iaas/api/#/en/identity/20160918/). Example: `FAULT-DOMAIN-1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_DHCP_OPTION_T Type

A single DHCP option according to[RFC 1533](https://tools.ietf.org/html/rfc1533). The two options available to use are`DHCP_DNS_OPTION`Type and`DHCP_SEARCH_DOMAIN_OPTION`Type. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

Syntax
```

```

Fields

Field Description

`l_type`

(required) The specific DHCP option. Either `DomainNameServer` (for`DHCP_DNS_OPTION`Type) or `SearchDomain` (for`DHCP_SEARCH_DOMAIN_OPTION`Type).

### DBMS_CLOUD_OCI_CORE_DHCP_OPTION_TBL Type

Nested table type of dbms_cloud_oci_core_dhcp_option_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_DHCP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the set of DHCP options.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`options`

(required) A set of DHCP options.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the set of DHCP options belongs to.

`domain_name_type`

(optional) The search domain name type of DHCP options

Allowed values are: 'SUBNET_DOMAIN', 'VCN_DOMAIN', 'CUSTOM_DOMAIN'

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_DRG_ATTACHMENT_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the DRG attachment. If you don't specify a route table here, the DRG attachment is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the DRG attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN. This field is deprecated. Instead, use the `networkDetails` field to specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

### DBMS_CLOUD_OCI_CORE_CREATE_DRG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the DRG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_CREATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type

Details used to create a route distribution.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the DRG route table belongs to.

`distribution_type`

(required) Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments

Allowed values are: 'IMPORT'

### DBMS_CLOUD_OCI_CORE_CREATE_DRG_ROUTE_TABLE_DETAILS_T Type

Details used in a request to create a DRG route table.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the DRG route table belongs to.

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements through referenced attachments are inserted into the DRG route table.

`is_ecmp_enabled`

(optional) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-premises networks, enable ECMP on the DRG route table.

### DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_PHASE_ONE_CONFIG_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_PHASE_TWO_CONFIG_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_DPD_CONFIG_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_create_ip_sec_connection_tunnel_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`cpe_local_identifier`

(optional) Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`. If you don't provide a value, the `ipAddress` attribute for the`CPE`Type object specified by `cpeId` is used as the `cpeLocalIdentifier`. For information about why you'd provide this value, see[If Your CPE Is Behind a NAT Device](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat). Example IP address: `10.0.3.3` Example hostname: `cpe.example.com`

`cpe_local_identifier_type`

(optional) The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.

Allowed values are: 'IP_ADDRESS', 'HOSTNAME'

`static_routes`

(required) Static routes to the CPE. A static route's CIDR must not be a multicast address or class E address. Used for routing a given IPSec tunnel's traffic only if the tunnel is using static routing. If you configure at least one tunnel to use static routing, then you must provide at least one valid static route. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. For more information, see the important note in`IP_SEC_CONNECTION`Type. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `10.0.1.0/24` Example: `2001:db8::/32`

`tunnel_configuration`

(optional) Information for creating the individual tunnels in the IPSec connection. You can provide a maximum of 2 `tunnelConfiguration` objects in the array (one for each of the two tunnels).

### DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`operating_system`

(optional)

`operating_system_version`

(optional)

`source_image_type`

(optional) The format of the image to be imported. Only monolithic images are supported. This attribute is not used for exported Oracle images with the OCI image format.

Allowed values are: 'QCOW2', 'VMDK'

`source_type`

(required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.

### DBMS_CLOUD_OCI_CORE_CREATE_IMAGE_DETAILS_T Type

Either instanceId or imageSourceDetails must be provided in addition to other required parameters.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment you want the image to be created in.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information. You cannot use a platform image name as a custom image name. Example: `My Oracle Linux image`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`image_source_details`

(optional)

`instance_id`

(optional) The OCID of the instance you want to use as the basis for the image.

`launch_mode`

(optional) Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

Allowed values are: 'NATIVE', 'EMULATED', 'PARAVIRTUALIZED', 'CUSTOM'

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_BASE_T Type

Creation details for an instance configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the instance configuration.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`source`

(optional) The source of the instance configuration. An instance configuration defines the settings to use when creating Compute instances, including details such as the base image, shape, and metadata. You can also specify the associated resources for the instance, such as block volume attachments and network configuration. When you create an instance configuration using an existing instance as a template, the instance configuration does not include any information from the source instance's boot volume, such as installed applications, binaries, and files on the instance. It also does not include the contents of any block volumes that are attached to the instance. To create an instance configuration that includes the custom setup from an instance's boot volume, you must first create a custom image from the instance (see`CREATE_IMAGE`Function). Then, use the custom image to launch a new instance (see`LAUNCH_INSTANCE`Function). Finally, create the instance configuration based on the instance that you created from the custom image. To include block volume contents with an instance configuration, first create a backup of the attached block volumes (see`CREATE_VOLUME_BACKUP`Function). Then, create the instance configuration by specifying the list of settings, using`INSTANCE_CONFIGURATION_VOLUME_SOURCE_FROM_VOLUME_BACKUP_DETAILS`Function to include the block volume backups in the list of settings. The following values are supported: * `NONE`: Creates an instance configuration using the list of settings that you specify. * `INSTANCE`: Creates an instance configuration using an existing instance as a template.

Allowed values are: 'NONE', 'INSTANCE'

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_DETAILS_T Type

Details for creating an instance configuration by providing a list of configuration settings.

Syntax
```

```

`dbms_cloud_oci_core_create_instance_configuration_details_t`is a subtype of the`dbms_cloud_oci_core_create_instance_configuration_base_t`type.

Fields

Field Description

`instance_details`

(required)

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_FROM_INSTANCE_DETAILS_T Type

Details for creating an instance configuration using an existing instance as a template.

Syntax
```

```

`dbms_cloud_oci_core_create_instance_configuration_from_instance_details_t`is a subtype of the`dbms_cloud_oci_core_create_instance_configuration_base_t`type.

Fields

Field Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance to use to create the instance configuration.

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONSOLE_CONNECTION_DETAILS_T Type

The details for creating a instance console connection. The instance console connection is created in the same compartment as the instance.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_id`

(required) The OCID of the instance to create the console connection to.

`public_key`

(required) The SSH public key used to authenticate the console connection.

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_T Type

The location for where an instance pool will place instances.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to place instances. Example: `Uocm:PHX-AD-1`

`fault_domains`

(optional) The fault domains to place instances. If you don't provide any values, the system makes a best effort to distribute instances across all fault domains based on capacity. To distribute the instances evenly across selected fault domains, provide a set of fault domains. For example, you might want instances to be evenly distributed if your applications require high availability. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`

`primary_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary subnet in which to place instances. This field is deprecated. Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.

`primary_vnic_subnets`

(optional)

`secondary_vnic_subnets`

(optional) The set of secondary VNIC data for instances in the pool.

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_create_instance_pool_placement_configuration_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_ATTACH_LOAD_BALANCER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_attach_load_balancer_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_DETAILS_T Type

The data to create an instance pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the instance pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration associated with the instance pool.

`placement_configurations`

(required) The placement configurations for the instance pool. Provide one placement configuration for each availability domain. To use the instance pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

`l_size`

(required) The number of instances that should be in the instance pool.

`load_balancers`

(optional) The load balancers to attach to the instance pool.

`instance_display_name_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance displaynames follow the format. The formatter does not retroactively change instance's displaynames, only instance displaynames in the future follow the format

`instance_hostname_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance hostnames follow the format. The formatter does not retroactively change instance's hostnames, only instance hostnames in the future follow the format

### DBMS_CLOUD_OCI_CORE_CREATE_INTERNET_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the internet gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_enabled`

(required) Whether the gateway is enabled upon creation.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the Internet Gateway is attached to.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the Internet Gateway is using.

### DBMS_CLOUD_OCI_CORE_CREATE_IPV6_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ip_address`

(optional) An IPv6 address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns an IPv6 address from the subnet. The subnet is the one that contains the VNIC you specify in `vnicId`. Example: `2001:DB8::`

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to assign the IPv6 to. The IPv6 will be in the VNIC's subnet.

`ipv6_subnet_cidr`

(optional) The IPv6 prefix allocated to the subnet. This is required if more than one IPv6 prefix exists on the subnet.

### DBMS_CLOUD_OCI_CORE_CREATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the local peering gateway (LPG).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the LPG will use. If you don't specify a route table here, the LPG is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the LPG. For information about why you would associate a route table with an LPG, see[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the LPG belongs to.

### DBMS_CLOUD_OCI_CORE_CREATE_NAT_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the NAT gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`block_traffic`

(optional) Whether the NAT gateway blocks traffic through it. The default is `false`. Example: `true`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the gateway belongs to.

`public_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP address associated with the NAT gateway.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the NAT gateway. If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.

### DBMS_CLOUD_OCI_CORE_CREATE_NETWORK_SECURITY_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the network security group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to create the network security group in.

### DBMS_CLOUD_OCI_CORE_CREATE_PRIVATE_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`hostname_label`

(optional) The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`ip_address`

(optional) A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. Example: `10.0.3.3`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to assign the private IP to. The VNIC and private IP must be in the same subnet.

`vlan_id`

(optional) Use this attribute only with the Oracle Cloud VMware Solution. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN from which the private IP is to be drawn. The IP address, *if supplied*, must be valid for the given VLAN. See`VLAN`Type.

### DBMS_CLOUD_OCI_CORE_CREATE_PUBLIC_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the public IP. For ephemeral public IPs, you must set this to the private IP's compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`lifetime`

(required) Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public IP pool. For more information, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

Allowed values are: 'EPHEMERAL', 'RESERVED'

`private_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP to assign the public IP to. Required for an ephemeral public IP because it must always be assigned to a private IP (specifically a *primary* private IP). Optional for a reserved public IP. If you don't provide it, the public IP is created but not assigned to a private IP. You can later assign the public IP with`UPDATE_PUBLIC_IP`Function.

`public_ip_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

### DBMS_CLOUD_OCI_CORE_CREATE_PUBLIC_IP_POOL_DETAILS_T Type

The information used to create a public IP pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the public IP pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_CREATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the RPC.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG the RPC belongs to.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_ROUTE_RULE_T Type

A mapping between a destination IP address range and a virtual device to route matching packets to (a target).

Syntax
```

```

Fields

Field Description

`cidr_block`

(optional) Deprecated. Instead use `destination` and `destinationType`. Requests that include both `cidrBlock` and `destination` will be rejected. A destination IP address range in CIDR notation. Matching packets will be routed to the indicated network entity (the target). Cannot be an IPv6 prefix. Example: `0.0.0.0/0`

`destination`

(optional) Conceptually, this is the range of IP addresses used for matching when routing traffic. Required if you provide a `destinationType`. Allowed values: * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`. If you set this to an IPv6 prefix, the route rule's target can only be a DRG or internet gateway. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). * The `cidrBlock` value for a`SERVICE`Type, if you're setting up a route rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.

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

### DBMS_CLOUD_OCI_CORE_ROUTE_RULE_TBL Type

Nested table type of dbms_cloud_oci_core_route_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_ROUTE_TABLE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the route table.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_rules`

(required) The collection of rules used for routing destination IPs to network devices.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the route table belongs to.

### DBMS_CLOUD_OCI_CORE_EGRESS_SECURITY_RULE_T Type

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

### DBMS_CLOUD_OCI_CORE_INGRESS_SECURITY_RULE_T Type

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

### DBMS_CLOUD_OCI_CORE_EGRESS_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_core_egress_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INGRESS_SECURITY_RULE_TBL Type

Nested table type of dbms_cloud_oci_core_ingress_security_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_SECURITY_LIST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the security list.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(required) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ingress_security_rules`

(required) Rules for allowing ingress IP packets.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN the security list belongs to.

### DBMS_CLOUD_OCI_CORE_SERVICE_ID_REQUEST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`SERVICE`Type.

### DBMS_CLOUD_OCI_CORE_SERVICE_ID_REQUEST_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_service_id_request_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_SERVICE_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the service gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the service gateway will use. If you don't specify a route table here, the service gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the service gateway. For information about why you would associate a route table with a service gateway, see[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

`services`

(required) List of the OCIDs of the`SERVICE`Type objects to enable for the service gateway. This list can be empty if you don't want to enable any `Service` objects when you create the gateway. You can enable a `Service` object later by using either`ATTACH_SERVICE_ID`Function or`UPDATE_SERVICE_GATEWAY`Function. For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See`ROUTE_TABLE`Type.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

### DBMS_CLOUD_OCI_CORE_CREATE_SUBNET_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options the subnet will use. If you don't provide a value, the subnet uses the VCN's default set of DHCP options.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed. This value must be set if you want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It can only be set if the VCN itself was created with a DNS label. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `subnet123`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ipv6_cidr_block`

(optional) Use this to enable IPv6 addressing for this subnet. The VCN must be enabled for IPv6. You can't change this subnet characteristic later. All subnets are /64 in size. The subnet portion of the IPv6 address is the fourth hextet from the left (1111 in the following example). For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefixes, BYOIPv6 prefixes) for the subnet that meets the following criteria: - The prefixes must be valid. - Multiple prefixes must not overlap each other or the on-premises network prefix. - The number of prefixes must not exceed the limit of IPv6 prefixes allowed to a subnet.

`prohibit_internet_ingress`

(optional) Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false. For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default. `prohibitPublicIpOnVnic` will be set to the value of `prohibitInternetIngress` to dictate IPv4 behavior in this subnet. Only one or the other flag should be specified. Example: `true`

`prohibit_public_ip_on_vnic`

(optional) Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in`CREATE_VNIC_DETAILS`Type). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet). If you intend to use an IPv6 prefix, you should use the flag `prohibitInternetIngress` to specify ingress internet traffic behavior of the subnet. Example: `true`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the subnet will use. If you don't provide a value, the subnet uses the VCN's default route table.

`security_list_ids`

(optional) The OCIDs of the security list or lists the subnet will use. If you don't provide a value, the subnet uses the VCN's default security list. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to contain the subnet.

### DBMS_CLOUD_OCI_CORE_BYOIPV6_CIDR_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_byoipv6_cidr_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VCN_DETAILS_T Type

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

(optional) The list of one or more ULA or Private IPv6 prefixes for the VCN that meets the following criteria: - The CIDR blocks must be valid. - Multiple CIDR blocks must not overlap each other or the on-premises network prefix. - The number of CIDR blocks must not exceed the limit of IPv6 prefixes allowed to a VCN. **Important:** Do *not* specify a value for `ipv6CidrBlock`. Use this parameter instead.

`is_oracle_gua_allocation_enabled`

(optional) Specifies whether to skip Oracle allocated IPv6 GUA. By default, Oracle will allocate one GUA of /56 size for an IPv6 enabled VCN.

`byoipv6_cidr_details`

(optional) The list of BYOIPv6 OCIDs and BYOIPv6 prefixes required to create a VCN that uses BYOIPv6 address ranges.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed. You must set this value if you want instances to be able to use hostnames to resolve other instances in the VCN. Otherwise the Internet and VCN Resolver will not work. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_ipv6_enabled`

(optional) Whether IPv6 is enabled for the VCN. Default is `false`. If enabled, Oracle will assign the VCN a IPv6 /56 CIDR block. You may skip having Oracle allocate the VCN a IPv6 /56 CIDR block by setting isOracleGuaAllocationEnabled to `false`. For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `true`

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_T Type

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_core_cross_connect_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_CREATE_VLAN_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the VLAN will use. If you don't provide a value, the VLAN uses the VCN's default route table.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN to contain the VLAN.

`vlan_tag`

(optional) The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all VLANs in the VCN. If you don't provide a value, Oracle assigns one. You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`l_type`

(optional) The type of backup to create. If omitted, defaults to INCREMENTAL.

Allowed values are: 'FULL', 'INCREMENTAL'

`volume_id`

(required) The OCID of the volume that needs to be backed up.

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_POLICY_ASSIGNMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`asset_id`

(required) The OCID of the volume to assign the policy to.

`policy_id`

(required) The OCID of the volume backup policy to assign to the volume.

### DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_SCHEDULE_T Type

Defines the backup frequency and retention period for a volume backup policy. For more information, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Fields

Field Description

`backup_type`

(required) The type of volume backup to create.

Allowed values are: 'FULL', 'INCREMENTAL'

`offset_seconds`

(optional) The number of seconds that the volume backup start time should be shifted from the default interval boundaries specified by the period. The volume backup start time is the frequency start time plus the offset.

`period`

(required) The volume backup frequency.

Allowed values are: 'ONE_HOUR', 'ONE_DAY', 'ONE_WEEK', 'ONE_MONTH', 'ONE_YEAR'

`offset_type`

(optional) Indicates how the offset is defined. If value is `STRUCTURED`, then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used and `offsetSeconds` will be ignored in requests and users should ignore its value from the responses. `hourOfDay` is applicable for periods `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`. `dayOfWeek` is applicable for period `ONE_WEEK`. `dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`. 'month' is applicable for period 'ONE_YEAR'. They will be ignored in the requests for inapplicable periods. If value is `NUMERIC_SECONDS`, then `offsetSeconds` will be used for both requests and responses and the structured fields will be ignored in the requests and users should ignore their values from the responses. For clients using older versions of Apis and not sending `offsetType` in their requests, the behaviour is just like `NUMERIC_SECONDS`.

Allowed values are: 'STRUCTURED', 'NUMERIC_SECONDS'

`hour_of_day`

(optional) The hour of the day to schedule the volume backup.

`day_of_week`

(optional) The day of the week to schedule the volume backup.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

`day_of_month`

(optional) The day of the month to schedule the volume backup.

`month`

(optional) The month of the year to schedule the volume backup.

Allowed values are: 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'

`retention_seconds`

(required) How long, in seconds, to keep the volume backups created by this schedule.

`time_zone`

(optional) Specifies what time zone is the schedule in

Allowed values are: 'UTC', 'REGIONAL_DATA_CENTER_TIME'

### DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_SCHEDULE_TBL Type

Nested table type of dbms_cloud_oci_core_volume_backup_schedule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_POLICY_DETAILS_T Type

Specifies the properties for creating user defined backup policy. For more information about user defined backup policies, see[User Defined Policies](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies)in[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`destination_region`

(optional) The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`. See[Region Pairs](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs)for details about paired regions.

`schedules`

(optional) The collection of schedules for the volume backup policy. See see[Schedules](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules)in[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for more information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_DETAILS_T Type

Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.

Syntax
```

```

Fields

Field Description

`l_type`

(required)

### DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_block_volume_replica_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_DETAILS_T Type

The details of the volume to create. For CreateVolume operation, this field is required in the request, see`CREATE_VOLUME`Function.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain of the volume. Omissible for cloning a volume. The new volume will be created in the availability domain of the source volume. Example: `Uocm:PHX-AD-1`

`backup_policy_id`

(optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.

`compartment_id`

(required) The OCID of the compartment that contains the volume.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The OCID of the Vault service key to assign as the master encryption key for the volume.

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `0`: Represents Lower Cost option. * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`size_in_g_bs`

(optional) The size of the volume in GBs.

`size_in_m_bs`

(optional) The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.

`source_details`

(optional)

`volume_backup_id`

(optional) The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`block_volume_replicas`

(optional) The list of block volume replicas to be enabled for this volume in the specified destination availability domains.

`autotune_policies`

(optional) The list of autotune policies to be enabled for this volume.

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_GROUP_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment that will contain the volume group backup. This parameter is optional, by default backup will be created in the same compartment and source volume group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`l_type`

(optional) The type of backup to create. If omitted, defaults to incremental.

Allowed values are: 'FULL', 'INCREMENTAL'

`volume_group_id`

(required) The OCID of the volume group that needs to be backed up.

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_DETAILS_T Type

Specifies the source for a volume group.

Syntax
```

```

Fields

Field Description

`l_type`

(required)

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_DETAILS_T Type

Contains the details for the volume group replica.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`availability_domain`

(required) The availability domain of the volume group replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_volume_group_replica_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the volume group.

`backup_policy_id`

(optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume group. If omitted, no policy will be assigned.

`compartment_id`

(required) The OCID of the compartment that contains the volume group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`source_details`

(required)

`volume_group_replicas`

(optional) The list of volume group replicas that this volume group will be enabled to have in the specified destination availability domains.

### DBMS_CLOUD_OCI_CORE_CREATE_VTAP_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_MACSEC_KEY_T Type

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

### DBMS_CLOUD_OCI_CORE_MACSEC_PROPERTIES_T Type

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

`is_unprotected_traffic_allowed`

(optional) Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails.

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_GROUP_T Type

For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group is a link aggregation group (LAG), which can contain one or more`CROSS_CONNECT`Type. Customers who are colocated with Oracle in a FastConnect location create and use cross-connect groups. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). **Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the cross-connect group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_LOCATION_T Type

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_cross_connect_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_COLLECTION_T Type

An array of CrossConnectMappingDetails

Syntax
```

```

Fields

Field Description

`items`

(required) CrossConnectMappingDetails items

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_PORT_SPEED_SHAPE_T Type

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

### DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_STATUS_T Type

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

### DBMS_CLOUD_OCI_CORE_DEDICATED_CAPACITY_SOURCE_T Type

A capacity source of bare metal hosts that is dedicated to a user.

Syntax
```

```

`dbms_cloud_oci_core_dedicated_capacity_source_t`is a subtype of the`dbms_cloud_oci_core_capacity_source_t`type.

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of this capacity source.

### DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_T Type

A dedicated virtual machine host lets you host multiple VM instances on a dedicated server that is not shared with other tenancies.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the dedicated virtual machine host is running in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the dedicated virtual machine host.

`dedicated_vm_host_shape`

(required) The dedicated virtual machine host shape. The shape determines the number of CPUs and other resources available for VMs.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) The fault domain for the dedicated virtual machine host's assigned instances. For more information, see[Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host, delete it, and then create a new dedicated virtual machine host in the preferred fault domain. To get a list of fault domains, use the `ListFaultDomains` operation in the[Identity and Access Management Service API](https://docs.oracle.com/iaas/api/#/en/identity/20160918/). Example: `FAULT-DOMAIN-1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated VM host.

`lifecycle_state`

(required) The current state of the dedicated VM host.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the dedicated VM host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`total_ocpus`

(required) The total OCPUs of the dedicated VM host.

`remaining_ocpus`

(required) The available OCPUs of the dedicated VM host.

`total_memory_in_g_bs`

(optional) The total memory of the dedicated VM host, in GBs.

`remaining_memory_in_g_bs`

(optional) The remaining memory of the dedicated VM host, in GBs.

### DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_INSTANCE_SHAPE_SUMMARY_T Type

The shape used to launch instances associated with the dedicated VM host.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The shape's availability domain.

`instance_shape_name`

(required) The name of the virtual machine instance shapes that can be launched on a dedicated VM host.

### DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_INSTANCE_SUMMARY_T Type

Condensed instance data when listing instances on a dedicated VM host.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the virtual machine instance is running in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the virtual machine instance.

`instance_id`

(required) The OCID of the virtual machine instance.

`shape`

(required) The shape of the VM instance.

`time_created`

(required) The date and time the virtual machine instance was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_SHAPE_SUMMARY_T Type

The shape used to launch the dedicated virtual machine (VM) host.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The shape's availability domain.

`dedicated_vm_host_shape`

(required) The name of the dedicated VM host shape. You can enumerate all available shapes by calling`DEDICATED_VM_HOST_SHAPES`Type.

### DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_SUMMARY_T Type

A dedicated virtual machine (VM) host lets you host multiple instances on a dedicated server that is not shared with other tenancies.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the dedicated VM host is running in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the dedicated VM host.

`dedicated_vm_host_shape`

(required) The shape of the dedicated VM host. The shape determines the number of CPUs and other resources available for VMs.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) The fault domain for the dedicated VM host's assigned instances. For more information, see Fault Domains. If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated VM host, delete it and create a new dedicated VM host in the preferred fault domain. To get a list of fault domains, use the ListFaultDomains operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated VM host.

`lifecycle_state`

(required) The current state of the dedicated VM host.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the dedicated VM host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`remaining_ocpus`

(required) The current available OCPUs of the dedicated VM host.

`total_ocpus`

(required) The current total OCPUs of the dedicated VM host.

`total_memory_in_g_bs`

(optional) The current total memory of the dedicated VM host, in GBs.

`remaining_memory_in_g_bs`

(optional) The current available memory of the dedicated VM host, in GBs.

### DBMS_CLOUD_OCI_CORE_DEFAULT_DRG_ROUTE_TABLES_T Type

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

### DBMS_CLOUD_OCI_CORE_DETACH_INSTANCE_POOL_INSTANCE_DETAILS_T Type

An instance that is to be detached from an instance pool.

Syntax
```

```

Fields

Field Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`is_decrement_size`

(optional) Whether to decrease the size of the instance pool when the instance is detached. If `true`, the pool size is decreased. If `false`, the pool will provision a new, replacement instance using the pool's instance configuration as a template. Default is `true`.

`is_auto_terminate`

(optional) Whether to permanently terminate (delete) the instance and its attached boot volume when detaching it from the instance pool. Default is `false`.

### DBMS_CLOUD_OCI_CORE_DETACH_LOAD_BALANCER_DETAILS_T Type

Represents a load balancer that is to be detached from an instance pool.

Syntax
```

```

Fields

Field Description

`load_balancer_id`

(required) The OCID of the load balancer to detach from the instance pool.

`backend_set_name`

(required) The name of the backend set on the load balancer to detach from the instance pool.

### DBMS_CLOUD_OCI_CORE_DETACHED_VOLUME_AUTOTUNE_POLICY_T Type

Volume's performace will be tuned to the lower cost settings once detached.

Syntax
```

```

`dbms_cloud_oci_core_detached_volume_autotune_policy_t`is a subtype of the`dbms_cloud_oci_core_autotune_policy_t`type.

### DBMS_CLOUD_OCI_CORE_DEVICE_T Type

Device Path corresponding to the block devices attached to instances having a name and isAvailable flag.

Syntax
```

```

Fields

Field Description

`name`

(required) The device name.

`is_available`

(required) The flag denoting whether device is available.

### DBMS_CLOUD_OCI_CORE_DHCP_DNS_OPTION_T Type

DHCP option for specifying how DNS (hostname resolution) is handled in the subnets in the VCN. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

Syntax
```

```

`dbms_cloud_oci_core_dhcp_dns_option_t`is a subtype of the`dbms_cloud_oci_core_dhcp_option_t`type.

Fields

Field Description

`custom_dns_servers`

(optional) If you set `serverType` to `CustomDnsServer`, specify the IP address of at least one DNS server of your choice (three maximum).

`server_type`

(required) * **VcnLocal:** Reserved for future use. * **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\". Instances can resolve internet hostnames (no internet gateway is required), and can resolve hostnames of instances in the VCN. This is the default value in the default set of DHCP options in the VCN. For the Internet and VCN Resolver to work across the VCN, there must also be a DNS label set for the VCN, a DNS label set for each subnet, and a hostname for each instance. The Internet and VCN Resolver also enables reverse DNS lookup, which lets you determine the hostname corresponding to the private IP address. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). * **CustomDnsServer:** Instances use a DNS server of your choice (three maximum).

Allowed values are: 'VcnLocal', 'VcnLocalPlusInternet', 'CustomDnsServer'

### DBMS_CLOUD_OCI_CORE_DHCP_OPTIONS_T Type

A set of DHCP options. Used by the VCN to automatically provide configuration information to the instances when they boot up. There are two options you can set: -`DHCP_DNS_OPTION`Type: Lets you specify how DNS (hostname resolution) is handled in the subnets in your VCN. -`DHCP_SEARCH_DOMAIN_OPTION`Type: Lets you specify a search domain name to use for DNS queries. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)and[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the set of DHCP options.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_DHCP_SEARCH_DOMAIN_OPTION_T Type

DHCP option for specifying a search domain name for DNS queries. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

Syntax
```

```

`dbms_cloud_oci_core_dhcp_search_domain_option_t`is a subtype of the`dbms_cloud_oci_core_dhcp_option_t`type.

Fields

Field Description

`search_domain_names`

(required) A single search domain name according to[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). During a DNS query, the OS will append this search domain name to the value being queried. If you set`DHCP_DNS_OPTION`Type to `VcnLocalPlusInternet`, and you assign a DNS label to the VCN during creation, the search domain name in the VCN's default set of DHCP options is automatically set to the VCN domain (for example, `vcn1.oraclevcn.com`). If you don't want to use a search domain name, omit this option from the set of DHCP options. Do not include this option with an empty list of search domain names, or with an empty string as the value for any search domain name.

### DBMS_CLOUD_OCI_CORE_DRG_T Type

A dynamic routing gateway (DRG) is a virtual router that provides a path for private network traffic between networks. You use it with other Networking Service components to create a connection to your on-premises network using[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)or a connection that uses[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). For more information, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the DRG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the DRG attachment is using. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)This field is deprecated. Instead, use the `networkDetails` field to view the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN. This field is deprecated. Instead, use the `networkDetails` field to view the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached resource.

`export_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export route distribution used to specify how routes in the assigned DRG route table are advertised to the attachment. If this value is null, no routes are advertised through this attachment.

`is_cross_tenancy`

(optional) Indicates whether the DRG attachment and attached network live in a different tenancy than the DRG. Example: `false`

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_ID_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The criteria by which a specific attachment will import routes to the DRG.

Syntax
```

```

`dbms_cloud_oci_core_drg_attachment_id_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_core_drg_route_distribution_match_criteria_t`type.

Fields

Field Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_INFO_T Type

The `DrgAttachmentInfo` resource contains the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle-assigned ID of the DRG attachment

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_MATCH_ALL_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

All routes are imported or exported.

Syntax
```

```

`dbms_cloud_oci_core_drg_attachment_match_all_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_core_drg_route_distribution_match_criteria_t`type.

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required)

Allowed values are: 'VCN'

### DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_TYPE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type

The attachment type from which the DRG will import routes. Routes will be imported from all attachments of this type.

Syntax
```

```

`dbms_cloud_oci_core_drg_attachment_type_drg_route_distribution_match_criteria_t`is a subtype of the`dbms_cloud_oci_core_drg_route_distribution_match_criteria_t`type.

Fields

Field Description

`attachment_type`

(required) The type of the network resource to be included in this match. A match for a network type implies that all DRG attachments of that type insert routes into the table.

Allowed values are: 'VCN', 'VIRTUAL_CIRCUIT', 'REMOTE_PEERING_CONNECTION', 'IPSEC_TUNNEL'

### DBMS_CLOUD_OCI_CORE_DRG_REDUNDANCY_STATUS_T Type

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

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_STATEMENT_T Type

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

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_RULE_T Type

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

### DBMS_CLOUD_OCI_CORE_DRG_ROUTE_TABLE_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(required) The date and time the DRG route table was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The DRG route table's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements from referenced attachments are inserted into the DRG route table.

`is_ecmp_enabled`

(required) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-premises network, enable ECMP on the DRG route table to which these attachments import routes.

### DBMS_CLOUD_OCI_CORE_VOLUME_ATTACHMENT_T Type

A base object for all types of attachments between a storage volume and an instance. For specific details about iSCSI attachments, see`I_SCSI_VOLUME_ATTACHMENT`Type. For general information about volume attachments, see[Overview of Block Volume Storage](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`attachment_type`

(required) The type of volume attachment.

`availability_domain`

(required) The availability domain of an instance. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment.

`device`

(optional) The device name.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The OCID of the volume attachment.

`instance_id`

(required) The OCID of the instance the volume is attached to.

`is_read_only`

(optional) Whether the attachment was created in read-only mode.

`is_shareable`

(optional) Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.

`lifecycle_state`

(required) The current state of the volume attachment.

Allowed values are: 'ATTACHING', 'ATTACHED', 'DETACHING', 'DETACHED'

`time_created`

(required) The date and time the volume was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`volume_id`

(required) The OCID of the volume.

`is_pv_encryption_in_transit_enabled`

(optional) Whether in-transit encryption for the data volume's paravirtualized attachment is enabled or not.

`is_multipath`

(optional) Whether the Iscsi or Paravirtualized attachment is multipath or not, it is not applicable to NVMe attachment.

`iscsi_login_state`

(optional) The iscsi login state of the volume attachment. For a Iscsi volume attachment, all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.

Allowed values are: 'UNKNOWN', 'LOGGING_IN', 'LOGIN_SUCCEEDED', 'LOGIN_FAILED', 'LOGGING_OUT', 'LOGOUT_SUCCEEDED', 'LOGOUT_FAILED'

### DBMS_CLOUD_OCI_CORE_EMULATED_VOLUME_ATTACHMENT_T Type

An Emulated volume attachment.

Syntax
```

```

`dbms_cloud_oci_core_emulated_volume_attachment_t`is a subtype of the`dbms_cloud_oci_core_volume_attachment_t`type.

### DBMS_CLOUD_OCI_CORE_ENCRYPTION_DOMAIN_CONFIG_T Type

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

### DBMS_CLOUD_OCI_CORE_ENUM_INTEGER_IMAGE_CAPABILITY_DESCRIPTOR_T Type

Enum Integer type CapabilityDescriptor

Syntax
```

```

`dbms_cloud_oci_core_enum_integer_image_capability_descriptor_t`is a subtype of the`dbms_cloud_oci_core_image_capability_schema_descriptor_t`type.

Fields

Field Description

`l_values`

(required) the list of values for the enum

`default_value`

(optional) the default value

### DBMS_CLOUD_OCI_CORE_ENUM_STRING_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type

Enum String type of ImageCapabilitySchemaDescriptor

Syntax
```

```

`dbms_cloud_oci_core_enum_string_image_capability_schema_descriptor_t`is a subtype of the`dbms_cloud_oci_core_image_capability_schema_descriptor_t`type.

Fields

Field Description

`l_values`

(required) the list of values for the enum

`default_value`

(optional) the default value

### DBMS_CLOUD_OCI_CORE_ERROR_T Type

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

### DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_DETAILS_T Type

The destination details for the image export. Set `destinationType` to `objectStorageTuple` and use`EXPORT_IMAGE_VIA_OBJECT_STORAGE_TUPLE_DETAILS`Function when specifying the namespace, bucket name, and object name. Set `destinationType` to `objectStorageUri` and use`EXPORT_IMAGE_VIA_OBJECT_STORAGE_URI_DETAILS`Function when specifying the Object Storage URL.

Syntax
```

```

Fields

Field Description

`destination_type`

(required) The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.

`export_format`

(optional) The format to export the image to. The default value is `OCI`. The following image formats are available: - `OCI` - Oracle Cloud Infrastructure file with a QCOW2 image and Oracle Cloud Infrastructure metadata (.oci). Use this format to export a custom image that you want to import into other tenancies or regions. - `QCOW2` - QEMU Copy On Write (.qcow2) - `VDI` - Virtual Disk Image (.vdi) for Oracle VM VirtualBox - `VHD` - Virtual Hard Disk (.vhd) for Hyper-V - `VMDK` - Virtual Machine Disk (.vmdk)

Allowed values are: 'QCOW2', 'VMDK', 'OCI', 'VHD', 'VDI'

### DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_export_image_via_object_storage_tuple_details_t`is a subtype of the`dbms_cloud_oci_core_export_image_details_t`type.

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket to export the image to.

`namespace_name`

(required) The Object Storage namespace to export the image to.

`object_name`

(required) The Object Storage object name for the exported image.

### DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_export_image_via_object_storage_uri_details_t`is a subtype of the`dbms_cloud_oci_core_export_image_details_t`type.

Fields

Field Description

`destination_uri`

(required) The Object Storage URL to export the image to. See[Object Storage URLs](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs)and[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for constructing URLs for image import/export.

### DBMS_CLOUD_OCI_CORE_FAST_CONNECT_PROVIDER_SERVICE_T Type

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

### DBMS_CLOUD_OCI_CORE_FAST_CONNECT_PROVIDER_SERVICE_KEY_T Type

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

### DBMS_CLOUD_OCI_CORE_GENERIC_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The standard platform configuration to be used when launching a bare metal instance.

Syntax
```

```

`dbms_cloud_oci_core_generic_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_GENERIC_BM_PLATFORM_CONFIG_T Type

The standard platform configuration of a bare metal instance.

Syntax
```

```

`dbms_cloud_oci_core_generic_bm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_GET_PUBLIC_IP_BY_IP_ADDRESS_DETAILS_T Type

IP address of the public IP.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) The public IP address. Example: 203.0.113.2

### DBMS_CLOUD_OCI_CORE_GET_PUBLIC_IP_BY_PRIVATE_IP_ID_DETAILS_T Type

Details of the private IP that the public IP is assigned to.

Syntax
```

```

Fields

Field Description

`private_ip_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP.

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_CONFIG_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_core_tunnel_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_DEVICE_CONFIG_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_STATUS_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_STATUS_TBL Type

Nested table type of dbms_cloud_oci_core_tunnel_status_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_DEVICE_STATUS_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_PHASE_ONE_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_PHASE_TWO_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_T Type

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

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_ERROR_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_T Type

The tunnel's shared secret (pre-shared key).

Syntax
```

```

Fields

Field Description

`shared_secret`

(required) The tunnel's shared secret (pre-shared key).

### DBMS_CLOUD_OCI_CORE_MULTIPATH_DEVICE_T Type

Secondary multipath device, it uses the charUsername and chapSecret from primary volume attachment

Syntax
```

```

Fields

Field Description

`ipv4`

(required) The volume's iSCSI IP address. Example: `169.254.2.2`

`iqn`

(required) The target volume's iSCSI Qualified Name in the format defined by[RFC 3720](https://tools.ietf.org/html/rfc3720#page-32). Example: `iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195`

`port`

(optional) The volume's iSCSI port, usually port 860 or 3260. Example: `3260`

### DBMS_CLOUD_OCI_CORE_MULTIPATH_DEVICE_TBL Type

Nested table type of dbms_cloud_oci_core_multipath_device_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_I_SCSI_VOLUME_ATTACHMENT_T Type

An ISCSI volume attachment.

Syntax
```

```

`dbms_cloud_oci_core_i_scsi_volume_attachment_t`is a subtype of the`dbms_cloud_oci_core_volume_attachment_t`type.

Fields

Field Description

`chap_secret`

(optional) The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name. (Also called the \"CHAP password\".)

`chap_username`

(optional) The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name. See[RFC 1994](https://tools.ietf.org/html/rfc1994)for more on CHAP. Example: `ocid1.volume.oc1.phx.&lt;unique_ID&gt;`

`ipv4`

(required) The volume's iSCSI IP address. Example: `169.254.0.2`

`iqn`

(required) The target volume's iSCSI Qualified Name in the format defined by[RFC 3720](https://tools.ietf.org/html/rfc3720#page-32).

`port`

(required) The volume's iSCSI port, usually port 860 or 3260. Example: `3260`

`multipath_devices`

(optional) A list of secondary multipath devices

`encryption_in_transit_type`

(optional) Refer the top-level definition of encryptionInTransitType. The default value is NONE.

Allowed values are: 'NONE', 'BM_ENCRYPTION_IN_TRANSIT'

`is_agent_auto_iscsi_login_enabled`

(optional) Whether Oracle Cloud Agent is enabled perform the iSCSI login and logout commands after the volume attach or detach operations for non multipath-enabled iSCSI attachments.

### DBMS_CLOUD_OCI_CORE_LAUNCH_OPTIONS_T Type

Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.

Syntax
```

```

Fields

Field Description

`boot_volume_type`

(optional) Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.

Allowed values are: 'ISCSI', 'SCSI', 'IDE', 'VFIO', 'PARAVIRTUALIZED'

`firmware`

(optional) Firmware used to boot VM. Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the default for platform images.

Allowed values are: 'BIOS', 'UEFI_64'

`network_type`

(optional) Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

Allowed values are: 'E1000', 'VFIO', 'PARAVIRTUALIZED'

`remote_data_volume_type`

(optional) Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.

Allowed values are: 'ISCSI', 'SCSI', 'IDE', 'VFIO', 'PARAVIRTUALIZED'

`is_pv_encryption_in_transit_enabled`

(optional) Deprecated. Instead use `isPvEncryptionInTransitEnabled` in`LAUNCH_INSTANCE_DETAILS`Function.

`is_consistent_volume_naming_enabled`

(optional) Whether to enable consistent volume naming feature. Defaults to false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_FEATURES_T Type

Oracle Cloud Agent features supported on the image.

Syntax
```

```

Fields

Field Description

`is_monitoring_supported`

(optional) This attribute is not used.

`is_management_supported`

(optional) This attribute is not used.

### DBMS_CLOUD_OCI_CORE_IMAGE_T Type

A boot disk image for launching an instance. For more information, see[Overview of the Compute Service](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`base_image_id`

(optional) The OCID of the image originally used to launch the instance.

`compartment_id`

(required) The OCID of the compartment containing the instance you want to use as the basis for the image.

`create_image_allowed`

(required) Whether instances launched with this image can be used to create new images. For example, you cannot create an image of an Oracle Database instance. Example: `true`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information. You cannot use a platform image name as a custom image name. Example: `My custom Oracle Linux image`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the image.

`launch_mode`

(optional) Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

Allowed values are: 'NATIVE', 'EMULATED', 'PARAVIRTUALIZED', 'CUSTOM'

`launch_options`

(optional)

`lifecycle_state`

(required)

Allowed values are: 'PROVISIONING', 'IMPORTING', 'AVAILABLE', 'EXPORTING', 'DISABLED', 'DELETED'

`operating_system`

(required) The image's operating system. Example: `Oracle Linux`

`operating_system_version`

(required) The image's operating system version. Example: `7.2`

`agent_features`

(optional)

`listing_type`

(optional) The listing type of the image. The default value is \"NONE\".

Allowed values are: 'COMMUNITY', 'NONE'

`size_in_m_bs`

(optional) The boot volume size for an instance launched from this image (1 MB = 1,048,576 bytes). Note this is not the same as the size of the image when it was exported or the actual size of the image. Example: `47694`

`billable_size_in_g_bs`

(optional) The size of the internal storage for this image that is subject to billing (1 GB = 1,073,741,824 bytes). Example: `100`

`time_created`

(required) The date and time the image was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_IMAGE_SHAPE_COMPATIBILITY_ENTRY_T Type

An image and shape that are compatible.

Syntax
```

```

Fields

Field Description

`image_id`

(required) The image OCID.

`shape`

(required) The shape name.

`memory_constraints`

(optional)

`ocpu_constraints`

(optional)

### DBMS_CLOUD_OCI_CORE_IMAGE_SHAPE_COMPATIBILITY_SUMMARY_T Type

Summary information for a compatible image and shape.

Syntax
```

```

Fields

Field Description

`image_id`

(required) The image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`shape`

(required) The shape name.

`memory_constraints`

(optional)

`ocpu_constraints`

(optional)

### DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_image_source_via_object_storage_tuple_details_t`is a subtype of the`dbms_cloud_oci_core_image_source_details_t`type.

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket for the image.

`namespace_name`

(required) The Object Storage namespace for the image.

`object_name`

(required) The Object Storage name for the image.

### DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_image_source_via_object_storage_uri_details_t`is a subtype of the`dbms_cloud_oci_core_image_source_details_t`type.

Fields

Field Description

`source_uri`

(required) The Object Storage URL for the image.

### DBMS_CLOUD_OCI_CORE_INSTANCE_OPTIONS_T Type

Optional mutable instance options

Syntax
```

```

Fields

Field Description

`are_legacy_imds_endpoints_disabled`

(optional) Whether to disable the legacy (/v1) instance metadata service endpoints. Customers who have migrated to /v2 should set this to true for added security. Default is false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_AVAILABILITY_CONFIG_T Type

Options for defining the availabiity of a VM instance after a maintenance event that impacts the underlying hardware.

Syntax
```

```

Fields

Field Description

`is_live_migration_preferred`

(optional) Whether to live migrate supported VM instances to a healthy physical VM host without disrupting running instances during infrastructure maintenance events. If null, Oracle chooses the best option for migrating the VM during infrastructure maintenance events.

`recovery_action`

(optional) The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.

Allowed values are: 'RESTORE_INSTANCE', 'STOP_INSTANCE'

### DBMS_CLOUD_OCI_CORE_INSTANCE_SHAPE_CONFIG_T Type

The shape configuration for an instance. The shape configuration determines the resources allocated to an instance.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

`baseline_ocpu_utilization`

(optional) The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`. The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

`processor_description`

(optional) A short description of the instance's processor (CPU).

`networking_bandwidth_in_gbps`

(optional) The networking bandwidth available to the instance, in gigabits per second.

`max_vnic_attachments`

(optional) The maximum number of VNIC attachments for the instance.

`gpus`

(optional) The number of GPUs available to the instance.

`gpu_description`

(optional) A short description of the instance's graphics processing unit (GPU). If the instance does not have any GPUs, this field is `null`.

`local_disks`

(optional) The number of local disks available to the instance.

`local_disks_total_size_in_g_bs`

(optional) The aggregate size of all local disks, in gigabytes. If the instance does not have any local disks, this field is `null`.

`local_disk_description`

(optional) A short description of the local disks available to this instance. If the instance does not have any local disks, this field is `null`.

`vcpus`

(optional) The total number of VCPUs available to the instance. This can be used instead of OCPUs, in which case the actual number of OCPUs will be calculated based on this value and the actual hardware. This must be a multiple of 2.

### DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

### DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_CONFIG_T Type

Configuration options for the Oracle Cloud Agent software running on the instance.

Syntax
```

```

Fields

Field Description

`is_monitoring_disabled`

(optional) Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.

`is_management_disabled`

(optional) Whether Oracle Cloud Agent can run all the available management plugins. These are the management plugins: OS Management Service Agent and Compute Instance Run Command. The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.

`are_all_plugins_disabled`

(optional) Whether Oracle Cloud Agent can run all of the available plugins. This includes the management and monitoring plugins. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`plugins_config`

(optional) The configuration of plugins associated with this instance.

### DBMS_CLOUD_OCI_CORE_INSTANCE_T Type

A compute host. The image used to launch the instance determines its operating system and other software. The shape specified during the launch process determines the number of CPUs and memory allocated to the instance. When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the`LIST_VNIC_ATTACHMENTS`Function operation to get the VNIC ID for the instance, and then call`GET_VNIC`Function with the VNIC ID. For more information, see[Overview of the Compute Service](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the instance is running in. Example: `Uocm:PHX-AD-1`

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation this instance is launched under. When this field contains an empty string or is null, the instance is not currently in a capacity reservation. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`compartment_id`

(required) The OCID of the compartment that contains the instance.

`dedicated_vm_host_id`

(optional) The OCID of the dedicated virtual machine host that the instance is placed on.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

`fault_domain`

(optional) The name of the fault domain the instance is running in. A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains. If you do not specify the fault domain, the system selects one for you. Example: `FAULT-DOMAIN-1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the instance.

`image_id`

(optional) Deprecated. Use `sourceDetails` instead.

`ipxe_script`

(optional) When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process. If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots. Be aware that the same iPXE script will run every time an instance boots, not only after the initial LaunchInstance call. The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot. If your instance boot volume attachment type is paravirtualized, the boot volume is attached to the instance through virtio-scsi and no iPXE script is used. If your instance boot volume attachment type is paravirtualized and you use custom iPXE to network boot into your instance, the primary boot volume is attached as a data volume through virtio-scsi drive. For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see[Bring Your Own Image](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm). For more information about iPXE, see http://ipxe.org.

`launch_mode`

(optional) Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

Allowed values are: 'NATIVE', 'EMULATED', 'PARAVIRTUALIZED', 'CUSTOM'

`launch_options`

(optional)

`instance_options`

(optional)

`availability_config`

(optional)

`preemptible_instance_config`

(optional)

`lifecycle_state`

(required) The current state of the instance.

Allowed values are: 'MOVING', 'PROVISIONING', 'RUNNING', 'STARTING', 'STOPPING', 'STOPPED', 'CREATING_IMAGE', 'TERMINATING', 'TERMINATED'

`metadata`

(optional) Custom metadata that you provide.

`l_region`

(required) The region that contains the availability domain the instance is running in. For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively. For all other regions, the full region name is returned. Examples: `phx`, `eu-frankfurt-1`

`shape`

(required) The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`shape_config`

(optional)

`is_cross_numa_node`

(optional) Whether the instance’s OCPUs and memory are distributed across multiple NUMA nodes.

`source_details`

(optional)

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`time_created`

(required) The date and time the instance was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`agent_config`

(optional)

`time_maintenance_reboot_due`

(optional) The date and time the instance is expected to be stopped / started, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time. Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state. Example: `2018-05-25T21:10:29.600Z`

`platform_config`

(optional)

`instance_configuration_id`

(optional) The OCID of the Instance Configuration used to source launch details for this instance. Any other fields supplied in the instance launch request override the details stored in the Instance Configuration for this instance launch.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_T Type

An instance configuration is a template that defines the settings to use when creating Compute instances. For more information about instance configurations, see[Managing Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the instance configuration.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration.

`instance_details`

(optional)

`deferred_fields`

(optional) Parameters that were not specified when the instance configuration was created, but that are required to launch an instance from the instance configuration. See the`LAUNCH_INSTANCE_CONFIGURATION`Function operation.

`time_created`

(required) The date and time the instance configuration was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_MILAN_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal GPU instance with the following shape: BM.GPU.GM4.8 (also named BM.GPU.A100-v2.8) (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_amd_milan_bm_gpu_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_MILAN_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with one of the following shapes: BM.Standard.E4.128 or BM.DenseIO.E4.128 (the AMD Milan platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_amd_milan_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_ROME_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration of a bare metal GPU instance that uses the BM.GPU4.8 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_amd_rome_bm_gpu_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_ROME_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with the BM.Standard.E3.128 shape (the AMD Rome platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_amd_rome_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a virtual machine instance with the AMD platform.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_amd_vm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_DETACHED_VOLUME_AUTOTUNE_POLICY_T Type

Volume's performace will be tuned to the lower cost settings once detached.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_detached_volume_autotune_policy_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_autotune_policy_t`type.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_GENERIC_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The standard platform configuration to be used when launching a bare metal instance.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_generic_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_access_control_service_enabled`

(optional) Whether the Access Control Service is enabled on the instance. When enabled, the platform can enforce PCIe device isolation, required for VFIO device pass-through.

`are_virtual_instructions_enabled`

(optional) Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes or VT-x for Intel shapes.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_IMAGE_FILTER_DETAILS_T Type

These are the criteria for selecting an image. This is required if imageId is not specified.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment containing images to search

`defined_tags_filter`

(optional) Filter based on these defined tags. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`operating_system`

(optional) The image's operating system. Example: `Oracle Linux`

`operating_system_version`

(optional) The image's operating system version. Example: `7.2`

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_instance_source_via_boot_volume_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_instance_source_details_t`type.

Fields

Field Description

`boot_volume_id`

(optional) The OCID of the boot volume used to boot the instance.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_instance_source_via_image_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_instance_source_details_t`type.

Fields

Field Description

`boot_volume_size_in_g_bs`

(optional) The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).

`image_id`

(optional) The OCID of the image used to boot the instance.

`kms_key_id`

(optional) The OCID of the Vault service key to assign as the master encryption key for the boot volume.

`boot_volume_vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`instance_source_image_filter_details`

(optional)

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_ICELAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with the BM.Standard3.64 shape or the BM.Optimized3.36 shape (the Intel Ice Lake platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_intel_icelake_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_SKYLAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with one of the following shapes: BM.Standard2.52, BM.GPU2.2, BM.GPU3.8, or BM.DenseIO2.52 (the Intel Skylake platform).

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_intel_skylake_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a virtual machine instance with the Intel platform.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_intel_vm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_launch_instance_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ISCSI_ATTACH_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_iscsi_attach_volume_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_attach_volume_details_t`type.

Fields

Field Description

`use_chap`

(optional) Whether to use CHAP authentication for the volume attachment. Defaults to false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_PARAVIRTUALIZED_ATTACH_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_paravirtualized_attach_volume_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_attach_volume_details_t`type.

Fields

Field Description

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_PERFORMANCE_BASED_AUTOTUNE_POLICY_T Type

If a volume is being throttled at the current setting for a certain period of time, auto-tune will gradually increase the volume’s performance limited up to Maximum VPUs/GB. After the volume has been idle at the current setting for a certain period of time, auto-tune will gradually decrease the volume’s performance limited down to Default/Minimum VPUs/GB.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_performance_based_autotune_policy_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_autotune_policy_t`type.

Fields

Field Description

`max_vpus_per_gb`

(required) This will be the maximum VPUs/GB performance level that the volume will be auto-tuned temporarily based on performance monitoring.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_SUMMARY_T Type

Summary information for an instance configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the instance configuration.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The OCID of the instance configuration.

`time_created`

(required) The date and time the instance configuration was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_FROM_VOLUME_BACKUP_DETAILS_T Type

Specifies the volume backup.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_volume_source_from_volume_backup_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_volume_source_details_t`type.

Fields

Field Description

`id`

(optional) The OCID of the volume backup.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_FROM_VOLUME_DETAILS_T Type

Specifies the source volume.

Syntax
```

```

`dbms_cloud_oci_core_instance_configuration_volume_source_from_volume_details_t`is a subtype of the`dbms_cloud_oci_core_instance_configuration_volume_source_details_t`type.

Fields

Field Description

`id`

(optional) The OCID of the volume.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CONSOLE_CONNECTION_T Type

The `InstanceConsoleConnection` API provides you with console access to Compute instances, enabling you to troubleshoot malfunctioning instances remotely. For more information about instance console connections, see[Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment to contain the console connection.

`connection_string`

(optional) The SSH connection string for the console connection.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`fingerprint`

(optional) The SSH public key's fingerprint for client authentication to the console connection.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(optional) The OCID of the console connection.

`instance_id`

(optional) The OCID of the instance the console connection connects to.

`lifecycle_state`

(optional) The current state of the console connection.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED'

`service_host_key_fingerprint`

(optional) The SSH public key's fingerprint for the console connection service host.

`vnc_connection_string`

(optional) The SSH connection string for the SSH tunnel used to connect to the console connection over VNC.

### DBMS_CLOUD_OCI_CORE_INSTANCE_CREDENTIALS_T Type

The credentials for a particular instance.

Syntax
```

```

Fields

Field Description

`password`

(required) The password for the username.

`username`

(required) The username.

### DBMS_CLOUD_OCI_CORE_INSTANCE_MAINTENANCE_REBOOT_T Type

The maximum possible date and time that a maintenance reboot can be extended.

Syntax
```

```

Fields

Field Description

`time_maintenance_reboot_due_max`

(required) The maximum extension date and time for the maintenance reboot, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). The range for the maintenance extension is between 1 and 14 days from the initial scheduled maintenance date. Example: `2018-05-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_LOAD_BALANCER_BACKEND_T Type

Represents the load balancer Backend that is configured for an instance pool instance.

Syntax
```

```

Fields

Field Description

`load_balancer_id`

(required) The OCID of the load balancer attached to the instance pool.

`backend_set_name`

(required) The name of the backend set on the load balancer.

`backend_name`

(required) The name of the backend in the backend set.

`backend_health_status`

(required) The health of the backend as observed by the load balancer.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_LOAD_BALANCER_BACKEND_TBL Type

Nested table type of dbms_cloud_oci_core_instance_pool_instance_load_balancer_backend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_T Type

Information about an instance that belongs to an instance pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`instance_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance pool.

`availability_domain`

(required) The availability domain the instance is running in.

`lifecycle_state`

(required) The attachment state of the instance in relation to the instance pool.

Allowed values are: 'ATTACHING', 'ACTIVE', 'DETACHING'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the instance.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) The fault domain the instance is running in.

`instance_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration used to create the instance.

`l_region`

(required) The region that contains the availability domain the instance is running in.

`shape`

(required) The shape of the instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

`state`

(required) The lifecycle state of the instance. Refer to `lifecycleState` in the`INSTANCE`Type resource.

`time_created`

(required) The date and time the instance pool instance was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`load_balancer_backends`

(optional) The load balancer backends that are configured for the instance.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SUBNET_DETAILS_T Type

Base details about the IPv6 subnet.

Syntax
```

```

Fields

Field Description

`is_assign_ipv6_ip`

(optional) Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled subnet. Default: False. When provided you may optionally provide an IPv6 prefix (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr` is not provided then an IPv6 prefix is chosen for you.

`ipv6_address_ipv6_subnet_cidr_pair_details`

(optional) A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address. You can provide only the prefix ranges and OCI will select an available address from the range. You can optionally choose to leave the prefix range empty and instead provide the specific IPv6 address that should be used from within that range.

`subnet_id`

(required) The subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the secondary VNIC.

### DBMS_CLOUD_OCI_CORE_INSTANCE_POWER_ACTION_DETAILS_T Type

A base object for all types of instance power action requests.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The type of power action to perform.

### DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_IMAGE_FILTER_DETAILS_T Type

These are the criteria for selecting an image. This is required if imageId is not specified.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing images to search

`defined_tags_filter`

(optional) Filter based on these defined tags. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`operating_system`

(optional) The image's operating system. Example: `Oracle Linux`

`operating_system_version`

(optional) The image's operating system version. Example: `7.2`

### DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_source_via_boot_volume_details_t`is a subtype of the`dbms_cloud_oci_core_instance_source_details_t`type.

Fields

Field Description

`boot_volume_id`

(required) The OCID of the boot volume used to boot the instance.

### DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_core_instance_source_via_image_details_t`is a subtype of the`dbms_cloud_oci_core_instance_source_details_t`type.

Fields

Field Description

`boot_volume_size_in_g_bs`

(optional) The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 32,768 GB (32 TB).

`image_id`

(optional) The OCID of the image used to boot the instance.

`kms_key_id`

(optional) The OCID of the Vault service key to assign as the master encryption key for the boot volume.

`boot_volume_vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.

`instance_source_image_filter_details`

(optional)

### DBMS_CLOUD_OCI_CORE_INSTANCE_SUMMARY_T Type

Condensed instance data when listing instances in an instance pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the instance.

`availability_domain`

(required) The availability domain the instance is running in.

`compartment_id`

(required) The OCID of the compartment that contains the instance.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) The fault domain the instance is running in.

`instance_configuration_id`

(required) The OCID of the instance confgiuration used to create the instance.

`l_region`

(required) The region that contains the availability domain the instance is running in.

`shape`

(optional) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`state`

(required) The current state of the instance pool instance.

`time_created`

(required) The date and time the instance pool instance was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`load_balancer_backends`

(optional) The load balancer backends that are configured for the instance pool instance.

### DBMS_CLOUD_OCI_CORE_INTEL_ICELAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with the BM.Standard3.64 shape or the BM.Optimized3.36 shape (the Intel Ice Lake platform).

Syntax
```

```

`dbms_cloud_oci_core_intel_icelake_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INTEL_ICELAKE_BM_PLATFORM_CONFIG_T Type

The platform configuration of a bare metal instance that uses the BM.Standard3.64 shape or the BM.Optimized3.36 shape (the Intel Ice Lake platform).

Syntax
```

```

`dbms_cloud_oci_core_intel_icelake_bm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INTEL_SKYLAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a bare metal instance with an Intel X7-based processor (the Intel Skylake platform).

Syntax
```

```

`dbms_cloud_oci_core_intel_skylake_bm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INTEL_SKYLAKE_BM_PLATFORM_CONFIG_T Type

The platform configuration of a bare metal instance that uses one of the following shapes: BM.Standard2.52, BM.GPU2.2, BM.GPU3.8, or BM.DenseIO2.52 (the Intel Skylake platform).

Syntax
```

```

`dbms_cloud_oci_core_intel_skylake_bm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

Fields

Field Description

`numa_nodes_per_socket`

(optional) The number of NUMA nodes per socket (NPS).

Allowed values are: 'NPS1', 'NPS2'

`is_symmetric_multi_threading_enabled`

(optional) Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also called simultaneous multithreading (SMT) or Intel Hyper-Threading. Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple independent threads of execution, to better use the resources and increase the efficiency of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which can provide higher or more predictable performance for some workloads.

`is_input_output_memory_management_unit_enabled`

(optional) Whether the input-output memory management unit is enabled.

`percentage_of_cores_enabled`

(optional) The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage results in a fractional number of cores, the system rounds up the number of cores across processors and provisions an instance with a whole number of cores. If the applications that you run on the instance use a core-based licensing model and need fewer cores than the full size of the shape, you can disable cores to reduce your licensing costs. The instance itself is billed for the full shape, regardless of whether all cores are enabled.

`config_map`

(optional) Instance Platform Configuration Configuration Map for flexible setting input.

### DBMS_CLOUD_OCI_CORE_INTEL_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type

The platform configuration used when launching a virtual machine instance with the Intel platform.

Syntax
```

```

`dbms_cloud_oci_core_intel_vm_launch_instance_platform_config_t`is a subtype of the`dbms_cloud_oci_core_launch_instance_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_INTEL_VM_PLATFORM_CONFIG_T Type

The platform configuration of a virtual machine instance that uses the Intel platform.

Syntax
```

```

`dbms_cloud_oci_core_intel_vm_platform_config_t`is a subtype of the`dbms_cloud_oci_core_platform_config_t`type.

### DBMS_CLOUD_OCI_CORE_INTERNET_GATEWAY_T Type

Represents a router that connects the edge of a VCN with the Internet. For an example scenario that uses an internet gateway, see[Typical Networking Service Scenarios](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#scenarios). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the internet gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_IPSEC_TUNNEL_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the IPSec tunnel attached to the DRG.

Syntax
```

```

`dbms_cloud_oci_core_ipsec_tunnel_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_details_t`type.

Fields

Field Description

`ipsec_connection_id`

(optional) The IPSec connection that contains the attached IPSec tunnel.

`transport_attachment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit's DRG attachment.

### DBMS_CLOUD_OCI_CORE_IPV6_T Type

An *IPv6* is a conceptual term that refers to an IPv6 address and related properties. The `IPv6` object is the API representation of an IPv6. You can create and assign an IPv6 to any VNIC that is in an IPv6-enabled subnet in an IPv6-enabled VCN. **Note:** IPv6 addressing is supported for all commercial and government regions. For important details about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the IPv6. This is the same as the VNIC's compartment.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPv6.

`ip_address`

(required) The IPv6 address of the `IPv6` object. The address is within the IPv6 prefix of the VNIC's subnet (see the `ipv6CidrBlock` attribute for the`SUBNET`Type object. Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`

`lifecycle_state`

(required) The IPv6's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the VNIC is in.

`time_created`

(required) The date and time the IPv6 was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC the IPv6 is assigned to. The VNIC and IPv6 must be in the same subnet.

### DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type

Configuration options for the Oracle Cloud Agent software running on the instance.

Syntax
```

```

Fields

Field Description

`is_monitoring_disabled`

(optional) Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. Default value is false (monitoring plugins are enabled). These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.

`is_management_disabled`

(optional) Whether Oracle Cloud Agent can run all the available management plugins. Default value is false (management plugins are enabled). These are the management plugins: OS Management Service Agent and Compute Instance Run Command. The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.

`are_all_plugins_disabled`

(optional) Whether Oracle Cloud Agent can run all the available plugins. This includes the management and monitoring plugins. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`plugins_config`

(optional) The configuration of plugins associated with this instance.

### DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_AVAILABILITY_CONFIG_DETAILS_T Type

Options for VM migration during infrastructure maintenance events and for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.

Syntax
```

```

Fields

Field Description

`is_live_migration_preferred`

(optional) Whether to live migrate supported VM instances to a healthy physical VM host without disrupting running instances during infrastructure maintenance events. If null, Oracle chooses the best option for migrating the VM during infrastructure maintenance events.

`recovery_action`

(optional) The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.

Allowed values are: 'RESTORE_INSTANCE', 'STOP_INSTANCE'

### DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested for the instance. If the parameter is provided, the instance is created with the resources that you specify. If some properties are missing or the entire parameter is not provided, the instance is created with the default configuration values for the `shape` that you specify. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`vcpus`

(optional) The total number of VCPUs available to the instance. This can be used instead of OCPUs, in which case the actual number of OCPUs will be calculated based on this value and the actual hardware. This must be a multiple of 2.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

`baseline_ocpu_utilization`

(optional) The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`. The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

`nvmes`

(optional) The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.

### DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_DETAILS_T Type

Instance launch details. Use the `sourceDetails` parameter to specify whether a boot volume or an image should be used to launch a new instance.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the instance. Example: `Uocm:PHX-AD-1`

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation this instance is launched under. You can opt out of all default reservations by specifying an empty string as input for this field. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`compartment_id`

(required) The OCID of the compartment.

`create_vnic_details`

(optional)

`dedicated_vm_host_id`

(optional) The OCID of the dedicated virtual machine host to place the instance on.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`fault_domain`

(optional) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains. If you do not specify the fault domain, the system selects one for you. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`compute_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)that the instance will be created in.

`hostname_label`

(optional) Deprecated. Instead use `hostnameLabel` in`CREATE_VNIC_DETAILS`Type. If you provide both, the values must match.

`image_id`

(optional) Deprecated. Use `sourceDetails` with`INSTANCE_SOURCE_VIA_IMAGE_DETAILS`Function source type instead. If you specify values for both, the values must match.

`ipxe_script`

(optional) This is an advanced option. When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process. If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots. Be aware that the same iPXE script will run every time an instance boots, not only after the initial LaunchInstance call. The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot. If your instance boot volume attachment type is paravirtualized, the boot volume is attached to the instance through virtio-scsi and no iPXE script is used. If your instance boot volume attachment type is paravirtualized and you use custom iPXE to network boot into your instance, the primary boot volume is attached as a data volume through virtio-scsi drive. For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see[Bring Your Own Image](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm). For more information about iPXE, see http://ipxe.org.

`launch_options`

(optional)

`instance_options`

(optional)

`availability_config`

(optional)

`preemptible_instance_config`

(optional)

`metadata`

(optional) Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance. A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to: * Provide information to[Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)to be used for various system initialization tasks. * Get information about the instance, including the custom metadata that you provide when you launch the instance. **Providing Cloud-Init Metadata** You can use the following metadata key names to provide information to Cloud-Init: **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the `authorized_keys` file, as shown in the example below. **\"user_data\"** - Provide your own base64-encoded data to be used by Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For information about how to take advantage of user data, see the[Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html). **Metadata Example** \"metadata\" : { \"quake_bot_level\" : \"Severe\", \"ssh_authorized_keys\" : \"ssh-rsa &lt;your_public_SSH_key&gt;== rsa-key-20160227\", \"user_data\" : \"&lt;your_public_SSH_key&gt;==\" } **Getting Metadata on the Instance** To get information about your instance, connect to the instance using SSH and issue any of the following GET requests: curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/ curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/ curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/&lt;any-key-name&gt; You'll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively. The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`agent_config`

(optional)

`shape`

(optional) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`shape_config`

(optional)

`source_details`

(optional)

`subnet_id`

(optional) Deprecated. Instead use `subnetId` in`CREATE_VNIC_DETAILS`Type. At least one of them is required; if you provide both, the values must match.

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.

`platform_config`

(optional)

`instance_configuration_id`

(optional) The OCID of the Instance Configuration containing instance launch details. Any other fields supplied in this instance launch request will override the details stored in the Instance Configuration for this instance launch.

### DBMS_CLOUD_OCI_CORE_LETTER_OF_AUTHORITY_T Type

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

### DBMS_CLOUD_OCI_CORE_LOCAL_PEERING_GATEWAY_T Type

A local peering gateway (LPG) is an object on a VCN that lets that VCN peer with another VCN in the same region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the LPG.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_LOOP_BACK_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the loopback attachment on the DRG. A loopback attachment can be used to terminate a virtual circuit that is carrying an IPSec tunnel, routing traffic directly to the IPSec tunnel attachment where the tunnel can terminate.

Syntax
```

```

`dbms_cloud_oci_core_loop_back_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_details_t`type.

Fields

Field Description

`ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target IPSec tunnel attachment.

### DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_ENTRY_T Type

One Trusted Platform Module (TPM) Platform Configuration Register (PCR) entry. The entry might be measured during boot, or specified in a policy.

Syntax
```

```

Fields

Field Description

`pcr_index`

(optional) The index of the policy.

`value`

(optional) The hashed PCR value.

`hash_algorithm`

(optional) The type of algorithm used to calculate the hash.

### DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_core_measured_boot_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_REPORT_MEASUREMENTS_T Type

A list of Trusted Platform Module (TPM) Platform Configuration Register (PCR) entries.

Syntax
```

```

Fields

Field Description

`policy`

(optional) The list of expected PCR entries to use during verification.

`actual`

(optional) The list of actual PCR entries measured during boot.

### DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_REPORT_T Type

The measured boot report for a shielded instance.

Syntax
```

```

Fields

Field Description

`is_policy_verification_successful`

(required) Whether the verification succeeded, and the new values match the expected values.

`measurements`

(optional)

### DBMS_CLOUD_OCI_CORE_MEMBER_REPLICA_T Type

OCIDs for the volume replicas in this volume group replica.

Syntax
```

```

Fields

Field Description

`volume_replica_id`

(required) The volume replica ID.

`membership_state`

(optional) Membership state of the volume replica in relation to the volume group replica.

Allowed values are: 'ADD_PENDING', 'STABLE', 'REMOVE_PENDING'

### DBMS_CLOUD_OCI_CORE_MODIFY_VCN_CIDR_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_NAT_GATEWAY_T Type

A NAT (Network Address Translation) gateway, which represents a router that lets instances without public IPs contact the public internet without exposing the instance to inbound internet traffic. For more information, see[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the NAT gateway.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_NETWORK_SECURITY_GROUP_T Type

A *network security group* (NSG) provides virtual firewall rules for a specific set of`VNIC`Type in a VCN. Compare NSGs with`SECURITY_LIST`Type, which provide virtual firewall rules to all the VNICs in a *subnet*. A network security group consists of two items: * The set of`VNIC`Type that all have the same security rule needs (for example, a group of Compute instances all running the same application) * A set of NSG`SECURITY_RULE`Type that apply to the VNICs in the group After creating an NSG, you can add VNICs and security rules to it. For example, when you create an instance, you can specify one or more NSGs to add the instance to (see`CREATE_VNIC_DETAILS`Function). Or you can add an existing instance to an NSG with`UPDATE_VNIC`Function. To add security rules to an NSG, see`ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function. To list the VNICs in an NSG, see`LIST_NETWORK_SECURITY_GROUP_VNICS`Function. To list the security rules in an NSG, see`LIST_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function. For more information about network security groups, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). **Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure all of the following are set correctly: * Any security rules in any NSGs the instance's VNIC belongs to * Any`SECURITY_LIST`Type associated with the instance's subnet * The instance's OS firewall rules To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the network security group is in.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`lifecycle_state`

(required) The network security group's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED'

`time_created`

(required) The date and time the network security group was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group's VCN.

### DBMS_CLOUD_OCI_CORE_NETWORK_SECURITY_GROUP_VNIC_T Type

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

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ENTITY_RELATIONSHIP_T Type

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

### DBMS_CLOUD_OCI_CORE_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ENTITY_RELATIONSHIP_TBL Type

Nested table type of dbms_cloud_oci_core_topology_entity_relationship_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_T Type

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

### DBMS_CLOUD_OCI_CORE_NETWORKING_TOPOLOGY_T Type

Defines the representation of a virtual network topology for a region. See[Network Visualizer Documentation](https://docs.oracle.com/iaas/Content/Network/Concepts/network_visualizer.htm)for more information, including conventions and pictures of symbols.

Syntax
```

```

`dbms_cloud_oci_core_networking_topology_t`is a subtype of the`dbms_cloud_oci_core_topology_t`type.

### DBMS_CLOUD_OCI_CORE_PARAVIRTUALIZED_VOLUME_ATTACHMENT_T Type

A paravirtualized volume attachment.

Syntax
```

```

`dbms_cloud_oci_core_paravirtualized_volume_attachment_t`is a subtype of the`dbms_cloud_oci_core_volume_attachment_t`type.

### DBMS_CLOUD_OCI_CORE_PEER_REGION_FOR_REMOTE_PEERING_T Type

Details about a region that supports remote VCN peering. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The region's name. Example: `us-phoenix-1`

### DBMS_CLOUD_OCI_CORE_PERCENTAGE_OF_CORES_ENABLED_OPTIONS_T Type

Configuration options for the percentage of cores enabled.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The minimum allowed percentage of cores enabled.

`l_max`

(optional) The maximum allowed percentage of cores enabled.

`default_value`

(optional) The default percentage of cores enabled.

### DBMS_CLOUD_OCI_CORE_PERFORMANCE_BASED_AUTOTUNE_POLICY_T Type

If a volume is being throttled at the current setting for a certain period of time, auto-tune will gradually increase the volume’s performance limited up to Maximum VPUs/GB. After the volume has been idle at the current setting for a certain period of time, auto-tune will gradually decrease the volume’s performance limited down to Default/Minimum VPUs/GB.

Syntax
```

```

`dbms_cloud_oci_core_performance_based_autotune_policy_t`is a subtype of the`dbms_cloud_oci_core_autotune_policy_t`type.

Fields

Field Description

`max_vpus_per_gb`

(required) This will be the maximum VPUs/GB performance level that the volume will be auto-tuned temporarily based on performance monitoring.

### DBMS_CLOUD_OCI_CORE_PRIVATE_IP_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_PUBLIC_IP_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`lifecycle_state`

(optional) The public IP pool's current state.

Allowed values are: 'INACTIVE', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the public IP pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_SUMMARY_T Type

Summary information about a public IP pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the public IP pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`lifecycle_state`

(optional) The public IP pool's current state.

`time_created`

(optional) The date and time the public IP pool was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_core_public_ip_pool_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_COLLECTION_T Type

Results of a `ListPublicIpPool` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of public IP pool summaries.

### DBMS_CLOUD_OCI_CORE_REBOOT_MIGRATE_ACTION_DETAILS_T Type

Parameters for the `rebootMigrate``INSTANCE_ACTION`Function.

Syntax
```

```

`dbms_cloud_oci_core_reboot_migrate_action_details_t`is a subtype of the`dbms_cloud_oci_core_instance_power_action_details_t`type.

Fields

Field Description

`delete_local_storage`

(optional) For bare metal instances that have local storage, this must be set to true to verify that the local storage will be deleted during the migration. For instances without, this parameter has no effect.

`time_scheduled`

(optional) If present, this parameter will set (or reset) the scheduled time that the instance will be reboot migrated in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). This will also change the `timeMaintenanceRebootDue` field on the instance. If not present, the reboot migration will be triggered immediately.

### DBMS_CLOUD_OCI_CORE_REMOTE_PEERING_CONNECTION_T Type

A remote peering connection (RPC) is an object on a DRG that lets the VCN that is attached to the DRG peer with a VCN in a different region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the RPC.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG that this RPC belongs to.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_REMOTE_PEERING_CONNECTION_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the DRG attachment to another DRG.

Syntax
```

```

`dbms_cloud_oci_core_remote_peering_connection_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_details_t`type.

### DBMS_CLOUD_OCI_CORE_REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to remove statements from a route distribution.

Syntax
```

```

Fields

Field Description

`statement_ids`

(optional) The Oracle-assigned ID of each route distribution to remove.

### DBMS_CLOUD_OCI_CORE_REMOVE_DRG_ROUTE_RULES_DETAILS_T Type

Details used in a request to remove static routes from a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rule_ids`

(optional) The Oracle-assigned ID of each DRG route rule to be deleted.

### DBMS_CLOUD_OCI_CORE_REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rule_ids`

(optional) The Oracle-assigned ID of each`SECURITY_RULE`Type to be deleted.

### DBMS_CLOUD_OCI_CORE_REMOVE_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type

The information needed to remove capacity from a public IP pool.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to remove from the public IP pool. Example: `10.0.1.0/24`

### DBMS_CLOUD_OCI_CORE_REMOVE_SUBNET_IPV6_CIDR_DETAILS_T Type

Details object for removing an IPv6 prefix from a subnet.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(required) This field is not required and should only be specified when removing an IPv6 prefix from a subnet's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/64`

### DBMS_CLOUD_OCI_CORE_REMOVE_VCN_CIDR_DETAILS_T Type

Details for removing a CIDR block from a VCN.

Syntax
```

```

Fields

Field Description

`cidr_block`

(required) The CIDR block to remove.

### DBMS_CLOUD_OCI_CORE_REMOVE_VCN_IPV6_CIDR_DETAILS_T Type

Details used when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix. You can only remove one of these per request.

Syntax
```

```

Fields

Field Description

`ipv6_cidr_block`

(optional) This field is not required and should only be specified when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix from a VCN's IPv6 address space. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123::/56`

### DBMS_CLOUD_OCI_CORE_RESET_ACTION_DETAILS_T Type

Parameters for the `reset``INSTANCE_ACTION`Function. If omitted, default values are used.

Syntax
```

```

`dbms_cloud_oci_core_reset_action_details_t`is a subtype of the`dbms_cloud_oci_core_instance_power_action_details_t`type.

Fields

Field Description

`allow_dense_reboot_migration`

(optional) For instances that use a DenseIO shape, the flag denoting whether[reboot migration](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm#reboot)is performed for the instance. The default value is `false`. If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the maintenance process. The local NVMe-based SSD will be preserved. If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be deleted. A short downtime occurs during the migration. **Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.

### DBMS_CLOUD_OCI_CORE_ROUTE_TABLE_T Type

A collection of `RouteRule` objects, which are used to route packets based on destination IP to a particular network entity. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the route table.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_SECURITY_LIST_T Type

A set of virtual firewall rules for your VCN. Security lists are configured at the subnet level, but the rules are applied to the ingress and egress traffic for the individual instances in the subnet. The rules can be stateful or stateless. For more information, see[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). **Note:** Compare security lists to`NETWORK_SECURITY_GROUP`Types, which let you apply a set of security rules to a *specific set of VNICs* instead of an entire subnet. Oracle recommends using network security groups instead of security lists, although you can use either or both together. **Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure both the security lists associated with the instance's subnet and the instance's firewall rules are set correctly. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the security list.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(required) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_SERVICE_T Type

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

### DBMS_CLOUD_OCI_CORE_SERVICE_ID_RESPONSE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service.

`service_name`

(required) The name of the service.

### DBMS_CLOUD_OCI_CORE_SERVICE_ID_RESPONSE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_service_id_response_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_SERVICE_GATEWAY_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_SHAPE_OCPU_OPTIONS_T Type

For a flexible shape, the number of OCPUs available for instances that use this shape. If this field is null, then this shape has a fixed number of OCPUs equal to `ocpus`.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The minimum number of OCPUs.

`l_max`

(optional) The maximum number of OCPUs.

`max_per_numa_node`

(optional) The maximum number of cores available per NUMA node.

### DBMS_CLOUD_OCI_CORE_SHAPE_MEMORY_OPTIONS_T Type

For a flexible shape, the amount of memory available for instances that use this shape. If this field is null, then this shape has a fixed amount of memory equivalent to `memoryInGBs`.

Syntax
```

```

Fields

Field Description

`min_in_g_bs`

(optional) The minimum amount of memory, in gigabytes.

`max_in_g_bs`

(optional) The maximum amount of memory, in gigabytes.

`default_per_ocpu_in_g_bs`

(optional) The default amount of memory per OCPU available for this shape, in gigabytes.

`min_per_ocpu_in_g_bs`

(optional) The minimum amount of memory per OCPU available for this shape, in gigabytes.

`max_per_ocpu_in_g_bs`

(optional) The maximum amount of memory per OCPU available for this shape, in gigabytes.

`max_per_numa_node_in_g_bs`

(optional) The maximum amount of memory per NUMA node, in gigabytes.

### DBMS_CLOUD_OCI_CORE_SHAPE_NETWORKING_BANDWIDTH_OPTIONS_T Type

For a flexible shape, the amount of networking bandwidth available for instances that use this shape. If this field is null, then this shape has a fixed amount of bandwidth equivalent to `networkingBandwidthInGbps`.

Syntax
```

```

Fields

Field Description

`min_in_gbps`

(optional) The minimum amount of networking bandwidth, in gigabits per second.

`max_in_gbps`

(optional) The maximum amount of networking bandwidth, in gigabits per second.

`default_per_ocpu_in_gbps`

(optional) The default amount of networking bandwidth per OCPU, in gigabits per second.

### DBMS_CLOUD_OCI_CORE_SHAPE_MAX_VNIC_ATTACHMENT_OPTIONS_T Type

For a flexible shape, the number of VNIC attachments that are available for instances that use this shape. If this field is null, then this shape has a fixed maximum number of VNIC attachments equal to `maxVnicAttachments`.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The lowest maximum value of VNIC attachments.

`l_max`

(optional) The highest maximum value of VNIC attachments.

`default_per_ocpu`

(optional) The default number of VNIC attachments allowed per OCPU.

### DBMS_CLOUD_OCI_CORE_SHAPE_SECURE_BOOT_OPTIONS_T Type

Configuration options for Secure Boot.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Boolean values that indicate whether Secure Boot can be enabled or disabled.

`is_default_enabled`

(optional) Whether Secure Boot is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_MEASURED_BOOT_OPTIONS_T Type

Configuration options for the Measured Boot feature.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Boolean values that indicate whether the Measured Boot feature can be enabled or disabled.

`is_default_enabled`

(optional) Whether the Measured Boot feature is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_TRUSTED_PLATFORM_MODULE_OPTIONS_T Type

Configuration options for the Trusted Platform Module (TPM).

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Boolean values that indicate whether the Trusted Platform Module can be enabled or disabled.

`is_default_enabled`

(optional) Whether the Trusted Platform Module is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_NUMA_NODES_PER_SOCKET_PLATFORM_OPTIONS_T Type

Configuration options for NUMA nodes per socket.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) The supported values for this platform configuration property.

Allowed values are: 'NPS0', 'NPS1', 'NPS2', 'NPS4'

`default_value`

(optional) The default NUMA nodes per socket configuration.

### DBMS_CLOUD_OCI_CORE_SHAPE_MEMORY_ENCRYPTION_OPTIONS_T Type

Configuration options for memory encryption.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Whether memory encryption can be enabled.

`is_default_enabled`

(optional) Whether memory encryption is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_SYMMETRIC_MULTI_THREADING_ENABLED_PLATFORM_OPTIONS_T Type

Configuration options for symmetric multithreading (also called simultaneous multithreading or SMT).

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Whether symmetric multithreading can be enabled.

`is_default_enabled`

(optional) Whether symmetric multithreading is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_ACCESS_CONTROL_SERVICE_ENABLED_PLATFORM_OPTIONS_T Type

Configuration options for the Access Control Service.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Whether the Access Control Service can be enabled.

`is_default_enabled`

(optional) Whether the Access Control Service is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_VIRTUAL_INSTRUCTIONS_ENABLED_PLATFORM_OPTIONS_T Type

Configuration options for the virtualization instructions.

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Whether virtualization instructions can be enabled.

`is_default_enabled`

(optional) Whether virtualization instructions are enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_INPUT_OUTPUT_MEMORY_MANAGEMENT_UNIT_ENABLED_PLATFORM_OPTIONS_T Type

Configuration options for the input-output memory management unit (IOMMU).

Syntax
```

```

Fields

Field Description

`allowed_values`

(optional) Whether the input-output memory management unit can be enabled.

`is_default_enabled`

(optional) Whether the input-output memory management unit is enabled by default.

### DBMS_CLOUD_OCI_CORE_SHAPE_PLATFORM_CONFIG_OPTIONS_T Type

The list of supported platform configuration options for this shape.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of platform being configured.

Allowed values are: 'AMD_MILAN_BM', 'AMD_MILAN_BM_GPU', 'AMD_ROME_BM', 'AMD_ROME_BM_GPU', 'GENERIC_BM', 'INTEL_ICELAKE_BM', 'INTEL_SKYLAKE_BM', 'AMD_VM', 'INTEL_VM'

`secure_boot_options`

(optional)

`measured_boot_options`

(optional)

`trusted_platform_module_options`

(optional)

`numa_nodes_per_socket_platform_options`

(optional)

`memory_encryption_options`

(optional)

`symmetric_multi_threading_options`

(optional)

`access_control_service_options`

(optional)

`virtual_instructions_options`

(optional)

`input_output_memory_management_unit_options`

(optional)

`percentage_of_cores_enabled_options`

(optional)

### DBMS_CLOUD_OCI_CORE_SHAPE_ALTERNATIVE_OBJECT_T Type

The shape that Oracle recommends you to use an alternative to the current shape.

Syntax
```

```

Fields

Field Description

`shape_name`

(required) The name of the shape.

### DBMS_CLOUD_OCI_CORE_SHAPE_ALTERNATIVE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_core_shape_alternative_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_SHAPE_T Type

A compute instance shape that can be used in`LAUNCH_INSTANCE`Function. For more information, see[Overview of the Compute Service](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm)and[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).

Syntax
```

```

Fields

Field Description

`baseline_ocpu_utilizations`

(optional) For a subcore burstable VM, the supported baseline OCPU utilization for instances that use this shape.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

`min_total_baseline_ocpus_required`

(optional) For a subcore burstable VM, the minimum total baseline OCPUs required. The total baseline OCPUs is equal to baselineOcpuUtilization chosen multiplied by the number of OCPUs chosen.

`shape`

(required) The name of the shape. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`processor_description`

(optional) A short description of the shape's processor (CPU).

`ocpus`

(optional) The default number of OCPUs available for this shape.

`memory_in_g_bs`

(optional) The default amount of memory available for this shape, in gigabytes.

`network_ports`

(optional) The number of physical network interface card (NIC) ports available for this shape.

`networking_bandwidth_in_gbps`

(optional) The networking bandwidth available for this shape, in gigabits per second.

`max_vnic_attachments`

(optional) The maximum number of VNIC attachments available for this shape.

`gpus`

(optional) The number of GPUs available for this shape.

`gpu_description`

(optional) A short description of the graphics processing unit (GPU) available for this shape. If the shape does not have any GPUs, this field is `null`.

`local_disks`

(optional) The number of local disks available for this shape.

`local_disks_total_size_in_g_bs`

(optional) The aggregate size of the local disks available for this shape, in gigabytes. If the shape does not have any local disks, this field is `null`.

`local_disk_description`

(optional) A short description of the local disks available for this shape. If the shape does not have any local disks, this field is `null`.

`rdma_ports`

(optional) The number of networking ports available for the remote direct memory access (RDMA) network between nodes in a high performance computing (HPC) cluster network. If the shape does not support cluster networks, this value is `0`.

`rdma_bandwidth_in_gbps`

(optional) The networking bandwidth available for the remote direct memory access (RDMA) network for this shape, in gigabits per second.

`is_live_migration_supported`

(optional) Whether live migration is supported for this shape.

`ocpu_options`

(optional)

`memory_options`

(optional)

`networking_bandwidth_options`

(optional)

`max_vnic_attachment_options`

(optional)

`platform_config_options`

(optional)

`is_billed_for_stopped_instance`

(optional) Whether billing continues when the instances that use this shape are in the stopped state.

`billing_type`

(optional) How instances that use this shape are charged.

Allowed values are: 'ALWAYS_FREE', 'LIMITED_FREE', 'PAID'

`quota_names`

(optional) The list of of compartment quotas for the shape.

`is_subcore`

(optional) Whether the shape supports creating subcore or burstable instances. A[burstable instance](https://docs.oracle.com/iaas/Content/Compute/References/burstable-instances.htm)is a virtual machine (VM) instance that provides a baseline level of CPU performance with the ability to burst to a higher level to support occasional spikes in usage.

`is_flexible`

(optional) Whether the shape supports creating flexible instances. A[flexible shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#flexible)is a shape that lets you customize the number of OCPUs and the amount of memory when launching or resizing your instance.

`resize_compatible_shapes`

(optional) The list of compatible shapes that this shape can be changed to. For more information, see[Changing the Shape of an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).

`recommended_alternatives`

(optional) The list of shapes and shape details (if applicable) that Oracle recommends that you use as an alternative to the current shape.

### DBMS_CLOUD_OCI_CORE_SOFT_RESET_ACTION_DETAILS_T Type

Parameters for the `softReset``INSTANCE_ACTION`Function. If omitted, default values are used.

Syntax
```

```

`dbms_cloud_oci_core_soft_reset_action_details_t`is a subtype of the`dbms_cloud_oci_core_instance_power_action_details_t`type.

Fields

Field Description

`allow_dense_reboot_migration`

(optional) For instances that use a DenseIO shape, the flag denoting whether[reboot migration](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm#reboot)is performed for the instance. The default value is `false`. If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the maintenance process. The local NVMe-based SSD will be preserved. If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be deleted. A short downtime occurs during the migration. **Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.

### DBMS_CLOUD_OCI_CORE_SUBNET_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options that the subnet uses.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed. The absence of this parameter means the Internet and VCN Resolver will not resolve hostnames of instances in this subnet. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `subnet123`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The subnet's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ipv6_cidr_block`

(optional) For an IPv6-enabled subnet, this is the IPv6 prefix for the subnet's IP address space. The subnet size is always /64. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefixes, BYOIPv6 prefixes) for the subnet.

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

### DBMS_CLOUD_OCI_CORE_SUBNET_TOPOLOGY_T Type

Defines the visualization of a subnet in a VCN. See[Network Visualizer Documentation](https://docs.oracle.com/iaas/Content/Network/Concepts/network_visualizer.htm)for more information, including conventions and pictures of symbols.

Syntax
```

```

`dbms_cloud_oci_core_subnet_topology_t`is a subtype of the`dbms_cloud_oci_core_topology_t`type.

Fields

Field Description

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet for which the visualization is generated.

### DBMS_CLOUD_OCI_CORE_TERMINATE_PREEMPTION_ACTION_T Type

Terminates the preemptible instance when it is interrupted for eviction.

Syntax
```

```

`dbms_cloud_oci_core_terminate_preemption_action_t`is a subtype of the`dbms_cloud_oci_core_preemption_action_t`type.

Fields

Field Description

`preserve_boot_volume`

(optional) Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ASSOCIATED_WITH_RELATIONSHIP_DETAILS_T Type

Defines association details for an `associatedWith` relationship.

Syntax
```

```

Fields

Field Description

`via`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the entities via which the relationship is created. For example an instance is associated with a network security group via the VNIC attachment and the VNIC.

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ASSOCIATED_WITH_ENTITY_RELATIONSHIP_T Type

Defines the `AssociatedWith` relationship between virtual network topology entities. An `AssociatedWith` relationship is defined when there is no obvious `contains` relationship but entities are still related. For example, a DRG is associated with a VCN because a DRG is not managed by VCN but can be attached to a VCN.

Syntax
```

```

`dbms_cloud_oci_core_topology_associated_with_entity_relationship_t`is a subtype of the`dbms_cloud_oci_core_topology_entity_relationship_t`type.

Fields

Field Description

`associated_with_details`

(optional)

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_CONTAINS_ENTITY_RELATIONSHIP_T Type

Defines the `contains` relationship between virtual network topology entities. A `Contains` relationship is defined when an entity fully owns, contains or manages another entity. For example, a subnet is contained and managed in the scope of a VCN, therefore a VCN has a `contains` relationship to a subnet.

Syntax
```

```

`dbms_cloud_oci_core_topology_contains_entity_relationship_t`is a subtype of the`dbms_cloud_oci_core_topology_entity_relationship_t`type.

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ROUTES_TO_RELATIONSHIP_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_TOPOLOGY_ROUTES_TO_ENTITY_RELATIONSHIP_T Type

Defines the `routesTo` relationship between virtual network topology entities. A `RoutesTo` relationship is defined when a routing table and a routing rule are used to govern how to route traffic from one entity to another. For example, a DRG might have a routing rule to send certain traffic to an LPG.

Syntax
```

```

`dbms_cloud_oci_core_topology_routes_to_entity_relationship_t`is a subtype of the`dbms_cloud_oci_core_topology_entity_relationship_t`type.

Fields

Field Description

`route_rule_details`

(required)

### DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_ANSWER_TBL Type

Nested table type of dbms_cloud_oci_core_cpe_device_config_answer_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_TUNNEL_CPE_DEVICE_CONFIG_T Type

The set of CPE configuration answers for the tunnel, which the customer provides in`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of`CPE_DEVICE_SHAPE_DETAIL`Type). See these related operations: *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_CPE_DEVICE_CONFIG_CONTENT`Function

Syntax
```

```

Fields

Field Description

`tunnel_cpe_device_config_parameter`

(optional)

### DBMS_CLOUD_OCI_CORE_TUNNEL_ROUTE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_CORE_TUNNEL_SECURITY_ASSOCIATION_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`size_in_g_bs`

(optional) The size to resize the volume to in GBs. Has to be larger than the current size.

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`boot_volume_replicas`

(optional) The list of boot volume replicas that this boot volume will be updated to have in the specified destination availability domains.

`autotune_policies`

(optional) The list of autotune policies to be enabled for this volume.

### DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_KMS_KEY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the new Vault service key to assign to protect the specified volume. This key has to be a valid Vault service key, and policies must exist to allow the user and the Block Volume service to access this key. If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.

### DBMS_CLOUD_OCI_CORE_UPDATE_BYOIP_RANGE_DETAILS_T Type

The information used to update a `ByoipRange` resource.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_CAPACITY_SOURCE_DETAILS_T Type

A capacity source of bare metal hosts.

Syntax
```

```

Fields

Field Description

`capacity_type`

(required) The capacity type of bare metal hosts.

### DBMS_CLOUD_OCI_CORE_UPDATE_CAPTURE_FILTER_DETAILS_T Type

These details can be included in a request to update a capture filter. A capture filter contains a set of rules governing what traffic a VTAP mirrors or a VCN flow log collects.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`vtap_capture_filter_rules`

(optional) The set of rules governing what traffic a VTAP mirrors.

`flow_log_capture_filter_rules`

(optional) The set of rules governing what traffic the VCN flow log collects.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_T Type

The data to update an instance pool within a cluster network.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance pool.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`l_size`

(optional) The number of instances that should be in the instance pool. To determine whether capacity is available for a specific shape before you resize an instance pool, use the`CREATE_COMPUTE_CAPACITY_REPORT`Function operation.

`instance_configuration_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration associated with the instance pool.

### DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_update_cluster_network_instance_pool_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_DETAILS_T Type

The data to update a[cluster network with instance pools](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_pools`

(optional) The instance pools in the cluster network to update.

### DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CAPACITY_RESERVATION_DETAILS_T Type

Details for updating the compute capacity reservation.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_default_reservation`

(optional) Whether this capacity reservation is the default. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`instance_reservation_configs`

(optional) The capacity configurations for the capacity reservation. To use the reservation for the desired shape, specify the shape, count, and optionally the fault domain where you want this configuration.

### DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CAPACITY_TOPOLOGY_DETAILS_T Type

The details for updating the compute capacity topology.

Syntax
```

```

Fields

Field Description

`capacity_source`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CLUSTER_DETAILS_T Type

The data to update a compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_DETAILS_T Type

Create Image Capability Schema for an image.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`schema_data`

(optional) The map of each capability name to its ImageCapabilitySchemaDescriptor.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CORE_UPDATE_CONSOLE_HISTORY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_CPE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`cpe_device_shape_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device type. You can provide a value if you want to generate CPE device configuration content for IPSec connections that use this CPE. For a list of possible values, see`LIST_CPE_DEVICE_SHAPES`Function. For more information about generating CPE device configuration content, see: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG`Function

### DBMS_CLOUD_OCI_CORE_UPDATE_MACSEC_KEY_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_MACSEC_PROPERTIES_T Type

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

`is_unprotected_traffic_allowed`

(optional) Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails.

### DBMS_CLOUD_OCI_CORE_UPDATE_CROSS_CONNECT_DETAILS_T Type

Update a CrossConnect

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_active`

(optional) Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready. Example: `true`

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection this cross-connect uses.

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_CORE_UPDATE_CROSS_CONNECT_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`customer_reference_name`

(optional) A reference name or identifier for the physical fiber connection this cross-connect group uses.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`macsec_properties`

(optional)

### DBMS_CLOUD_OCI_CORE_UPDATE_DEDICATED_CAPACITY_SOURCE_DETAILS_T Type

A capacity source of bare metal hosts that is dedicated to a user.

Syntax
```

```

`dbms_cloud_oci_core_update_dedicated_capacity_source_details_t`is a subtype of the`dbms_cloud_oci_core_update_capacity_source_details_t`type.

### DBMS_CLOUD_OCI_CORE_UPDATE_DEDICATED_VM_HOST_DETAILS_T Type

Details for updating the dedicated virtual machine host details.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_DHCP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`options`

(optional)

`domain_name_type`

(optional) The search domain name type of DHCP options

Allowed values are: 'SUBNET_DOMAIN', 'VCN_DOMAIN', 'CUSTOM_DOMAIN'

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ATTACHMENT_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`export_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export route distribution used to specify how routes in the assigned DRG route table are advertised out through the attachment. If this value is null, no routes are advertised through this attachment.

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`default_drg_route_tables`

(optional)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type

Details used in a request to update a route distribution. You cannot assign a table to a virtual circuit or IPSec tunnel attachment if there is a static route rule for an RPC attachment.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_update_drg_route_distribution_statement_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type

Details request to update statements in a route distribution.

Syntax
```

```

Fields

Field Description

`statements`

(required) The route distribution statements to update, and the details to be updated.

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULE_DETAILS_T Type

Details used to update a route rule in the DRG route table.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle-assigned ID of each DRG route rule to update.

`destination`

(optional) The range of IP addresses used for matching when routing traffic. Potential values: * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.

`destination_type`

(optional) Type of destination for the rule. Allowed values: * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

Allowed values are: 'CIDR_BLOCK'

`next_hop_drg_attachment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_update_drg_route_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULES_DETAILS_T Type

Details used to update route rules in a DRG route table.

Syntax
```

```

Fields

Field Description

`route_rules`

(optional) The DRG rute rules to update.

### DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_TABLE_DETAILS_T Type

Details used in a request to update a DRG route table. You can't assign a table to a virtual circuit or IPSec tunnel attachment if there is a static route rule for an RPC attachment.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution used to specify how incoming route advertisements through referenced attachements are inserted into the DRG route table.

`is_ecmp_enabled`

(optional) If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-prem networks, set this value to true on the route table.

### DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`cpe_local_identifier`

(optional) Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`. For information about why you'd provide this value, see[If Your CPE Is Behind a NAT Device](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat). Example IP address: `10.0.3.3` Example hostname: `cpe.example.com`

`cpe_local_identifier_type`

(optional) The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.

Allowed values are: 'IP_ADDRESS', 'HOSTNAME'

`static_routes`

(optional) Static routes to the CPE. If you provide this attribute, it replaces the entire current set of static routes. A static route's CIDR must not be a multicast address or class E address. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). Example: `10.0.1.0/24` Example: `2001:db8::/32`

### DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`shared_secret`

(optional) The shared secret (pre-shared key) to use for the tunnel. Only numbers, letters, and spaces are allowed.

### DBMS_CLOUD_OCI_CORE_UPDATE_IMAGE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`operating_system`

(optional) Operating system Example: `Oracle Linux`

`operating_system_version`

(optional) Operating system version Example: `7.4`

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_AGENT_CONFIG_DETAILS_T Type

Configuration options for the Oracle Cloud Agent software running on the instance.

Syntax
```

```

Fields

Field Description

`is_monitoring_disabled`

(optional) Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.

`is_management_disabled`

(optional) Whether Oracle Cloud Agent can run all the available management plugins. These are the management plugins: OS Management Service Agent and Compute Instance Run Command. The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.

`are_all_plugins_disabled`

(optional) Whether Oracle Cloud Agent can run all the available plugins. This includes the management and monitoring plugins. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`plugins_config`

(optional) The configuration of plugins associated with this instance.

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_AVAILABILITY_CONFIG_DETAILS_T Type

Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware, including whether to live migrate supported VM instances when possible without sending a prior customer notification.

Syntax
```

```

Fields

Field Description

`is_live_migration_preferred`

(optional) Whether to live migrate supported VM instances to a healthy physical VM host without disrupting running instances during infrastructure maintenance events. If null, Oracle chooses the best option for migrating the VM during infrastructure maintenance events.

`recovery_action`

(optional) The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.

Allowed values are: 'RESTORE_INSTANCE', 'STOP_INSTANCE'

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_CONFIGURATION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_CONSOLE_CONNECTION_DETAILS_T Type

Specifies the properties for updating tags for an instance console connection.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested for the instance. If provided, the instance will be updated with the resources specified. In the case where some properties are missing, the missing values will be set to the default for the provided `shape`. Each shape only supports certain configurable values. If the `shape` is provided and the configuration values are invalid for that new `shape`, an error will be returned. If no `shape` is provided and the configuration values are invalid for the instance's existing shape, an error will be returned.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`vcpus`

(optional) The total number of VCPUs available to the instance. This can be used instead of OCPUs, in which case the actual number of OCPUs will be calculated based on this value and the actual hardware. This must be a multiple of 2.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

`baseline_ocpu_utilization`

(optional) The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`. The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

`nvmes`

(optional) The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.

### DBMS_CLOUD_OCI_CORE_UPDATE_LAUNCH_OPTIONS_T Type

Options for tuning the compatibility and performance of VM shapes.

Syntax
```

```

Fields

Field Description

`boot_volume_type`

(optional) Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images. Before you change the boot volume attachment type, detach all block volumes and VNICs except for the boot volume and the primary VNIC. If the instance is running when you change the boot volume attachment type, it will be rebooted. **Note:** Some instances might not function properly if you change the boot volume attachment type. After the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave as expected, the changes are not supported. Revert the instance to the original boot volume attachment type.

Allowed values are: 'ISCSI', 'PARAVIRTUALIZED'

`network_type`

(optional) Emulation type for the physical network interface card (NIC). * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. Before you change the networking type, detach all VNICs and block volumes except for the primary VNIC and the boot volume. The image must have paravirtualized drivers installed. For more information, see[Editing an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm). If the instance is running when you change the network type, it will be rebooted. **Note:** Some instances might not function properly if you change the networking type. After the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave as expected, the changes are not supported. Revert the instance to the original networking type.

Allowed values are: 'VFIO', 'PARAVIRTUALIZED'

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the volume's paravirtualized attachment. To enable in-transit encryption for block volumes and boot volumes, this field must be set to `true`. Data in transit is transferred over an internal and highly secure network. If you have specific compliance requirements related to the encryption of the data while it is moving between the instance and the boot volume or the block volume, you can enable in-transit encryption. In-transit encryption is not enabled by default. All boot volumes and block volumes are encrypted at rest. For more information, see[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#Encrypti).

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation this instance is launched under. You can remove the instance from a reservation by specifying an empty string as input for this field. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`agent_config`

(optional)

`metadata`

(optional) Custom metadata key/value string pairs that you provide. Any set of key/value pairs provided here will completely replace the current set of key/value pairs in the `metadata` field on the instance. The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance has launched. Any request that updates, removes, or adds either of these fields will be rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that already exist on the instance. The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance has launched. Any request that updates, removes, or adds either of these fields will be rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that already exist on the instance. The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

`shape`

(optional) The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. For more information about how to change shapes, and a list of shapes that are supported, see[Editing an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm). For details about the CPUs, memory, and other properties of each shape, see[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm). The new shape must be compatible with the image that was used to launch the instance. You can enumerate all available shapes and determine image compatibility by calling`LIST_SHAPES`Function. To determine whether capacity is available for a specific shape before you change the shape of an instance, use the`CREATE_COMPUTE_CAPACITY_REPORT`Function operation. If the instance is running when you change the shape, the instance is rebooted. Example: `VM.Standard2.1`

`shape_config`

(optional)

`update_operation_constraint`

(optional) The parameter acts as a fail-safe to prevent unwanted downtime when updating a running instance. The default is ALLOW_DOWNTIME. * `ALLOW_DOWNTIME` - Compute might reboot the instance while updating the instance if a reboot is required. * `AVOID_DOWNTIME` - If the instance is in running state, Compute tries to update the instance without rebooting it. If the instance requires a reboot to be updated, an error is returned and the instance is not updated. If the instance is stopped, it is updated and remains in the stopped state.

Allowed values are: 'ALLOW_DOWNTIME', 'AVOID_DOWNTIME'

`instance_options`

(optional)

`fault_domain`

(optional) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`launch_options`

(optional)

`availability_config`

(optional)

`time_maintenance_reboot_due`

(optional) For a VM instance, resets the scheduled time that the instance will be reboot migrated for infrastructure maintenance, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). If the instance hasn't been rebooted after this date, Oracle reboots the instance within 24 hours of the time and date that maintenance is due. To get the maximum possible date that a maintenance reboot can be extended, use`GET_INSTANCE_MAINTENANCE_REBOOT`Function. Regardless of how the instance is stopped, this flag is reset to empty as soon as the instance reaches the Stopped state. To reboot migrate a bare metal instance, use the`INSTANCE_ACTION`Function operation. For more information, see[Infrastructure Maintenance](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm). Example: `2018-05-25T21:10:29.600Z`

`dedicated_vm_host_id`

(optional) The OCID of the dedicated virtual machine host to place the instance on. Supported only if this VM instance was already placed on a dedicated virtual machine host - that is, you can't move an instance from on-demand capacity to dedicated capacity, nor can you move an instance from dedicated capacity to on-demand capacity.

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_T Type

The location for where an instance pool will place instances.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to place instances. Example: `Uocm:PHX-AD-1`

`fault_domains`

(optional) The fault domains to place instances. If you don't provide any values, the system makes a best effort to distribute instances across all fault domains based on capacity. To distribute the instances evenly across selected fault domains, provide a set of fault domains. For example, you might want instances to be evenly distributed if your applications require high availability. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`

`primary_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary subnet in which to place instances. This field is deprecated. Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.

`primary_vnic_subnets`

(optional)

`secondary_vnic_subnets`

(optional) The set of secondary VNIC data for instances in the pool.

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_update_instance_pool_placement_configuration_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_DETAILS_T Type

The data to update an instance pool.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`instance_configuration_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance configuration associated with the instance pool.

`placement_configurations`

(optional) The placement configurations for the instance pool. Provide one placement configuration for each availability domain. To use the instance pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

`l_size`

(optional) The number of instances that should be in the instance pool. To determine whether capacity is available for a specific shape before you resize an instance pool, use the`CREATE_COMPUTE_CAPACITY_REPORT`Function operation.

`instance_display_name_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance displaynames follow the format. The formatter does not retroactively change instance's displaynames, only instance displaynames in the future follow the format

`instance_hostname_formatter`

(optional) A user-friendly formatter for the instance pool's instances. Instance hostnames follow the format. The formatter does not retroactively change instance's hostnames, only instance hostnames in the future follow the format

### DBMS_CLOUD_OCI_CORE_UPDATE_INTERNET_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_enabled`

(optional) Whether the gateway is enabled.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the Internet Gateway is using.

### DBMS_CLOUD_OCI_CORE_UPDATE_IPV6_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to reassign the IPv6 to. The VNIC must be in the same subnet as the current VNIC.

### DBMS_CLOUD_OCI_CORE_UPDATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the LPG will use. For information about why you would associate a route table with an LPG, see[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

### DBMS_CLOUD_OCI_CORE_UPDATE_NAT_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`block_traffic`

(optional) Whether the NAT gateway blocks traffic through it. The default is `false`. Example: `true`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table used by the NAT gateway. If you don't specify a route table here, the NAT gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the NAT gateway.

### DBMS_CLOUD_OCI_CORE_UPDATE_NETWORK_SECURITY_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_RULE_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_core_update_security_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules to update.

### DBMS_CLOUD_OCI_CORE_UPDATE_PRIVATE_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`hostname_label`

(optional) The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `bminstance1`

`vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC to reassign the private IP to. The VNIC must be in the same subnet as the current VNIC.

### DBMS_CLOUD_OCI_CORE_UPDATE_PUBLIC_IP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`private_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP to assign the public IP to. * If the public IP is already assigned to a different private IP, it will be unassigned and then reassigned to the specified private IP. * If you set this field to an empty string, the public IP will be unassigned from the private IP it is currently assigned to.

### DBMS_CLOUD_OCI_CORE_UPDATE_PUBLIC_IP_POOL_DETAILS_T Type

The data to update for a public IP pool.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_ROUTE_TABLE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_rules`

(optional) The collection of rules used for routing destination IPs to network devices.

### DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_LIST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`egress_security_rules`

(optional) Rules for allowing egress IP packets.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`ingress_security_rules`

(optional) Rules for allowing ingress IP packets.

### DBMS_CLOUD_OCI_CORE_UPDATE_SERVICE_GATEWAY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`block_traffic`

(optional) Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules. Example: `true`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the service gateway will use. For information about why you would associate a route table with a service gateway, see[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

`services`

(optional) List of all the `Service` objects you want enabled on this service gateway. Sending an empty list means you want to disable all services. Omitting this parameter entirely keeps the existing list of services intact. You can also enable or disable a particular `Service` by using`ATTACH_SERVICE_ID`Function or`DETACH_SERVICE_ID`Function. For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See`ROUTE_TABLE`Type.

### DBMS_CLOUD_OCI_CORE_UPDATE_SUBNET_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`dhcp_options_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the set of DHCP options the subnet will use.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the subnet will use.

`security_list_ids`

(optional) The OCIDs of the security list or lists the subnet will use. This replaces the entire current set of security lists. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`cidr_block`

(optional) The CIDR block of the subnet. The new CIDR block must meet the following criteria: - Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range. **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress. Example: `172.16.0.0/16`

`ipv6_cidr_block`

(optional) This is the IPv6 prefix for the subnet's IP address space. The subnet size is always /64. See[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm). The provided prefix must maintain the following rules - a. The IPv6 prefix is valid and correctly formatted. b. The IPv6 prefix is within the parent VCN IPv6 range. Example: `2001:0db8:0123:1111::/64`

`ipv6_cidr_blocks`

(optional) The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefix, BYOIPv6 prefixes) for the subnet that meets the following criteria: - The prefixes must be valid. - Multiple prefixes must not overlap each other or the on-premises network prefix. - The number of prefixes must not exceed the limit of IPv6 prefixes allowed to a subnet.

### DBMS_CLOUD_OCI_CORE_UPDATE_TUNNEL_CPE_DEVICE_CONFIG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`tunnel_cpe_device_config`

(optional) The set of configuration answers for a CPE device.

### DBMS_CLOUD_OCI_CORE_UPDATE_VCN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_VIRTUAL_CIRCUIT_DETAILS_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_UPDATE_VLAN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to use with this VLAN. All VNICs in the VLAN will belong to these NSGs. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the VLAN will use.

`cidr_block`

(optional) The CIDR block of the VLAN. The new CIDR block must meet the following criteria: - Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range. **Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.

### DBMS_CLOUD_OCI_CORE_UPDATE_VNIC_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as an empty array removes the VNIC from all network security groups. If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the VNIC belongs to the NSGs that are associated with the VLAN itself. See`VLAN`Type. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip). If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `skipSourceDestCheck` attribute is ignored. This is because the source/destination check is always disabled for VNICs in a VLAN. Example: `true`

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_ATTACHMENT_DETAILS_T Type

details for updating a volume attachment.

Syntax
```

```

Fields

Field Description

`iscsi_login_state`

(optional) The iscsi login state of the volume attachment. For a multipath volume attachment, all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.

Allowed values are: 'UNKNOWN', 'LOGGING_IN', 'LOGIN_SUCCEEDED', 'LOGIN_FAILED', 'LOGGING_OUT', 'LOGOUT_SUCCEEDED', 'LOGOUT_FAILED'

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_BACKUP_POLICY_DETAILS_T Type

Specifies the properties for updating a user defined backup policy. For more information about user defined backup policies, see[User Defined Policies](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies)in[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`destination_region`

(optional) The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`. Specify `none` to reset the `destinationRegion` parameter. See[Region Pairs](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs)for details about paired regions.

`schedules`

(optional) The collection of schedules for the volume backup policy. See see[Schedules](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules)in[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for more information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `0`: Represents Lower Cost option. * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

`size_in_g_bs`

(optional) The size to resize the volume to in GBs. Has to be larger than the current size.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`block_volume_replicas`

(optional) The list of block volume replicas that this volume will be updated to have in the specified destination availability domains.

`autotune_policies`

(optional) The list of autotune policies enabled for this volume.

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_GROUP_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`volume_ids`

(optional) OCIDs for the volumes in this volume group.

`volume_group_replicas`

(optional) The list of volume group replicas that this volume group will be updated to have in the specified destination availability domains.

### DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_KMS_KEY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the new Vault service key to assign to protect the specified volume. This key has to be a valid Vault service key, and policies must exist to allow the user and the Block Volume service to access this key. If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.

### DBMS_CLOUD_OCI_CORE_UPDATE_VTAP_DETAILS_T Type

These details can be included in a request to update a virtual test access point (VTAP).

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_UPDATED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type

Syntax
```

```

Fields

Field Description

`security_rules`

(optional) The NSG security rules that were updated.

### DBMS_CLOUD_OCI_CORE_UPGRADE_STATUS_T Type

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

### DBMS_CLOUD_OCI_CORE_VCN_T Type

A virtual cloud network (VCN). For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`byoipv6_cidr_blocks`

(optional) The list of BYOIPv6 prefixes required to create a VCN that uses BYOIPv6 ranges.

`ipv6_private_cidr_blocks`

(optional) For an IPv6-enabled VCN, this is the list of Private IPv6 prefixes for the VCN's IP address space.

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`dns_label`

(optional) A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter. The value cannot be changed. The absence of this parameter means the Internet and VCN Resolver will not work for this VCN. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The VCN's Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).

`ipv6_cidr_blocks`

(optional) For an IPv6-enabled VCN, this is the list of IPv6 prefixes for the VCN's IP address space. The prefixes are provided by Oracle and the sizes are always /56.

`lifecycle_state`

(required) The VCN's current state.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING'

`time_created`

(optional) The date and time the VCN was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vcn_domain_name`

(optional) The VCN's domain name, which consists of the VCN's DNS label, and the `oraclevcn.com` domain. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `vcn1.oraclevcn.com`

### DBMS_CLOUD_OCI_CORE_VCN_DNS_RESOLVER_ASSOCIATION_T Type

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

### DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type

Specifies the VCN Attachment

Syntax
```

```

`dbms_cloud_oci_core_vcn_drg_attachment_network_create_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_create_details_t`type.

Fields

Field Description

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see[Advanced Scenario: Transit Routing](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm). For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

### DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies details within the VCN.

Syntax
```

```

`dbms_cloud_oci_core_vcn_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_details_t`type.

Fields

Field Description

`route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table the DRG attachment is using. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

Allowed values are: 'VCN_CIDRS', 'SUBNET_CIDRS'

### DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type

Specifies the update details for the VCN attachment.

Syntax
```

```

`dbms_cloud_oci_core_vcn_drg_attachment_network_update_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_update_details_t`type.

Fields

Field Description

`route_table_id`

(optional) This is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table that is used to route the traffic as it enters a VCN through this attachment. For information about why you would associate a route table with a DRG attachment, see: *[Transit Routing: Access to Multiple VCNs in Same Region](https://docs.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)*[Transit Routing: Private Access to Oracle Services](https://docs.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)

`vcn_route_type`

(optional) Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment. Routes from the VCN ingress route table are always imported.

### DBMS_CLOUD_OCI_CORE_VCN_TOPOLOGY_T Type

Defines the representation of a virtual network topology for a VCN. See[Network Visualizer Documentation](https://docs.oracle.com/iaas/Content/Network/Concepts/network_visualizer.htm)for more information, including conventions and pictures of symbols.

Syntax
```

```

`dbms_cloud_oci_core_vcn_topology_t`is a subtype of the`dbms_cloud_oci_core_topology_t`type.

Fields

Field Description

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for which the topology is generated.

### DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNEL_DETAILS_T Type

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

### DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPE_T Type

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

### DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_DRG_ATTACHMENT_NETWORK_DETAILS_T Type

Specifies the virtual circuit attached to the DRG.

Syntax
```

```

`dbms_cloud_oci_core_virtual_circuit_drg_attachment_network_details_t`is a subtype of the`dbms_cloud_oci_core_drg_attachment_network_details_t`type.

Fields

Field Description

`transport_only_mode`

(optional) Boolean flag that determines wether all traffic over the virtual circuits is encrypted. Example: `true`

### DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_T Type

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

### DBMS_CLOUD_OCI_CORE_VLAN_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

### DBMS_CLOUD_OCI_CORE_VNIC_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

`ipv6_addresses`

(optional) List of IPv6 addresses assigned to the VNIC. Example: `2001:DB8::`

### DBMS_CLOUD_OCI_CORE_VNIC_ATTACHMENT_T Type

Represents an attachment between a VNIC and an instance. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the instance. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment the VNIC attachment is in, which is the same compartment the instance is in.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The OCID of the VNIC attachment.

`instance_id`

(required) The OCID of the instance.

`lifecycle_state`

(required) The current state of the VNIC attachment.

Allowed values are: 'ATTACHING', 'ATTACHED', 'DETACHING', 'DETACHED'

`nic_index`

(optional) Which physical network interface card (NIC) the VNIC uses. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`subnet_id`

(optional) The OCID of the subnet to create the VNIC in.

`vlan_id`

(optional) The OCID of the VLAN to create the VNIC in. Creating the VNIC in a VLAN (instead of a subnet) is possible only if you are an Oracle Cloud VMware Solution customer. See`VLAN`Type. An error is returned if the instance already has a VNIC attached to it from this VLAN.

`time_created`

(required) The date and time the VNIC attachment was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`vlan_tag`

(optional) The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process is complete. However, if the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution, the `vlanTag` value is instead the value of the `vlanTag` attribute for the VLAN. See`VLAN`Type. Example: `0`

`vnic_id`

(optional) The OCID of the VNIC. Available after the attachment process is complete.

### DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_INFO_TBL Type

Nested table type of dbms_cloud_oci_core_block_volume_replica_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_VOLUME_T Type

A detachable block volume device that allows you to dynamically expand the storage capacity of an instance. For more information, see[Overview of Cloud Volume Storage](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the volume. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The OCID of the compartment that contains the volume.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`id`

(required) The OCID of the volume.

`is_hydrated`

(optional) Specifies whether the cloned volume's data has finished copying from the source volume or backup.

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume.

`lifecycle_state`

(required) The current state of a volume.

Allowed values are: 'PROVISIONING', 'RESTORING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY'

`vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `0`: Represents Lower Cost option. * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For performance autotune enabled volumes, It would be the Default(Minimum) VPUs/GB.

`size_in_g_bs`

(optional) The size of the volume in GBs.

`size_in_m_bs`

(required) The size of the volume in MBs. This field is deprecated. Use sizeInGBs instead.

`source_details`

(optional)

`time_created`

(required) The date and time the volume was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`volume_group_id`

(optional) The OCID of the source volume group.

`is_auto_tune_enabled`

(optional) Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.

`auto_tuned_vpus_per_gb`

(optional) The number of Volume Performance Units per GB that this volume is effectively tuned to.

`block_volume_replicas`

(optional) The list of block volume replicas of this volume.

`autotune_policies`

(optional) The list of autotune policies enabled for this volume.

### DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_T Type

A point-in-time copy of a volume that can then be used to create a new block volume or recover a block volume. For more information, see[Overview of Cloud Volume Storage](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the volume backup.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`expiration_time`

(optional) The date and time the volume backup will expire and be automatically deleted. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). This parameter will always be present for backups that were created automatically by a scheduled-backup policy. For manually created backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the volume backup.

`kms_key_id`

(optional) The OCID of the Vault service key which is the master encryption key for the volume backup. For more information about the Vault service and encryption keys, see[Overview of Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Using Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

`lifecycle_state`

(required) The current state of a volume backup.

Allowed values are: 'CREATING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY', 'REQUEST_RECEIVED'

`size_in_g_bs`

(optional) The size of the volume, in GBs.

`size_in_m_bs`

(optional) The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Please use sizeInGBs.

`source_type`

(optional) Specifies whether the backup was created manually, or via scheduled backup policy.

Allowed values are: 'MANUAL', 'SCHEDULED'

`source_volume_backup_id`

(optional) The OCID of the source volume backup.

`time_created`

(required) The date and time the volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_request_received`

(optional) The date and time the request to create the volume backup was received. Format defined by [RFC3339]https://tools.ietf.org/html/rfc3339.

`l_type`

(required) The type of a volume backup.

Allowed values are: 'FULL', 'INCREMENTAL'

`unique_size_in_g_bs`

(optional) The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space consumed on the volume and whether the backup is full or incremental.

`unique_size_in_mbs`

(optional) The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space consumed on the volume and whether the backup is full or incremental. This field is deprecated. Please use uniqueSizeInGBs.

`volume_id`

(optional) The OCID of the volume.

### DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_POLICY_T Type

A policy for automatically creating volume backups according to a recurring schedule. Has a set of one or more schedules that control when and how backups are created. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The OCID of the volume backup policy.

`schedules`

(required) The collection of schedules that this policy will apply.

`destination_region`

(optional) The paired destination region for copying scheduled backups to. Example `us-ashburn-1`. See[Region Pairs](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs)for details about paired regions.

`time_created`

(required) The date and time the volume backup policy was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`compartment_id`

(optional) The OCID of the compartment that contains the volume backup.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_POLICY_ASSIGNMENT_T Type

Specifies the volume that the volume backup policy is assigned to. For more information about Oracle defined backup policies and custom backup policies, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Fields

Field Description

`asset_id`

(required) The OCID of the volume the policy has been assigned to.

`id`

(required) The OCID of the volume backup policy assignment.

`policy_id`

(required) The OCID of the volume backup policy that has been assigned to the volume.

`time_created`

(required) The date and time the volume backup policy was assigned to the volume. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_INFO_T Type

Information about the volume group replica in the destination availability domain.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`volume_group_replica_id`

(required) The volume group replica's Oracle ID (OCID).

`availability_domain`

(required) The availability domain of the boot volume replica replica. Example: `Uocm:PHX-AD-1`

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_INFO_TBL Type

Nested table type of dbms_cloud_oci_core_volume_group_replica_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_T Type

Specifies a volume group which is a collection of volumes. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the volume group.

`compartment_id`

(required) The OCID of the compartment that contains the volume group.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID for the volume group.

`lifecycle_state`

(required) The current state of a volume group.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY', 'UPDATE_PENDING'

`size_in_m_bs`

(required) The aggregate size of the volume group in MBs.

`size_in_g_bs`

(optional) The aggregate size of the volume group in GBs.

`source_details`

(optional)

`time_created`

(required) The date and time the volume group was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`volume_ids`

(required) OCIDs for the volumes in this volume group.

`is_hydrated`

(optional) Specifies whether the newly created cloned volume group's data has finished copying from the source volume group or backup.

`volume_group_replicas`

(optional) The list of volume group replicas of this volume group.

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_BACKUP_T Type

A point-in-time copy of a volume group that can then be used to create a new volume group or restore a volume group. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the volume group backup.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`expiration_time`

(optional) The date and time the volume group backup will expire and be automatically deleted. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). This parameter will always be present for volume group backups that were created automatically by a scheduled-backup policy. For manually created volume group backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the volume group backup.

`lifecycle_state`

(required) The current state of a volume group backup.

Allowed values are: 'CREATING', 'COMMITTED', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAULTY', 'REQUEST_RECEIVED'

`size_in_m_bs`

(optional) The aggregate size of the volume group backup, in MBs.

`size_in_g_bs`

(optional) The aggregate size of the volume group backup, in GBs.

`source_type`

(optional) Specifies whether the volume group backup was created manually, or via scheduled backup policy.

Allowed values are: 'MANUAL', 'SCHEDULED'

`time_created`

(required) The date and time the volume group backup was created. This is the time the actual point-in-time image of the volume group data was taken. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_request_received`

(optional) The date and time the request to create the volume group backup was received. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`l_type`

(required) The type of backup.

Allowed values are: 'FULL', 'INCREMENTAL'

`unique_size_in_mbs`

(optional) The aggregate size used by the volume group backup, in MBs. It is typically smaller than sizeInMBs, depending on the spaceconsumed on the volume group and whether the volume backup is full or incremental.

`unique_size_in_gbs`

(optional) The aggregate size used by the volume group backup, in GBs. It is typically smaller than sizeInGBs, depending on the spaceconsumed on the volume group and whether the volume backup is full or incremental.

`volume_backup_ids`

(required) OCIDs for the volume backups in this volume group backup.

`volume_group_id`

(optional) The OCID of the source volume group.

`source_volume_group_backup_id`

(optional) The OCID of the source volume group backup.

### DBMS_CLOUD_OCI_CORE_MEMBER_REPLICA_TBL Type

Nested table type of dbms_cloud_oci_core_member_replica_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_T Type

An asynchronous replica of a volume group that can then be used to create a new volume group or recover a volume group. For more information, see[Volume Group Replication](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroupreplication.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain of the volume group replica.

`compartment_id`

(required) The OCID of the compartment that contains the volume group replica.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID for the volume group replica.

`lifecycle_state`

(required) The current state of a volume group.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ACTIVATING', 'TERMINATING', 'TERMINATED', 'FAULTY'

`size_in_g_bs`

(required) The aggregate size of the volume group replica in GBs.

`volume_group_id`

(required) The OCID of the source volume group.

`time_created`

(required) The date and time the volume group replica was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`member_replicas`

(required) Volume replicas within this volume group replica.

`time_last_synced`

(required) The date and time the volume group replica was last synced from the source volume group. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_BACKUP_DETAILS_T Type

Specifies the volume group backup to restore from.

Syntax
```

```

`dbms_cloud_oci_core_volume_group_source_from_volume_group_backup_details_t`is a subtype of the`dbms_cloud_oci_core_volume_group_source_details_t`type.

Fields

Field Description

`volume_group_backup_id`

(required) The OCID of the volume group backup to restore from.

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_DETAILS_T Type

Specifies the volume group to clone from.

Syntax
```

```

`dbms_cloud_oci_core_volume_group_source_from_volume_group_details_t`is a subtype of the`dbms_cloud_oci_core_volume_group_source_details_t`type.

Fields

Field Description

`volume_group_id`

(required) The OCID of the volume group to clone from.

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_REPLICA_DETAILS_T Type

Specifies the source volume replica which the volume group will be created from. The volume group replica shoulbe be in the same availability domain as the volume group. Only one volume group can be created from a volume group replica at the same time.

Syntax
```

```

`dbms_cloud_oci_core_volume_group_source_from_volume_group_replica_details_t`is a subtype of the`dbms_cloud_oci_core_volume_group_source_details_t`type.

Fields

Field Description

`volume_group_replica_id`

(required) The OCID of the volume group replica.

### DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUMES_DETAILS_T Type

Specifies the volumes in a volume group.

Syntax
```

```

`dbms_cloud_oci_core_volume_group_source_from_volumes_details_t`is a subtype of the`dbms_cloud_oci_core_volume_group_source_details_t`type.

Fields

Field Description

`volume_ids`

(required) OCIDs for the volumes in this volume group.

### DBMS_CLOUD_OCI_CORE_VOLUME_KMS_KEY_T Type

The Vault service master encryption key associated with this volume.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the Vault service key assigned to this volume. If the volume is not using Vault service, then the `kmsKeyId` will be a null string.

### DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_BLOCK_VOLUME_REPLICA_DETAILS_T Type

Specifies the source block volume replica which the block volume will be created from. The block volume replica shoulbe be in the same availability domain as the block volume. Only one volume can be created from a replica at the same time.

Syntax
```

```

`dbms_cloud_oci_core_volume_source_from_block_volume_replica_details_t`is a subtype of the`dbms_cloud_oci_core_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the block volume replica.

### DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_VOLUME_BACKUP_DETAILS_T Type

Specifies the volume backup.

Syntax
```

```

`dbms_cloud_oci_core_volume_source_from_volume_backup_details_t`is a subtype of the`dbms_cloud_oci_core_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the volume backup.

### DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_VOLUME_DETAILS_T Type

Specifies the source volume.

Syntax
```

```

`dbms_cloud_oci_core_volume_source_from_volume_details_t`is a subtype of the`dbms_cloud_oci_core_volume_source_details_t`type.

Fields

Field Description

`id`

(required) The OCID of the volume.

### DBMS_CLOUD_OCI_CORE_VTAP_T Type

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

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

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

- [Core Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7BFB0CCC-B4A4-406C-AACC-0C6A5166CEE2)
- [DBMS_CLOUD_OCI_CORE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-37D14062-DA48-49B2-8BC1-65D65765CE86)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AE9777E4-831C-42EC-9DC2-5F7C2F6E23B3)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-68FC3ACC-5C8A-403C-A15A-56CB40C6C472)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B210554D-FBAB-4B22-997C-60BFAC1397C1)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AABD8F5E-3EE7-4A47-91E8-835786BC54FE)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6C60CFA7-7E5B-40E8-8B2A-8F393A61CF84)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0F609F5E-2F91-4DE2-A4D5-661A7FDCBE36)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FCD9C352-7093-45F6-B17E-02B3FDCE58FD)
- [DBMS_CLOUD_OCI_CORE_ADD_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9210DD00-B452-4195-9BF3-FD42D1BDD483)
- [DBMS_CLOUD_OCI_CORE_IMAGE_MEMORY_CONSTRAINTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-32EA38EC-D023-452B-A7D0-B9476807B6F0)
- [DBMS_CLOUD_OCI_CORE_IMAGE_OCPU_CONSTRAINTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9D70D8DA-3998-49CD-878B-E88262494AC6)
- [DBMS_CLOUD_OCI_CORE_ADD_IMAGE_SHAPE_COMPATIBILITY_ENTRY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-75F6F5A1-D8AE-4963-ACB5-E55E5846C165)
- [DBMS_CLOUD_OCI_CORE_ICMP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-874B43F6-36CC-46D6-B91D-6C7FBF47D359)
- [DBMS_CLOUD_OCI_CORE_PORT_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3CEF4575-3BB0-46E8-AE4A-21EA0A1A4643)
- [DBMS_CLOUD_OCI_CORE_TCP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FFCA2000-087C-4FDE-843B-8CAFCD759348)
- [DBMS_CLOUD_OCI_CORE_UDP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-02FF7333-3F03-49B0-90C7-9E5D105EA92B)
- [DBMS_CLOUD_OCI_CORE_ADD_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3BFA047F-C10D-4C76-A4DD-B53F32589EDA)
- [DBMS_CLOUD_OCI_CORE_ADD_SECURITY_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5192E897-90D1-4F7D-B332-D0B48F6760A6)
- [DBMS_CLOUD_OCI_CORE_ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CF020F4E-C331-48C8-8CEF-63721936568D)
- [DBMS_CLOUD_OCI_CORE_ADD_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-07016749-64C8-4F5E-882A-E144A1926F9C)
- [DBMS_CLOUD_OCI_CORE_ADD_SUBNET_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E9A0C2A9-3FF5-4E3E-A121-347EB38E39F2)
- [DBMS_CLOUD_OCI_CORE_ADD_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90FC9240-CE11-4B7C-898A-90D750A711BF)
- [DBMS_CLOUD_OCI_CORE_BYOIPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5030071B-EE34-4E1E-B41E-8F1D73846818)
- [DBMS_CLOUD_OCI_CORE_ADD_VCN_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FEA26A1B-0775-476E-A756-6458AED970FA)
- [DBMS_CLOUD_OCI_CORE_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ABB89AE6-3A65-4F58-8C89-CD8DFC97EFC9)
- [DBMS_CLOUD_OCI_CORE_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3D26FFD8-08D1-4E81-AA43-FB84C8DF8232)
- [DBMS_CLOUD_OCI_CORE_ADDED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B5AD3D0B-047A-4D73-B3F4-B90B6122413C)
- [DBMS_CLOUD_OCI_CORE_ALLOWED_PHASE_ONE_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-14BD767D-5F5A-41B5-BB52-09F2E2E4EB43)
- [DBMS_CLOUD_OCI_CORE_ALLOWED_PHASE_TWO_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E86894EC-728C-4B11-B281-2B561890D4C0)
- [DBMS_CLOUD_OCI_CORE_DEFAULT_PHASE_ONE_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5561D4DE-4C80-4031-A178-1119B5E44247)
- [DBMS_CLOUD_OCI_CORE_DEFAULT_PHASE_TWO_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A15A6EB7-A5C3-409E-A4CD-301AA8941AED)
- [DBMS_CLOUD_OCI_CORE_ALLOWED_IKE_IP_SEC_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7BD54BAC-64B4-450D-B99E-C0D43D7C4810)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2D0B3671-43F7-43F5-9CE3-8C735BEFE9AD)
- [DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-823A6982-847B-4373-BF99-8E87999979DB)
- [DBMS_CLOUD_OCI_CORE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-52DC53FA-5AB8-459E-888F-350654DF2D69)
- [DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_GPU_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-78515251-8F44-4C6D-A028-981FBD1F8B21)
- [DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A9810907-E913-4261-AB9C-997345751951)
- [DBMS_CLOUD_OCI_CORE_AMD_MILAN_BM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-98792CD0-35F8-4ED4-8778-DE05B5429140)
- [DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3AFC2D8B-B93C-45B9-A72F-DEC5D2334CBC)
- [DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_GPU_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A674B98F-29EA-4D80-8B39-D0FCACEFE178)
- [DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CF20A559-6E89-44CC-8E0F-7228D6A2F7BC)
- [DBMS_CLOUD_OCI_CORE_AMD_ROME_BM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-932C31D8-A92A-4812-99C3-229810FFC7E0)
- [DBMS_CLOUD_OCI_CORE_AMD_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-45D2F98D-4F3C-4C9F-A8A1-5B2E8FF2C571)
- [DBMS_CLOUD_OCI_CORE_AMD_VM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7E8BEB8E-E3AA-4329-8E47-F6A5D660818F)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6013DDCB-DE4F-4C1C-A525-78315E0F468C)
- [DBMS_CLOUD_OCI_CORE_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F44C7912-6213-4E97-AC22-85463BBD072C)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3D6C6A05-5A07-4802-8441-B0D0E6D24DA5)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_AGREEMENTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CA197C90-7B02-4C6A-AF94-98A29F91CD63)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_RESOURCE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-798E4E05-E08A-41F6-B4EE-0C8289DD2823)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_LISTING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8AA1E426-AFEE-451E-A62D-64E76933FCD8)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AAC0D77E-0741-40DA-BA7A-EA10D5E11EB0)
- [DBMS_CLOUD_OCI_CORE_APP_CATALOG_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-514F7876-CBCC-4610-BEAF-8E3783FBB4FE)
- [DBMS_CLOUD_OCI_CORE_ATTACH_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-808337DC-AB36-4C20-99D8-4EF9C818B5E4)
- [DBMS_CLOUD_OCI_CORE_ATTACH_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-437A3F83-BE20-4CED-BBF0-7470F7AC6C2D)
- [DBMS_CLOUD_OCI_CORE_ATTACH_EMULATED_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-11992C22-BDCB-4680-B7A9-EA4C4B5B65C8)
- [DBMS_CLOUD_OCI_CORE_ATTACH_I_SCSI_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-24A0DB2B-772A-4D4B-B27A-718BC8976D46)
- [DBMS_CLOUD_OCI_CORE_ATTACH_INSTANCE_POOL_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C8672ABC-ED5C-4218-9D3A-5AE517D98381)
- [DBMS_CLOUD_OCI_CORE_ATTACH_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D306BD80-CD59-4D75-ADA7-AF534EEAFB1F)
- [DBMS_CLOUD_OCI_CORE_ATTACH_PARAVIRTUALIZED_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B0B62F66-7604-4416-81F2-B6AE3BC0DF45)
- [DBMS_CLOUD_OCI_CORE_ATTACH_SERVICE_DETERMINED_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-18846332-08DE-4383-9E22-15AE293A651B)
- [DBMS_CLOUD_OCI_CORE_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-63A3E9B7-345F-4E90-9BE7-D09F30494C10)
- [DBMS_CLOUD_OCI_CORE_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0C3A4FCC-05EB-4A94-A794-648332422487)
- [DBMS_CLOUD_OCI_CORE_CREATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D748BDAB-8C19-4257-840E-BF8801757CC8)
- [DBMS_CLOUD_OCI_CORE_ATTACH_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EB41914C-5978-4D6D-AE6C-80412AB3BD95)
- [DBMS_CLOUD_OCI_CORE_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7AE64F81-8C8F-483F-BBC7-0406B929CBE2)
- [DBMS_CLOUD_OCI_CORE_BGP_SESSION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5136C7DE-FB24-4682-A083-8D440276D769)
- [DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7E61216E-3D56-4EC9-B901-CC12E86823CB)
- [DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ABD17B77-BA82-4A47-B595-50D1724E0BD0)
- [DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AACBC83C-3855-48CA-A004-AD9D2AC2CAAA)
- [DBMS_CLOUD_OCI_CORE_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-38A15D36-B157-4FF2-A035-EFE6370736D9)
- [DBMS_CLOUD_OCI_CORE_BOOLEAN_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C0FC3127-6FF1-4D27-97B0-3CC6064FE9C2)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BFB68C5A-4934-4D37-86D9-857AB83627E0)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1431C08D-C8EE-46FE-A087-BF5EDBB123CF)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FA7BC9B0-83C9-452F-A381-CE69D3DC614F)
- [DBMS_CLOUD_OCI_CORE_AUTOTUNE_POLICY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EAF122FF-406E-4CDC-A31A-839459B356C2)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7F1DA782-CF78-4A58-A620-F060BB5C1929)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1F493DCD-89FF-405F-BB00-23A3F28A1136)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1DD0C67F-EAA4-463B-87E3-EB77DD724838)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_KMS_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-31399FFE-B3DA-4656-A1C6-1BF4845CA6CA)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E99B4F0F-B182-40E8-8C8D-B6148A586B30)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-93D20C85-03B4-4F63-A9F1-38267F7DBD11)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8396E23D-E7D6-403F-9507-CE5918F36D7F)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FB95125D-66D1-4FBF-85DC-67560598D218)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_SOURCE_FROM_BOOT_VOLUME_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9DC893A5-B382-4FAB-9857-987968A3113D)
- [DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-16218534-9034-4EA3-8E31-817F1D8C4260)
- [DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B539B823-2C7B-47EB-8B3E-3B8345259508)
- [DBMS_CLOUD_OCI_CORE_BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5BE724A2-0B1B-4B02-921A-04BBBDD943F0)
- [DBMS_CLOUD_OCI_CORE_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2D3D33D5-9642-4805-8CE0-B9ABFF6E106A)
- [DBMS_CLOUD_OCI_CORE_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-805332B6-2ED1-40C8-B7A4-4CC584A840EC)
- [DBMS_CLOUD_OCI_CORE_BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9CBD899F-7283-4756-8B6F-C819FB206D0D)
- [DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A892110D-2920-420F-99C3-3A22A71E7BB8)
- [DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B2497BE8-AED6-4197-BBE0-71044D2F05D8)
- [DBMS_CLOUD_OCI_CORE_BYOIP_ALLOCATED_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-77F05D3C-8641-443E-875A-2595272ADB43)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EA076763-DF52-4CFA-AAE7-99CEEB8E9F05)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_VCN_IPV6_ALLOCATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6576BD3F-2819-42B3-8F09-F3DA387DD3D3)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3259999E-2A3C-4962-9E5F-8F72C0968CC3)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-25BA0F20-3FCD-470C-A3AC-4047E482B836)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F03E76C2-F278-4118-9287-A99BF9B8B1B1)
- [DBMS_CLOUD_OCI_CORE_BYOIP_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-18144367-C90D-4643-BBDB-63428E97A905)
- [DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_INSTANCE_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E450269C-A42D-451C-A157-63A8B415FAF2)
- [DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_SHAPE_AVAILABILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FF57894E-26EB-4EBC-B62D-74314FBAA021)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-127C3BA8-5CF1-412A-896C-26C73D8011F4)
- [DBMS_CLOUD_OCI_CORE_CAPACITY_RESERVATION_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4930BC26-EDAB-436E-AE90-B813803BF089)
- [DBMS_CLOUD_OCI_CORE_CAPACITY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-212E2D33-D477-41FB-8842-503005596039)
- [DBMS_CLOUD_OCI_CORE_CAPTURE_CONSOLE_HISTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A12B94A8-8002-44D8-981A-4938A887BB67)
- [DBMS_CLOUD_OCI_CORE_VTAP_CAPTURE_FILTER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-774F0F2C-8056-4B9B-A2A0-89486BAD201C)
- [DBMS_CLOUD_OCI_CORE_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6F2C1041-7D05-4FFA-9BD5-14EE35869FDC)
- [DBMS_CLOUD_OCI_CORE_VTAP_CAPTURE_FILTER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A3ECE187-3ED1-4029-A92D-98CF44CDB8D2)
- [DBMS_CLOUD_OCI_CORE_FLOW_LOG_CAPTURE_FILTER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C11851C2-2833-41B3-84F0-57344DFB85AD)
- [DBMS_CLOUD_OCI_CORE_CAPTURE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-26BC2737-7F28-4AE7-85AF-A0D5335DDD3A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_BOOT_VOLUME_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B5628D09-D374-4E7C-9C4B-26A40101DECF)
- [DBMS_CLOUD_OCI_CORE_CHANGE_BOOT_VOLUME_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-94DB3FB3-83B1-4F7C-97BA-D70785D2D55C)
- [DBMS_CLOUD_OCI_CORE_CHANGE_BYOIP_RANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2DABB279-C526-469F-8C9D-369395DE5F3E)
- [DBMS_CLOUD_OCI_CORE_CHANGE_CAPTURE_FILTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E71DA29E-0CC4-497D-BB4A-6611C4B27186)
- [DBMS_CLOUD_OCI_CORE_CHANGE_CLUSTER_NETWORK_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9C6BE33D-9B2D-4A78-B088-2632E51DB135)
- [DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CAPACITY_RESERVATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-13B810A0-1896-42B0-BEB8-C03FDDCD7807)
- [DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CAPACITY_TOPOLOGY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0B9F38D5-2557-40D9-921D-4EC40544CF09)
- [DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-72F92036-293A-4813-833B-88DA4C85600B)
- [DBMS_CLOUD_OCI_CORE_CHANGE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-251D75B7-9F8A-4996-8AB9-065A79B70507)
- [DBMS_CLOUD_OCI_CORE_CHANGE_CPE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AD4C9A32-2F90-478F-ACCE-A628E5A05AAB)
- [DBMS_CLOUD_OCI_CORE_CHANGE_CROSS_CONNECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-79C77AF5-E5AD-40BF-BED2-627D1C5C6944)
- [DBMS_CLOUD_OCI_CORE_CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A643907D-E178-40AE-88F1-236A2C6CE1EB)
- [DBMS_CLOUD_OCI_CORE_CHANGE_DEDICATED_VM_HOST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6A4D6F07-2BE8-474A-A78B-82940127102E)
- [DBMS_CLOUD_OCI_CORE_CHANGE_DHCP_OPTIONS_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-59F26F96-8EFF-4505-83DA-66AFBA4B5901)
- [DBMS_CLOUD_OCI_CORE_CHANGE_DRG_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C8391520-22A5-4C1C-97D2-C3D767570A24)
- [DBMS_CLOUD_OCI_CORE_CHANGE_IP_SEC_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4CC9080D-E3C3-49F6-A7A5-D4BB8252558C)
- [DBMS_CLOUD_OCI_CORE_CHANGE_IMAGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9BAAF42A-7493-43F1-9D21-5F0B34257922)
- [DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FD777607-8BB6-4282-B5A7-3BC54C462846)
- [DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_CONFIGURATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D7E1F427-CCD2-4131-8FC4-D744F4909399)
- [DBMS_CLOUD_OCI_CORE_CHANGE_INSTANCE_POOL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F032FBD1-2B89-4E10-87D2-90F778D15E8E)
- [DBMS_CLOUD_OCI_CORE_CHANGE_INTERNET_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EFA6E47F-2CC4-44C6-A32A-F25F47D0109D)
- [DBMS_CLOUD_OCI_CORE_CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D51F3803-678C-4738-A7C6-81B3E7DC373A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_NAT_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BBB4C9B2-E891-4625-B507-4DC50FC073A5)
- [DBMS_CLOUD_OCI_CORE_CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8534D02E-5456-4511-9FEE-F03D8790A56E)
- [DBMS_CLOUD_OCI_CORE_CHANGE_PUBLIC_IP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EB85F097-BE49-4CAD-A4E0-DB0373B85281)
- [DBMS_CLOUD_OCI_CORE_CHANGE_PUBLIC_IP_POOL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7BEB201C-C701-449D-B766-1D0B005D663E)
- [DBMS_CLOUD_OCI_CORE_CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A396A0D0-3C9C-49E3-B061-8AE8C6BE8B3A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_ROUTE_TABLE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0797A2C7-D46B-442E-A594-A396E395FA7A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_SECURITY_LIST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-72E400D3-CF0A-4154-9B15-AC62E4AB9117)
- [DBMS_CLOUD_OCI_CORE_CHANGE_SERVICE_GATEWAY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E2601C9F-EEB4-47E9-B942-2839029E55A0)
- [DBMS_CLOUD_OCI_CORE_CHANGE_SUBNET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3A57E5DD-D0F1-4A70-AFAB-C47F257C195A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VCN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-74F81C1B-6F69-4A75-9A95-C707BE35B8EE)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5BA77981-34D0-4AAA-B9EC-EDB9B83C1F97)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VLAN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ED409F10-5684-4D82-A989-289F8D4B46AE)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-078AD2E2-EAEB-4538-B0F7-441569FC5701)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C374282-898E-4B0E-9340-A4D68366F86A)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_GROUP_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1AC6FDCC-D3D5-4CC2-B388-25D02D3A5DB9)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VOLUME_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-34C4F4B5-2D59-4112-A51E-7D4576A84E8D)
- [DBMS_CLOUD_OCI_CORE_CHANGE_VTAP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E1D27C87-C02A-4AB7-9A2E-8C11B4AA1FC7)
- [DBMS_CLOUD_OCI_CORE_CLUSTER_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DC16F98C-64BC-43E4-9015-8A0D90C466D9)
- [DBMS_CLOUD_OCI_CORE_CLUSTER_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9FD43968-91D0-4559-8169-A18A9BAE3259)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_IPV6_ADDRESS_IPV6_SUBNET_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-637A5CC2-6C04-406E-B24E-14AB158B796B)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_IPV6_ADDRESS_IPV6_SUBNET_CIDR_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CA1C47A0-0784-47C4-B10B-E8C9B86B6FB2)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_PRIMARY_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F7B19087-89C3-44EC-9C8C-04F21EF3742F)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SECONDARY_VNIC_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-196DEA87-D5A6-475F-80FA-E4C0792F1277)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SECONDARY_VNIC_SUBNET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-82CE2989-1B56-4BE3-BD89-5973C027D6A1)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-947C0071-08E3-4762-987C-BB8B0824ACF6)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_LOAD_BALANCER_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C294A6D3-435D-49A0-A6AB-6CAF5850BD00)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-81AD4F83-4895-45DD-B2D2-C8E03CB4F27F)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_LOAD_BALANCER_ATTACHMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A0A6503C-F124-44C7-A0A7-A4D9B9E48276)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FA638C80-D79E-4A84-8AFE-3C3FDF8A1ADA)
- [DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_PLACEMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-249AC00F-062B-4F78-98DB-EDB68417D0E0)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EC49A928-2C05-4071-A47D-AA93AF3A73DD)
- [DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F00717AF-9570-40E2-B8AE-5023FC8D69B8)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B3AA117A-2BD6-45F9-85E6-7ADEB166008A)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0EB227E7-0C73-4E4C-ADAD-874B025AE013)
- [DBMS_CLOUD_OCI_CORE_CLUSTER_NETWORK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-32DB59B0-FC28-4AFF-B97F-CD54FB402502)
- [DBMS_CLOUD_OCI_CORE_COMPARTMENT_INTERNAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5A306E24-C1F2-484D-9143-799C8EFFFC0E)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90A36A1E-B7ED-4FA1-B377-AB20324C2618)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6CA858F4-5130-41D6-8993-7A5DB1A85C19)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B4B8FBAF-CDB7-467D-9029-635BC44E960B)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_BARE_METAL_HOST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F85A7A84-E2D0-4B02-B131-50BC29B894CB)
- [DBMS_CLOUD_OCI_CORE_CAPACITY_REPORT_SHAPE_AVAILABILITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6DEF6409-CA1A-418D-9972-83F2629BA150)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-33FC8C86-704E-4216-A815-0317FF251C03)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8B54B69C-CD46-4EC1-B3E5-643F30423A6C)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A2B3E05F-E07A-4197-A94E-3F47378E4802)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3861B31D-CBA5-4DA8-8E27-0B775FE6D03D)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CC2B73C4-46A8-4831-86B0-45D5231F6A28)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_RESERVATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7D0BC85F-120A-4CEF-AA5D-B00ED076B8EF)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-68465F46-68B3-43DF-9832-4007F9173FD8)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3F5FD9C5-6819-4794-9771-C44C8C75B1BE)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4877C61D-1985-4BC7-9EEB-CD0E08B489F7)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CAPACITY_TOPOLOGY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-87AF2F05-F923-41E7-A060-0F3DA776D44A)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-282FDC6C-65BC-4ACD-9CCF-6FA1ED79F7D6)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A7427454-4098-4DDF-A3BB-FABFF4057860)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8360D989-A8C7-43E8-BDED-94FBC7E81693)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-276E6EEF-BB0D-49E2-94F4-F20ED35F62FE)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6EFA2326-BB0D-4B95-A87E-2B5C24B36BEE)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9B20D96B-9AC3-418D-8E91-C212F80B49D4)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9FA78115-5452-4AFD-96B9-FFAB8390A06C)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AF5F5F59-30A1-488F-986D-4206A6500133)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D188CDBC-DBB9-4A88-B0D8-0384957FC4B8)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-727661BF-6631-4FB4-9E43-52E05A88A12B)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-562C1CD5-A9C4-4435-9E63-B2E2123DACE0)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_HPC_ISLAND_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D90CBF1F-7EA2-428B-A340-4ABB613165CD)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-70D30976-AEB3-470C-A974-545521A104A7)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AABA20B2-7082-4328-AF99-B66162D4A3D0)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9E532A9D-5DC7-4A7E-BC28-E12A1D9BF095)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EC2FA593-F563-4920-A4BC-8B0E06C8B00A)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6D5D680D-1B47-4A74-8C89-8BBD8A08DB4D)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-276C7C1F-F407-4B6D-BAEB-64AD5A0C1B91)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_REPLICA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-13B1796F-0B93-4A33-8146-247481E70239)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AUTOTUNE_POLICY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EFFE56F0-D59E-4E9E-A01E-18A11429D547)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_CREATE_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3826257D-1CBA-4745-99EB-E88FBD93FFA1)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-780FE9B2-C391-4740-AD7E-64083A6C882B)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-25C080EE-84E4-4EDE-839F-FAEBCA3EF219)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_IPV6_ADDRESS_IPV6_SUBNET_CIDR_PAIR_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2295254F-7EA9-4685-B0C2-E7CAD615F649)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_CREATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D1FDD119-EA98-4377-A460-2A321F6504AD)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BB3FFB2B-B33D-4E73-AA99-F8C347163CCE)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-44F234FE-1960-4AB2-AC48-2EE7ADFFAC1D)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-350D33BE-EB2A-46A6-8BA4-4EF70ECC4718)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B0EDCB1F-634F-46C2-86B3-D750CCC820F2)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DE95778C-F238-4CEA-A36A-AED7526A1A5D)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FA5766EC-F19D-404B-972F-D082010C9E42)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E4F6A477-59F5-4193-B365-E3D75093803C)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A44B7D8A-13BC-452D-8E0C-2A932F992E9F)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AVAILABILITY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EDCE72F8-E4DF-4C10-B7BB-2A946C389F15)
- [DBMS_CLOUD_OCI_CORE_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E6B257BF-339A-41CF-BB79-49E89DB0DCBF)
- [DBMS_CLOUD_OCI_CORE_PREEMPTIBLE_INSTANCE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8162E37B-CA4E-42BB-95C1-0A14ADBDDFB8)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_LAUNCH_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D13BD80B-E2AA-4E3B-ABD2-44FEA4E7F201)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BEBDA02A-FAB0-44F3-A9E6-FEE23B14556A)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-25392445-4DFF-493E-AA9B-D9A31D994A96)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_BLOCK_VOLUME_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-51EF18D6-1CE9-4D4D-B0B6-0FE0F8272E71)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ATTACH_VNIC_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0736B0FD-7A6A-4B68-B2E8-9385DAD2CC05)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AD13E101-6374-47AE-8653-4C7861CC972A)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-633B2F27-2605-40FC-8E32-3335BADA1F52)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_INSTANCE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FB1FBAD6-9BB4-43F4-AFAC-2A93D3E9184B)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8602B874-603E-42E7-A6E4-79337774E44A)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EFAAA67B-631C-44DD-97D8-494749C771E8)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A31BCACC-FF1E-47CC-8F03-C6144A28F26E)
- [DBMS_CLOUD_OCI_CORE_COMPUTE_NETWORK_BLOCK_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9638B65A-3A09-4AA0-8E38-684D58F54249)
- [DBMS_CLOUD_OCI_CORE_CONNECT_LOCAL_PEERING_GATEWAYS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-06670346-F090-4FFE-94CA-D4C6AFED5923)
- [DBMS_CLOUD_OCI_CORE_CONNECT_REMOTE_PEERING_CONNECTIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F9BFF4ED-E768-427F-8412-2757AEE8A37D)
- [DBMS_CLOUD_OCI_CORE_CONSOLE_HISTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EC0268EA-ACBD-4CE8-AE0E-4F6C6D8B9EC2)
- [DBMS_CLOUD_OCI_CORE_COPY_BOOT_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-986FE0F0-A436-487E-92CF-58693185A073)
- [DBMS_CLOUD_OCI_CORE_COPY_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6CB377F6-BF5F-4D37-8F06-BE5DF8B0574A)
- [DBMS_CLOUD_OCI_CORE_COPY_VOLUME_GROUP_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C24E3FA8-2E0B-418B-85F3-34483D1479A6)
- [DBMS_CLOUD_OCI_CORE_CPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A7F4E061-1442-4A7C-A5B1-B4CD1FC022C4)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_ANSWER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EF2949D4-6B7D-4C0C-BB9D-0F7C029E5E3E)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_QUESTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CC15A872-BB3C-484A-A2AF-AEDFFDECC842)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CC177755-794B-4209-A33D-D260275AB257)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_QUESTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0AFA525F-98A0-4AD3-AF85-BACB9EFBF7D3)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_SHAPE_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-754B8315-2E9B-4BA5-A333-A55C2FCFD4F9)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C3D632B0-BFBC-4B6A-B080-DDB7D8AF85AA)
- [DBMS_CLOUD_OCI_CORE_CREATE_APP_CATALOG_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B0E7CEB2-7634-46CA-9C9A-9CEF36440B63)
- [DBMS_CLOUD_OCI_CORE_CREATE_BOOT_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B7AC9D27-0563-4D6D-9A92-DF986BFB5632)
- [DBMS_CLOUD_OCI_CORE_BOOT_VOLUME_REPLICA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-23542D16-8D38-420C-BEF4-9E3544DD40D6)
- [DBMS_CLOUD_OCI_CORE_CREATE_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4EC5AB46-F72F-43D7-8794-E2BF04570733)
- [DBMS_CLOUD_OCI_CORE_CREATE_BYOIP_RANGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ADACA870-68E0-47AE-B3D1-4093B7B5C94F)
- [DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_REPORT_SHAPE_AVAILABILITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-39C40267-F2D6-4BBA-BAF6-A1A789EED98E)
- [DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-89E8099E-48BF-4017-AEA4-31F2B0448CEF)
- [DBMS_CLOUD_OCI_CORE_CREATE_CAPTURE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CCF0BEB3-0575-4723-8738-005B66088761)
- [DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-96B848A7-6A5A-4349-83F2-D77CE420C2A6)
- [DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B262670B-957A-4566-AAE1-7626A5595D27)
- [DBMS_CLOUD_OCI_CORE_CREATE_CLUSTER_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BD92A43A-02DD-4B2C-98BC-7F31A87B6B7C)
- [DBMS_CLOUD_OCI_CORE_CREATE_CAPACITY_REPORT_SHAPE_AVAILABILITY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D773BDDE-566D-46B6-8363-98BBEA485A31)
- [DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_REPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-192A1B52-207B-4860-A47B-A66F6C4AF802)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DE77AB51-1B54-4639-B099-435B0CC9F00A)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_RESERVATION_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B84DA589-E9CA-4102-95B3-7F2B009793C4)
- [DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_RESERVATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CAD0F485-DA99-4605-AF5D-3E1D6263A301)
- [DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CAPACITY_TOPOLOGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EB242940-7363-403A-949D-3FDD89DDE5CE)
- [DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2946E6A3-E857-4CC6-AFB2-EEB6617EDA10)
- [DBMS_CLOUD_OCI_CORE_CREATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BBE3B035-43B5-4BCC-BC9F-28CA1D29591D)
- [DBMS_CLOUD_OCI_CORE_CREATE_CPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6AFB8F3C-8F17-4042-B043-3395DB3837FB)
- [DBMS_CLOUD_OCI_CORE_CREATE_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8D13EA01-E026-4685-B180-13FD52486AC2)
- [DBMS_CLOUD_OCI_CORE_CREATE_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D667FE95-A5C1-4357-9E41-918C5E2B4A92)
- [DBMS_CLOUD_OCI_CORE_CREATE_CROSS_CONNECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5403E334-B2DB-47D9-A3A0-F60D5F31D2D1)
- [DBMS_CLOUD_OCI_CORE_CREATE_CROSS_CONNECT_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B90595F7-7B17-423E-9192-C7A90A38F6C1)
- [DBMS_CLOUD_OCI_CORE_CREATE_DEDICATED_CAPACITY_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F633F20C-0C65-4A73-AD86-EFE011DF3E61)
- [DBMS_CLOUD_OCI_CORE_CREATE_DEDICATED_VM_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9275530B-1843-4AE1-8A7E-362D14127D32)
- [DBMS_CLOUD_OCI_CORE_DHCP_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AD775804-0EC5-4AFB-9D32-57E5F9D08D10)
- [DBMS_CLOUD_OCI_CORE_DHCP_OPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3E5DA5FA-139B-43A8-B208-CEC968246647)
- [DBMS_CLOUD_OCI_CORE_CREATE_DHCP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AAD6ED2C-7EB5-4BC6-BBC3-7B00E5AC9BE7)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-24469B55-E081-449B-A1BA-05E1D909239F)
- [DBMS_CLOUD_OCI_CORE_CREATE_DRG_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0BD9E3D1-0D6D-420B-9C14-7D6DB068DAC7)
- [DBMS_CLOUD_OCI_CORE_CREATE_DRG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3E560AAE-8431-41C4-B940-F955AC18690F)
- [DBMS_CLOUD_OCI_CORE_CREATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6695D7AE-EA86-469B-B0F3-7B0740D276C4)
- [DBMS_CLOUD_OCI_CORE_CREATE_DRG_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C31AD858-0000-4828-A201-1F864F016730)
- [DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-43A96EAD-B92A-4B2B-9E24-4BEAD84BCE13)
- [DBMS_CLOUD_OCI_CORE_PHASE_ONE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D2145E8E-5C2B-4131-BF67-A5067E3318FB)
- [DBMS_CLOUD_OCI_CORE_PHASE_TWO_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5F1B555D-FD18-4D5C-BAC0-752149F9ACF0)
- [DBMS_CLOUD_OCI_CORE_DPD_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CE473ACF-CC09-4201-A1F6-1EA587488B80)
- [DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8463D748-D27B-407B-BBE2-74BF7952739D)
- [DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-49099345-13F0-43A3-9E4E-4ECD689149B0)
- [DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DFF62008-62CB-4616-A3CE-17180FA8B84A)
- [DBMS_CLOUD_OCI_CORE_CREATE_IP_SEC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C44B8330-60F9-4945-B192-5E6E135B9CBA)
- [DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2B251142-0FF0-4108-872A-84656FA97457)
- [DBMS_CLOUD_OCI_CORE_CREATE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-432F228A-761A-4338-AB6E-1D0F42F28CF2)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-36291671-90F4-46C2-8FCB-7EE46F6785C5)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CCE8DDEE-E659-4940-AD74-F49C79912D91)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONFIGURATION_FROM_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1D4BE137-5E17-4373-BA1A-EB243CDFFC69)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_CONSOLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EF7B98C2-001E-4DC1-91DF-3FA517FDAACB)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2C77B7BB-E1BD-4B57-8A19-0B101F33A04E)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8420BF40-201A-4EDE-AE56-EC42725832CA)
- [DBMS_CLOUD_OCI_CORE_ATTACH_LOAD_BALANCER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-043E58D6-D6CE-43FC-87C2-878E983995B3)
- [DBMS_CLOUD_OCI_CORE_CREATE_INSTANCE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4B3D48ED-4F1D-480F-945B-CE659F98DDD4)
- [DBMS_CLOUD_OCI_CORE_CREATE_INTERNET_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1EEB9708-B8DF-4098-94F0-5CFE651C84B7)
- [DBMS_CLOUD_OCI_CORE_CREATE_IPV6_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-40BB9222-61C3-49F3-9AEE-002FD54E0BB6)
- [DBMS_CLOUD_OCI_CORE_CREATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-651159D4-4372-4E4F-8F2B-B179A2CE75FF)
- [DBMS_CLOUD_OCI_CORE_CREATE_NAT_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-667EACDA-0B49-4207-BEF6-7A3F58601680)
- [DBMS_CLOUD_OCI_CORE_CREATE_NETWORK_SECURITY_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1DB6AED5-F62E-4DCC-903A-8F22CD6A471B)
- [DBMS_CLOUD_OCI_CORE_CREATE_PRIVATE_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0AEFEE96-2C6B-4753-B46A-A07B5D7F2009)
- [DBMS_CLOUD_OCI_CORE_CREATE_PUBLIC_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-14A34ABF-29A1-4464-8CFF-F54AC7F5E69E)
- [DBMS_CLOUD_OCI_CORE_CREATE_PUBLIC_IP_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-45DF4773-9B4C-476C-A642-228B31017CE2)
- [DBMS_CLOUD_OCI_CORE_CREATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B67BF9E6-817C-49FC-BFA3-E05F66B3F1E4)
- [DBMS_CLOUD_OCI_CORE_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C7F54E04-CAA5-43E2-A69D-C3377BEA08D5)
- [DBMS_CLOUD_OCI_CORE_ROUTE_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0E1E7816-3B46-4A4D-9BA9-D1FFDEC396D8)
- [DBMS_CLOUD_OCI_CORE_CREATE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90B925DB-9F83-4E1C-A21A-69D3C95DBEE2)
- [DBMS_CLOUD_OCI_CORE_EGRESS_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A7A39C9B-27A1-40F0-B8AB-33D276A71616)
- [DBMS_CLOUD_OCI_CORE_INGRESS_SECURITY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5895583D-10BE-4DC2-8C73-0926323E54EA)
- [DBMS_CLOUD_OCI_CORE_EGRESS_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EC7C511C-4537-4A01-89E6-99D4590BB8CD)
- [DBMS_CLOUD_OCI_CORE_INGRESS_SECURITY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A1AF645B-6683-4BBB-B954-A51831385E50)
- [DBMS_CLOUD_OCI_CORE_CREATE_SECURITY_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8F1AE280-A680-4760-84E8-4D9103515C88)
- [DBMS_CLOUD_OCI_CORE_SERVICE_ID_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B913C7BF-1929-4032-906B-1D4276235259)
- [DBMS_CLOUD_OCI_CORE_SERVICE_ID_REQUEST_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F9CB76BA-0404-4E4A-8264-92181B2A4DA7)
- [DBMS_CLOUD_OCI_CORE_CREATE_SERVICE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-83A6045F-9AAD-4985-908F-EB3DF23558EF)
- [DBMS_CLOUD_OCI_CORE_CREATE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2FC7AE8D-C1E8-4331-B5B7-BD0B8D811167)
- [DBMS_CLOUD_OCI_CORE_BYOIPV6_CIDR_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-31B4C9F5-CF62-4E2B-BB89-49B59D00F77B)
- [DBMS_CLOUD_OCI_CORE_CREATE_VCN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A220AE6E-AD64-4222-885E-0AEE4377BE6C)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CE8E8443-A72E-4085-9958-C322A79A6E52)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BB1230D7-8ADA-42C7-A755-E8B72BDD31E0)
- [DBMS_CLOUD_OCI_CORE_CREATE_VIRTUAL_CIRCUIT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7EB5C96D-7003-47C4-B123-287E9121E924)
- [DBMS_CLOUD_OCI_CORE_CREATE_VLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C92BF3EE-B8B9-4C43-911B-014C907473E8)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6B2F68E7-16E3-480A-8C13-217272582505)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_POLICY_ASSIGNMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-387ACD3C-FE70-4FE1-94A3-CF4655FD5419)
- [DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E3B857C3-5A59-4C63-9C50-F1575579388D)
- [DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_SCHEDULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6A955AD1-DCC6-43FD-96B3-9D2A471FC2F2)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_BACKUP_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C7F0493-07C2-41E6-8F21-3A1B23751960)
- [DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FCED26FA-BA5C-4213-B4DC-127179ADDCE9)
- [DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-80533B1A-CDFB-4470-85B6-A611CFB7618C)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-07CAB193-3E22-4934-8950-4C6044AB14D7)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_GROUP_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3F2DB7A0-AEA9-4806-BA02-DC2C9AA772AF)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-37B6D83C-6C6B-419A-A1C5-132F28E51F15)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C6F6377-5722-4E37-9913-706057E65406)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B9E389E1-5B34-422F-AFAE-B5BE71C71C07)
- [DBMS_CLOUD_OCI_CORE_CREATE_VOLUME_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AD1B13B8-E545-4038-BB6D-B13D9A821BC4)
- [DBMS_CLOUD_OCI_CORE_CREATE_VTAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BCBBF9C5-E1D0-4F46-9C4F-76ED45153080)
- [DBMS_CLOUD_OCI_CORE_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-02558668-1851-480E-BFEB-4526928AFC06)
- [DBMS_CLOUD_OCI_CORE_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CA4B043D-20FA-4C68-A5C3-0636B9143250)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9DD076E4-4E25-45B8-97EC-A5CD60277661)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3B3C4152-041A-4AD5-A03A-A0036B1B2CF7)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-56505737-7B28-4887-82B9-A0F72F8AC0CD)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AB7B7A63-BA69-4029-A93C-CD00369BEC93)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-70B6BF19-CA6F-40B9-9640-E0548B2D7E32)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_MAPPING_DETAILS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B180A570-75C7-43A5-936E-78B5C416A12D)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_PORT_SPEED_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6D54CAAC-21B5-4671-84E6-9EB280FDB331)
- [DBMS_CLOUD_OCI_CORE_CROSS_CONNECT_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-805A8380-6E86-4476-8ED3-B0388DF881A5)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_CAPACITY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4218F098-DA83-4442-9894-C0EAA2507491)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4874DD05-989F-4274-849C-9714A8FBD86E)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_INSTANCE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-80F3B672-D6DC-4DE1-94E4-9FC8E4E39644)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EBA99215-9FBD-497B-A07C-BB676FC225D1)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-65B555E9-64AF-401F-82D4-351C44466D9E)
- [DBMS_CLOUD_OCI_CORE_DEDICATED_VM_HOST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F76D2C6F-93F1-4C8B-94A5-E9EDC07DF2E3)
- [DBMS_CLOUD_OCI_CORE_DEFAULT_DRG_ROUTE_TABLES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DCBCA86D-A943-49BC-84A9-03A615003FA3)
- [DBMS_CLOUD_OCI_CORE_DETACH_INSTANCE_POOL_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B14C05E3-770B-4D26-8C5C-07EE13EA0A2C)
- [DBMS_CLOUD_OCI_CORE_DETACH_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F37EA5DD-E556-45FA-9519-4EBA89813508)
- [DBMS_CLOUD_OCI_CORE_DETACHED_VOLUME_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3FD3050E-C331-4525-B6C0-1107859AEBE7)
- [DBMS_CLOUD_OCI_CORE_DEVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-98BFACD0-7F79-489B-B6B7-81F7CFDF19CA)
- [DBMS_CLOUD_OCI_CORE_DHCP_DNS_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-30331B6F-1C65-4B51-A028-B27D2C867954)
- [DBMS_CLOUD_OCI_CORE_DHCP_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C2672505-7A66-4E44-AB72-21B513D5C9DF)
- [DBMS_CLOUD_OCI_CORE_DHCP_SEARCH_DOMAIN_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-54FB2BEE-9CD9-4452-A5D6-D52163F9EF66)
- [DBMS_CLOUD_OCI_CORE_DRG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-317A41E8-9CE7-4A26-B7DF-EB80DF676DF8)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-25146383-5B94-41E0-BC11-582EB1956140)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CD61EBFD-C417-49E3-B23B-26FF51B5C065)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_ID_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B7DF67A9-E2F6-466D-BFF1-50BED1CA1E3D)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E964550E-4961-4150-83CB-CADE44161A2E)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_MATCH_ALL_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EF38BEDA-B607-4271-B82C-61BB87B673A2)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DB96EC96-850E-49B1-A527-98F4EDB3F75E)
- [DBMS_CLOUD_OCI_CORE_DRG_ATTACHMENT_TYPE_DRG_ROUTE_DISTRIBUTION_MATCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-28FF61F6-0195-440D-9296-EB624D0D63F8)
- [DBMS_CLOUD_OCI_CORE_DRG_REDUNDANCY_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-426736AB-8EC0-47C5-ABAD-A15974FBA56E)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-673C5F2C-EDE2-4340-8E02-17128021EDAF)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_DISTRIBUTION_STATEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C9780CF2-3B32-4E25-9F18-240167A95EF2)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4F9C1556-5D1A-4199-9076-73A88068032A)
- [DBMS_CLOUD_OCI_CORE_DRG_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BBC24299-CB3E-4A18-BB34-BCEFF19CA3F7)
- [DBMS_CLOUD_OCI_CORE_VOLUME_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B4ED8B8B-470F-453A-8F7A-B0705C3A4D59)
- [DBMS_CLOUD_OCI_CORE_EMULATED_VOLUME_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E5CE3722-2426-48D5-A9B4-18D183AA5DA6)
- [DBMS_CLOUD_OCI_CORE_ENCRYPTION_DOMAIN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-789EF2C5-AFC7-40F5-85E1-B9A2EC930B80)
- [DBMS_CLOUD_OCI_CORE_ENUM_INTEGER_IMAGE_CAPABILITY_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-85B02019-464D-4BE7-B072-457B34280161)
- [DBMS_CLOUD_OCI_CORE_ENUM_STRING_IMAGE_CAPABILITY_SCHEMA_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B642D301-8AB4-4AFF-861B-178D8F3AB85A)
- [DBMS_CLOUD_OCI_CORE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4F70B0B4-078A-44A4-9443-763CFBF5895D)
- [DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ED8BE5A0-5F1D-4CD2-9F0E-D16CE3D1039F)
- [DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-688CC19B-EFD0-493E-B4D0-C676FE7A5446)
- [DBMS_CLOUD_OCI_CORE_EXPORT_IMAGE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-55F0E76E-F486-4948-BF4D-CBDF1762D433)
- [DBMS_CLOUD_OCI_CORE_FAST_CONNECT_PROVIDER_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8B1A46E7-8874-41B4-9408-E0F7DE36ABF4)
- [DBMS_CLOUD_OCI_CORE_FAST_CONNECT_PROVIDER_SERVICE_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B9E452A1-F854-4ABC-B7CE-3B672B83E33B)
- [DBMS_CLOUD_OCI_CORE_GENERIC_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5DCD30B1-DC0F-4AC7-8E0E-ACE212065BCC)
- [DBMS_CLOUD_OCI_CORE_GENERIC_BM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F2A6D6EE-7347-41ED-814C-AFD6A5F573C7)
- [DBMS_CLOUD_OCI_CORE_GET_PUBLIC_IP_BY_IP_ADDRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A95B8F59-A91C-49C4-913C-697436F08702)
- [DBMS_CLOUD_OCI_CORE_GET_PUBLIC_IP_BY_PRIVATE_IP_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6DA175F3-62DF-4FAA-AFF0-E55D5E9F029A)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-ADE84A99-B042-4F4A-8CB1-9EDC82D9CA8D)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A01FF57F-A0BE-4BAC-BC14-0968C3345F91)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D39493D9-2E4E-45A7-B552-7264293D771A)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_DEVICE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2A060463-BEC2-4E31-8489-D429CAC67DC0)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FD54B72D-04A9-4280-81E3-BD6E8E00EC9B)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_STATUS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1191EC6A-F1F4-45D2-888A-9B4D4D4B36B0)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_DEVICE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-83E4C31B-6B58-46D6-8794-ADFB41109AFA)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_PHASE_ONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4884E48E-CA5E-4DD9-84E1-1D0C80B51C60)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_PHASE_TWO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-675F44D0-424D-41CA-B720-3DCFD0FBE87F)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6D14752D-2512-476A-AFC5-2AE10464B6CA)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_ERROR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-79654F7A-4D06-4CD5-AE5E-A24F9DC0DFDB)
- [DBMS_CLOUD_OCI_CORE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FAD285F9-8499-495C-A54D-572A305EA184)
- [DBMS_CLOUD_OCI_CORE_MULTIPATH_DEVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-19C2F349-3AE8-403B-BAF2-35338CC4E852)
- [DBMS_CLOUD_OCI_CORE_MULTIPATH_DEVICE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1ACE1243-B040-4DD6-B56E-A145761F231B)
- [DBMS_CLOUD_OCI_CORE_I_SCSI_VOLUME_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-166C3FCB-40E6-41DA-87BB-8C632984978F)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-265A4454-8735-4954-BB19-2C8E542F9FC4)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_FEATURES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-96D7ADAA-CF32-45CE-9B9E-3F6837E3FF84)
- [DBMS_CLOUD_OCI_CORE_IMAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DE6CEC67-0C9F-4931-AD6E-89CE9EEC5EE3)
- [DBMS_CLOUD_OCI_CORE_IMAGE_SHAPE_COMPATIBILITY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-572D3ED1-2D61-4727-A9BE-6C84AB8B9D80)
- [DBMS_CLOUD_OCI_CORE_IMAGE_SHAPE_COMPATIBILITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BACFE7E0-259A-4AB4-BF3B-F4D8D3CAD628)
- [DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F75B1003-25B8-416E-9D83-B3E602DBEAF2)
- [DBMS_CLOUD_OCI_CORE_IMAGE_SOURCE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DA4ED894-6B3B-4692-9CAA-898088A7D8E6)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C640FD91-FC54-4795-90DD-A686572A744B)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_AVAILABILITY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5760A0FD-5755-4622-A787-83686982DD05)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0A321DEF-C0FA-4FC2-85CD-86DDA9369417)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C1674AC6-5D93-4617-9853-1B8526573C24)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_AGENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1156E053-E5E1-4491-AF3C-9A1B7367406B)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5881768C-5459-4924-860F-97BBC1D7ADF3)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5FD99B55-1D8A-42F4-A522-280D4A84054D)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_MILAN_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-62208BC1-6435-4D50-8BC3-8E612A851885)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_MILAN_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-624012EB-D27B-4B75-8236-7C04AC1C5148)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_ROME_BM_GPU_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E98E7BA4-21E7-49AF-83AB-2F1A55ED8D2A)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_ROME_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9511464C-4383-49D9-9087-464B6F9D5AC0)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_AMD_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9A34A769-7C75-4EF4-99B2-A98A782F46FE)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_DETACHED_VOLUME_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4B69D26B-C899-4D94-91F1-A33F6E686993)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_GENERIC_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F57222B2-00CE-40D7-8A9E-D6DCAB5B00C3)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_IMAGE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1E46BA5A-8A91-4264-BCAB-C6361E998531)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4A1015A5-718B-4284-951C-539DAE40E72C)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C732D65B-CB6D-4D22-BE83-6CD1A738CAF9)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_ICELAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-64E12AD8-B50D-4706-9F2D-E4370BD5CD18)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_SKYLAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1AB88D2C-7F6D-4F32-BA91-4D553BB41203)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_INTEL_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8CCE9307-B76D-4E5C-9216-A152750B7255)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_ISCSI_ATTACH_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-435A9B87-BFA9-4BC8-B3A9-C0A649D44160)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_PARAVIRTUALIZED_ATTACH_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FC6D53FC-3FA3-4DBB-8030-F070E7CE558B)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_PERFORMANCE_BASED_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1C1DCC46-90B0-4370-9495-5BBFBF48CB36)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4084185A-DCFA-4C7F-86B1-7083070E98FA)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_FROM_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-579D4F37-F29E-47C1-A591-153D90D7EA37)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONFIGURATION_VOLUME_SOURCE_FROM_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9B0347E5-B989-44BB-BEA6-ACA81940032C)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CONSOLE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-73AE8CD7-58FD-4BC5-BE7F-AB24CEF99A30)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6FBB16EC-1E1D-4C5F-B1D8-AAC75B2FE62C)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_MAINTENANCE_REBOOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7DB11A0C-7E72-4BD9-AF89-D499DDC450E1)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_LOAD_BALANCER_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E8AA6BF2-3CFD-4CFC-95C5-B9C2970E03FD)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_LOAD_BALANCER_BACKEND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C99A6891-FA8C-4B29-A16F-E2BFFE19298E)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-058588A9-FA0C-4D5B-A64D-37601E636082)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POOL_PLACEMENT_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6C6A53CD-7592-4CAB-9D62-BEF07A7BF7C6)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_POWER_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D99257E5-FB11-4B12-B01B-19375CF27FA2)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_IMAGE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7E617522-D364-494A-9F7A-393DA7CB782E)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-26C83581-44FF-465B-99C1-C2CC197580B5)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B18CBA17-789B-490E-AE76-8161A85994BE)
- [DBMS_CLOUD_OCI_CORE_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-008142B1-CAAD-4432-B5C8-21C13BEC6B70)
- [DBMS_CLOUD_OCI_CORE_INTEL_ICELAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DF88F5F7-BDEC-4276-8C42-D6ACB9A9BC3A)
- [DBMS_CLOUD_OCI_CORE_INTEL_ICELAKE_BM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3CFE1867-9D66-45B8-AC67-3F4E26A29701)
- [DBMS_CLOUD_OCI_CORE_INTEL_SKYLAKE_BM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-33F18CB0-F41C-41ED-B49C-6BB4699B7C08)
- [DBMS_CLOUD_OCI_CORE_INTEL_SKYLAKE_BM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2EA823B9-4B35-4303-BE29-9840A3B7C29E)
- [DBMS_CLOUD_OCI_CORE_INTEL_VM_LAUNCH_INSTANCE_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-38D840AC-E0C0-4928-ABCC-01A2E3D5E9A1)
- [DBMS_CLOUD_OCI_CORE_INTEL_VM_PLATFORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4EA8565F-2AD1-412C-B496-DAC8B4D916EC)
- [DBMS_CLOUD_OCI_CORE_INTERNET_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6940BFBD-E002-4155-AFDA-6CF4A05E64D2)
- [DBMS_CLOUD_OCI_CORE_IPSEC_TUNNEL_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F478D58A-BF02-4C51-ABAC-7819F99F158B)
- [DBMS_CLOUD_OCI_CORE_IPV6_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C6D8C577-C757-401A-A7B9-993D8B7FCB93)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C5E5E5F5-CF85-4FAF-A3E9-353DC4AABD75)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_AVAILABILITY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E5C85F09-B8DE-4552-94BF-DEC4F4F8DDE8)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-68887BDE-D676-4965-9D9B-6F213A3A16AE)
- [DBMS_CLOUD_OCI_CORE_LAUNCH_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C246B3D8-4C9C-4729-9F1F-5D02F3686FEC)
- [DBMS_CLOUD_OCI_CORE_LETTER_OF_AUTHORITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-69132877-A8EC-4208-BA03-693A6A6AE533)
- [DBMS_CLOUD_OCI_CORE_LOCAL_PEERING_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AF0FF598-1F60-4738-915B-77DC520E9EB3)
- [DBMS_CLOUD_OCI_CORE_LOOP_BACK_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2F3BD1EA-945A-46E3-B6AC-4683216C70F3)
- [DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C379BCF4-BD9A-4A44-AE22-971A455E8CAF)
- [DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-97F0876B-FC05-4138-A53D-DC97F5BEECA5)
- [DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_REPORT_MEASUREMENTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-53039408-65E3-4692-A583-85F654B29B66)
- [DBMS_CLOUD_OCI_CORE_MEASURED_BOOT_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-53FEEE8A-1636-4B54-8EAF-34E97AF3572F)
- [DBMS_CLOUD_OCI_CORE_MEMBER_REPLICA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-48B8BE90-3074-4EBF-880C-19D482094154)
- [DBMS_CLOUD_OCI_CORE_MODIFY_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-379F05D5-CB1D-40E6-884B-9C55E398A0F7)
- [DBMS_CLOUD_OCI_CORE_NAT_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D41AB01E-C9EC-4342-9BEB-BC07E767A99E)
- [DBMS_CLOUD_OCI_CORE_NETWORK_SECURITY_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3FC619C6-CD7D-42C6-9B1F-CFE765238185)
- [DBMS_CLOUD_OCI_CORE_NETWORK_SECURITY_GROUP_VNIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2AD89BBE-B517-41E7-923F-CCDC5A97B7E7)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C9DC6DB-C31F-4654-95B9-290D3EFAD7F9)
- [DBMS_CLOUD_OCI_CORE_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-16787E62-C478-47F8-9091-406FB8CA2172)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ENTITY_RELATIONSHIP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-30607853-3DE1-44BE-B412-82406234897E)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0D5A1884-974C-4E06-991B-48C4D3E17CB7)
- [DBMS_CLOUD_OCI_CORE_NETWORKING_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2FF8E634-E520-451C-9E55-9CCD83A01094)
- [DBMS_CLOUD_OCI_CORE_PARAVIRTUALIZED_VOLUME_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90168143-E796-48C3-83E4-C35DB337C27F)
- [DBMS_CLOUD_OCI_CORE_PEER_REGION_FOR_REMOTE_PEERING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C5AD5F30-64B4-4C27-9534-EAFE395DD087)
- [DBMS_CLOUD_OCI_CORE_PERCENTAGE_OF_CORES_ENABLED_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A89FF20A-F172-40C5-82DE-5A388219F5D6)
- [DBMS_CLOUD_OCI_CORE_PERFORMANCE_BASED_AUTOTUNE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A0AFFC09-C0AB-4FF9-AA3C-DDAC27E57C35)
- [DBMS_CLOUD_OCI_CORE_PRIVATE_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5498A294-725E-44E8-A50B-F3E3E5A49431)
- [DBMS_CLOUD_OCI_CORE_PUBLIC_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-759E0AD3-A8FF-4458-B33D-B026A8DEE44A)
- [DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E0AE0252-F0F7-4C28-BB71-FEFF3AFEE045)
- [DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-85B1C64B-5B73-42F0-A8E3-33C2764A398C)
- [DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6AF704B1-CC91-4899-9D89-E7F2700B08CE)
- [DBMS_CLOUD_OCI_CORE_PUBLIC_IP_POOL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D208A4D7-5719-439C-A291-57C276C81CA9)
- [DBMS_CLOUD_OCI_CORE_REBOOT_MIGRATE_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7614926D-92FA-49C4-B8CD-51FE6EBD07DA)
- [DBMS_CLOUD_OCI_CORE_REMOTE_PEERING_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-65FF0DCB-6DC5-4B95-B806-4930293A2970)
- [DBMS_CLOUD_OCI_CORE_REMOTE_PEERING_CONNECTION_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C402A3FE-B5F5-4D54-B4D2-B49C71A5930E)
- [DBMS_CLOUD_OCI_CORE_REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C91B8F62-8F4B-4093-A0E2-F154ABFBC6E8)
- [DBMS_CLOUD_OCI_CORE_REMOVE_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-64D59E95-0668-4046-ABE2-7A31F89EED9F)
- [DBMS_CLOUD_OCI_CORE_REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1E66E10D-810B-4C7F-BB50-1EEE67917BEC)
- [DBMS_CLOUD_OCI_CORE_REMOVE_PUBLIC_IP_POOL_CAPACITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-866416CA-E0A0-4173-ABB3-62BDA883DA58)
- [DBMS_CLOUD_OCI_CORE_REMOVE_SUBNET_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-88FA9778-1A15-4D55-8154-1ECD97558427)
- [DBMS_CLOUD_OCI_CORE_REMOVE_VCN_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-56FEF501-E600-4599-A8C1-CCF52768709F)
- [DBMS_CLOUD_OCI_CORE_REMOVE_VCN_IPV6_CIDR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-87013B1B-65CD-48A6-9080-EE1D52B7C76C)
- [DBMS_CLOUD_OCI_CORE_RESET_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-12F8F9D8-DC0E-473B-AFF3-28576559AA67)
- [DBMS_CLOUD_OCI_CORE_ROUTE_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1A4EEC7F-DD2A-4435-B45A-3EE5B0F23ECB)
- [DBMS_CLOUD_OCI_CORE_SECURITY_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-07892B74-0568-4435-8A9E-D736281C924C)
- [DBMS_CLOUD_OCI_CORE_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4F60C363-7805-4EFD-97A5-44B4AAE25F85)
- [DBMS_CLOUD_OCI_CORE_SERVICE_ID_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C8E81E13-0809-4B22-90DF-1024D28BE5DE)
- [DBMS_CLOUD_OCI_CORE_SERVICE_ID_RESPONSE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CFB2849C-4468-4BCD-88A2-29DBC4AC2381)
- [DBMS_CLOUD_OCI_CORE_SERVICE_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FDBC9B8B-8208-4074-9107-9022DCDB7F5A)
- [DBMS_CLOUD_OCI_CORE_SHAPE_OCPU_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-54DB6550-B8B1-40FC-B546-9FA3063C0658)
- [DBMS_CLOUD_OCI_CORE_SHAPE_MEMORY_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-51DC29B2-8B09-4F3F-A4C8-B45D52E33BB3)
- [DBMS_CLOUD_OCI_CORE_SHAPE_NETWORKING_BANDWIDTH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A394C87A-7821-4E1E-B59D-5DA0E75F2A75)
- [DBMS_CLOUD_OCI_CORE_SHAPE_MAX_VNIC_ATTACHMENT_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-70C16534-EA98-4842-A478-60C803709787)
- [DBMS_CLOUD_OCI_CORE_SHAPE_SECURE_BOOT_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7F5C98BF-0034-4913-8B5A-FB0386CB71B0)
- [DBMS_CLOUD_OCI_CORE_SHAPE_MEASURED_BOOT_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-87C33918-51F2-4C9A-BF0B-41D0A5D86616)
- [DBMS_CLOUD_OCI_CORE_SHAPE_TRUSTED_PLATFORM_MODULE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-07369C1F-239C-48FB-8EBE-57080CAB16A8)
- [DBMS_CLOUD_OCI_CORE_SHAPE_NUMA_NODES_PER_SOCKET_PLATFORM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-76ECD194-70C1-489C-8FAC-B3671EDADD50)
- [DBMS_CLOUD_OCI_CORE_SHAPE_MEMORY_ENCRYPTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-42480240-34A1-4616-B66A-57F583E47461)
- [DBMS_CLOUD_OCI_CORE_SHAPE_SYMMETRIC_MULTI_THREADING_ENABLED_PLATFORM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FE5CB47E-AE5B-4647-97A5-C6DDA8A71C2B)
- [DBMS_CLOUD_OCI_CORE_SHAPE_ACCESS_CONTROL_SERVICE_ENABLED_PLATFORM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-064CAD78-6D6D-4231-AB04-20A12FFE024E)
- [DBMS_CLOUD_OCI_CORE_SHAPE_VIRTUAL_INSTRUCTIONS_ENABLED_PLATFORM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8489E2F8-B375-4E5C-B5AE-0263E1755D27)
- [DBMS_CLOUD_OCI_CORE_SHAPE_INPUT_OUTPUT_MEMORY_MANAGEMENT_UNIT_ENABLED_PLATFORM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3AA2F1ED-D374-4D79-970B-F4C1C2147B36)
- [DBMS_CLOUD_OCI_CORE_SHAPE_PLATFORM_CONFIG_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5BA8AA5A-3663-4D0B-A896-E13BC0E902EC)
- [DBMS_CLOUD_OCI_CORE_SHAPE_ALTERNATIVE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-28761E9F-0D87-4980-AC1F-A08590956733)
- [DBMS_CLOUD_OCI_CORE_SHAPE_ALTERNATIVE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-80A495F9-7AB1-4E92-B46F-CE9EF50F9F51)
- [DBMS_CLOUD_OCI_CORE_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-53B20872-E193-487A-BFA5-0BF758DC5DB7)
- [DBMS_CLOUD_OCI_CORE_SOFT_RESET_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-28A21CAA-6CBE-43D3-9ABC-E81FFAFD41A3)
- [DBMS_CLOUD_OCI_CORE_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D175BB16-EE3C-4CCE-B469-6AD399C064A2)
- [DBMS_CLOUD_OCI_CORE_SUBNET_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-784772BC-FE99-4BE1-981A-93371AA72B9F)
- [DBMS_CLOUD_OCI_CORE_TERMINATE_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0D1B957C-55B3-4842-B841-3E4AF6975A25)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ASSOCIATED_WITH_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5935C40E-5CE5-4D98-80AB-2D8F9E6A00C8)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ASSOCIATED_WITH_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EE9E4BB2-B480-4E6A-B129-93DFDAE5DC99)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_CONTAINS_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-21F56F63-7D93-4C02-8DF7-419F11A3EC67)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ROUTES_TO_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-09292B51-C8C9-4660-88AB-BEE7B44083F5)
- [DBMS_CLOUD_OCI_CORE_TOPOLOGY_ROUTES_TO_ENTITY_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-782A9D8A-E6E5-4C34-A1C4-36DB8C66912C)
- [DBMS_CLOUD_OCI_CORE_CPE_DEVICE_CONFIG_ANSWER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-70E8D8B3-387C-4BAA-AE4D-FCA69BF62B54)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_CPE_DEVICE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D4C42431-FDA1-4ADB-84D0-2DA8E96A7F9A)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_ROUTE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-72F024E0-A8BE-4C19-AF6B-7B8AE0E74FCD)
- [DBMS_CLOUD_OCI_CORE_TUNNEL_SECURITY_ASSOCIATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E479B3A3-A43D-4803-9601-43895E7A403D)
- [DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1850D047-DAA1-448E-ABAE-BED281A7B9CD)
- [DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1DF2A845-3E2F-4014-BD75-ADC87AA0DF0C)
- [DBMS_CLOUD_OCI_CORE_UPDATE_BOOT_VOLUME_KMS_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6F6405EB-EFA9-489E-A9C5-1A44C87A0444)
- [DBMS_CLOUD_OCI_CORE_UPDATE_BYOIP_RANGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4F4557DD-6904-49ED-805A-9EE92841AEF6)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CAPACITY_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-01C1B178-77A5-473F-8F4B-3A53FDB7E75A)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CAPTURE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-72020787-D16D-4184-813F-25FB95428F0A)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-04616219-D270-4061-A189-3B6E8F5C4A64)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_INSTANCE_POOL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8136B48C-C438-48B1-8C84-941194C61830)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CLUSTER_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-54B8E9B6-D628-4F90-8213-255F6E1C12F5)
- [DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CAPACITY_RESERVATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4B1048D6-E871-4392-AC66-09E9DACE5FAF)
- [DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CAPACITY_TOPOLOGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E66C5688-24EF-4984-9451-4676370315C0)
- [DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C7CC7779-557B-4508-8F0F-5076FF77B270)
- [DBMS_CLOUD_OCI_CORE_UPDATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C4697F87-A45D-43E0-AF64-4F30529F99FD)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CONSOLE_HISTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-992D63BA-D657-4792-AD19-1B57D5555719)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-CA911E93-9BD9-4978-87DE-97999B6B6EA2)
- [DBMS_CLOUD_OCI_CORE_UPDATE_MACSEC_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8250EDED-E10C-44E3-A010-0B4544C28553)
- [DBMS_CLOUD_OCI_CORE_UPDATE_MACSEC_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BDEC7F90-0DC8-49ED-BB0C-2C95DF3099F7)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CROSS_CONNECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-17BEDB4C-6159-4409-927B-0F6C1CC68A37)
- [DBMS_CLOUD_OCI_CORE_UPDATE_CROSS_CONNECT_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BB353A54-E2FC-4CA9-994F-0D5D8991920E)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DEDICATED_CAPACITY_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D71F0E91-DA21-4F9B-8FD5-747360FA3BAD)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DEDICATED_VM_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BA56E377-3AF8-4A47-B2A4-78CEF222A7D2)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DHCP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-17C99D78-14D2-4231-92F8-DBAB0DC49BD4)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1800CED4-8C0F-4402-9A7F-BFBEA2E9FBED)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6A87B153-8334-4966-924E-CAFD0C5B3B5C)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-669C32D2-6A76-4F0D-9816-DD9DF0C91CDC)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D721ABD3-3E45-447F-A6FB-BF32BC398D7A)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DEFE7603-E75D-4EAD-8C01-BBBA7B23CF9E)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-455A1F82-1D34-45D6-B416-1922761F8948)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-26C89D6E-C60B-4425-B595-09F453601881)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E7743F4F-3C93-4822-A276-06BBC8C57662)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C4CB0FD-588F-48CC-97F7-5E37EA0EB76F)
- [DBMS_CLOUD_OCI_CORE_UPDATE_DRG_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-EC4474F9-B5C2-40A4-9B7B-88460C23BC11)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90744027-C5D4-4838-950E-178BCB9A8D9D)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_TUNNEL_BGP_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-601E83CC-35E0-4908-8AAA-7F9009E81DDD)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_TUNNEL_ENCRYPTION_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E3723C3A-4900-4F33-A5C0-52E7799BFAAE)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A8F33153-E017-4AE5-BFC8-1BB008870C28)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A99F07D2-40DF-41D7-A51A-DB4508919980)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D53F1C32-6A5A-45A4-8609-41CD3DB21B73)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_AGENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4C7E0841-328D-48F6-8DB4-994F169DE0C7)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_AVAILABILITY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1718ACF6-C4EF-4A29-B186-6D28007D63B5)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3B5C0067-04B2-41B2-999C-A4022EAAAC31)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_CONSOLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1D1D6CB7-3BEC-490A-84F8-A08825B18624)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E206B7DE-AD3A-4935-ADEF-E481D14C86D5)
- [DBMS_CLOUD_OCI_CORE_UPDATE_LAUNCH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DB44D37C-0AB0-41AA-AEF7-0CDB73EFB013)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-BC3BCEDA-A6BE-406C-8CEF-29530DB2C3DA)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C450907B-FE37-4E97-B666-7E443B74E177)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_PLACEMENT_CONFIGURATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-E2213634-5308-428F-A798-CAEE1039E2C1)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INSTANCE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1242EF65-2330-4E08-B339-D354A8743F08)
- [DBMS_CLOUD_OCI_CORE_UPDATE_INTERNET_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AD2BFD70-24D1-42F6-A2C9-943DC10A9988)
- [DBMS_CLOUD_OCI_CORE_UPDATE_IPV6_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AB67247F-3AAB-490A-A25E-2ADB248BD0A5)
- [DBMS_CLOUD_OCI_CORE_UPDATE_LOCAL_PEERING_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2EAA75A2-1F84-4A58-A593-D9B863E758D5)
- [DBMS_CLOUD_OCI_CORE_UPDATE_NAT_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-422442E1-D0B4-4ABF-9C36-0DD39B3D2603)
- [DBMS_CLOUD_OCI_CORE_UPDATE_NETWORK_SECURITY_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-6F756C16-E6A4-4A48-8967-59BFE7C86593)
- [DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-36683A01-6700-47B9-8951-D44612E19173)
- [DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-9FDFA5C8-3E71-4F26-B2AD-ED6367F94836)
- [DBMS_CLOUD_OCI_CORE_UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-05CFF65F-0979-495F-898B-B60EF305E723)
- [DBMS_CLOUD_OCI_CORE_UPDATE_PRIVATE_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AC54287C-11A9-4FD1-8A1F-A973C73B9000)
- [DBMS_CLOUD_OCI_CORE_UPDATE_PUBLIC_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-56B8E73D-F8D6-40C0-AD91-E9811F9B0D85)
- [DBMS_CLOUD_OCI_CORE_UPDATE_PUBLIC_IP_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-88573359-E1CD-4E54-8C00-2950F1707095)
- [DBMS_CLOUD_OCI_CORE_UPDATE_REMOTE_PEERING_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7A2AEEF0-44CA-4658-85A8-DC4C56305323)
- [DBMS_CLOUD_OCI_CORE_UPDATE_ROUTE_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B85FA92B-52C4-4701-908E-A81911328A8C)
- [DBMS_CLOUD_OCI_CORE_UPDATE_SECURITY_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7D80DE4C-F311-4C31-A70F-3E3C91ECED57)
- [DBMS_CLOUD_OCI_CORE_UPDATE_SERVICE_GATEWAY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-90FFF8AF-0930-46F1-8416-458D0B40FDFA)
- [DBMS_CLOUD_OCI_CORE_UPDATE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-63701BD0-5125-46CB-99D7-7E4AD0E4BB63)
- [DBMS_CLOUD_OCI_CORE_UPDATE_TUNNEL_CPE_DEVICE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-210D6F68-1E2C-47CA-9439-4325F3F793E6)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VCN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A77B93C1-7BFF-43DF-AD90-D87523571AB8)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VIRTUAL_CIRCUIT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-034A441D-1F5E-4CE2-9A24-4AD841CDBD3A)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DB333312-7A23-4D99-B741-8F81A08AE9F4)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-82F01358-C9C8-4B3B-99FE-68B13099AA8C)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A2D1AD3D-BAB4-4BB6-B0B0-4C495C7DA0E8)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2AB4E03C-85D6-4D65-AEAA-519F9F8ADF8A)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_BACKUP_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-78E7EE77-C5DE-4872-A73F-626EFC38E4C6)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-55EDF5E0-0B3E-428F-BDC3-D9F9FE0B5D81)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_GROUP_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AFF2ECFD-0E36-471E-B100-2F65C801D025)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B1CFE9B4-EF20-4FB0-B35C-325052EBE39D)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VOLUME_KMS_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-450852AB-CAB6-4C1E-AC85-D07533BDEA1E)
- [DBMS_CLOUD_OCI_CORE_UPDATE_VTAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-54D72B6D-2DEA-43DA-B0B7-49C35D755E0B)
- [DBMS_CLOUD_OCI_CORE_UPDATED_NETWORK_SECURITY_GROUP_SECURITY_RULES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3239C87E-6E03-4E8B-9335-20962500296B)
- [DBMS_CLOUD_OCI_CORE_UPGRADE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D295C61B-5429-4FC0-8650-FAE5BA714C89)
- [DBMS_CLOUD_OCI_CORE_VCN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-D16323AD-6B73-457E-B13B-820520FA19C6)
- [DBMS_CLOUD_OCI_CORE_VCN_DNS_RESOLVER_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F47DD3DA-A776-4A2B-90AD-1AAB93332ABE)
- [DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_CREATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AA3A12BA-BED3-4550-A411-C64AB5F5C26A)
- [DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F6962F2D-0B47-4A34-B075-E7498AD4F21F)
- [DBMS_CLOUD_OCI_CORE_VCN_DRG_ATTACHMENT_NETWORK_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-51B7CAE0-C497-4259-A747-56A7CC238286)
- [DBMS_CLOUD_OCI_CORE_VCN_TOPOLOGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7C7A3666-E665-4D4D-BA74-E0EE9CD2A9A5)
- [DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-76E6CFAA-205F-4DEB-8FDF-B9681F4FF6B1)
- [DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-229D5D8D-DA28-4991-A3D1-84B58FC87968)
- [DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F141335B-77BD-499F-BD6A-0AF1AF299AAF)
- [DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_DRG_ATTACHMENT_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3C510CD0-34F3-4FD5-B91E-1974841E9B04)
- [DBMS_CLOUD_OCI_CORE_VIRTUAL_CIRCUIT_PUBLIC_PREFIX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-257C4B1D-F71F-4DC4-BDCE-D4400DBD97A7)
- [DBMS_CLOUD_OCI_CORE_VLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-5B66CE61-C362-48C6-A043-DE37154D1451)
- [DBMS_CLOUD_OCI_CORE_VNIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-231B123A-F9B6-4A55-B8DA-48479EC06E8C)
- [DBMS_CLOUD_OCI_CORE_VNIC_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-1B65D323-B520-4EEC-B161-BF2C6A91F46E)
- [DBMS_CLOUD_OCI_CORE_BLOCK_VOLUME_REPLICA_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-B8BD0D3F-09FC-4D1B-8094-54CC667499AB)
- [DBMS_CLOUD_OCI_CORE_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8D74562D-99B8-44A4-9014-435461B09D9B)
- [DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-2974B1DD-60C3-40DA-ADD6-C4DB1F65ACC2)
- [DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-A0702114-3E0E-4116-8C2B-3DFFE8341F7C)
- [DBMS_CLOUD_OCI_CORE_VOLUME_BACKUP_POLICY_ASSIGNMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-978563E1-C7A7-404A-83C9-68DFFCAE4954)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-7EAA8127-B238-47FA-A8B5-3FC0709222F3)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-0E632ED1-444C-49A9-8F58-87E5E5216BE5)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-FE08C728-AD56-4821-B71B-7DE2CF7CCA00)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-34AD63F8-86C1-4836-8BB8-6B810E9C5AF3)
- [DBMS_CLOUD_OCI_CORE_MEMBER_REPLICA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-179D2270-EE88-4D1E-90E7-1C2FD49B01C6)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_REPLICA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-3817AB56-B127-4243-B635-E839C6AC745C)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-C5C0E817-9775-484F-BF33-0DA9BBDB71D4)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-65E70437-DEF9-4529-90A3-1CE379840508)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUME_GROUP_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-05461648-50C1-4781-A135-7E7D4540E975)
- [DBMS_CLOUD_OCI_CORE_VOLUME_GROUP_SOURCE_FROM_VOLUMES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-AFCEAD43-9C35-4231-BBFF-32BB88A99666)
- [DBMS_CLOUD_OCI_CORE_VOLUME_KMS_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-F3E2214A-AB18-4C24-B235-68DAA83F0A0C)
- [DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_BLOCK_VOLUME_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-85F76994-50A7-47CF-8F90-B96973025E74)
- [DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_VOLUME_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-8329DD83-5F95-4863-AFE1-E40E96B173B1)
- [DBMS_CLOUD_OCI_CORE_VOLUME_SOURCE_FROM_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-DE82B4B0-7999-4225-9DE5-8EE8948446B3)
- [DBMS_CLOUD_OCI_CORE_VTAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/core_t.html#ADSDK-GUID-4274A9C0-0C69-45B4-ABD8-44E9F6C7085B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
