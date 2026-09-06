# Compute Cloud at Customer Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#dcoc-content-body)

## Compute Cloud at Customer Common Types

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_INVENTORY_T Type

Inventory for a Compute Cloud@Customer infrastructure. This information cannot be updated and is from the infrastructure. The information will only be available after the connectionState is transitioned to CONNECTED.

Syntax
```

```

Fields

Field Description

`serial_number`

(optional) The serial number of the Compute Cloud@Customer infrastructure rack.

`management_node_count`

(optional) The number of management nodes that are available and in active use on the Compute Cloud@Customer infrastructure rack.

`compute_node_count`

(optional) The number of compute nodes that are available and usable on the Compute Cloud@Customer infrastructure rack. There is no distinction of compute node type in this information.

`capacity_storage_tray_count`

(optional) The number of storage trays in the Compute Cloud@Customer infrastructure rack that are designated for capacity storage.

`performance_storage_tray_count`

(optional) The number of storage trays in the Compute Cloud@Customer infrastructure rack that are designated for performance storage.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_MANAGEMENT_NODE_T Type

Information about an individual management node in a Compute Cloud@Customer infrastructure.

Syntax
```

```

Fields

Field Description

`ip`

(optional) Address of the management node.

`hostname`

(optional) Hostname for interface to the management node.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_ROUTING_STATIC_DETAILS_T Type

Static routing information for a rack.

Syntax
```

```

Fields

Field Description

`uplink_vlan`

(optional) The virtual local area network (VLAN) identifier used to connect to the uplink (only access mode is supported).

`uplink_hsrp_group`

(optional) The uplink Hot Standby Router Protocol (HSRP) group value for the switch in the Compute Cloud@Customer infrastructure.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_PEER_INFORMATION_T Type

Routing information for peer nodes using the Border Gateway Protocol (BGP).

Syntax
```

```

Fields

Field Description

`asn`

(optional) The Autonomous System Number (ASN) of the peer network.

`ip`

(optional) Neighbor Border Gateway Protocal (BGP) IP address. The IP address usually refers to the customer data center router.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_PEER_INFORMATION_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_peer_information_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_ROUTING_DYNAMIC_DETAILS_T Type

Dynamic routing information for the Compute Cloud@Customer infrastructure.

Syntax
```

```

Fields

Field Description

`peer_information`

(optional) The list of peer devices in the dynamic routing configuration.

`oracle_asn`

(optional) The Oracle Autonomous System Number (ASN) to control routing and exchange information within the dynamic routing configuration.

`bgp_topology`

(optional) The topology in use for the Border Gateway Protocol (BGP) configuration.

Allowed values are: 'TRIANGLE', 'SQUARE', 'MESH'

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_MANAGEMENT_NODE_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_ccc_infrastructure_management_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_NETWORK_CONFIGURATION_T Type

Configuration information for the Compute Cloud@Customer infrastructure. This network configuration information cannot be updated and is retrieved from the data center. The information will only be available after the connectionState is transitioned to CONNECTED.

Syntax
```

```

Fields

Field Description

`management_nodes`

(optional) Information about the management nodes that are provisioned in the Compute Cloud@Customer infrastructure.

`uplink_port_speed_in_gbps`

(optional) Uplink port speed defined in gigabytes per second. All uplink ports must have identical speed.

`uplink_port_count`

(optional) Number of uplink ports per spine switch. Connectivity is identical on both spine switches. For example, if input is two 100 gigabyte ports; then port-1 and port-2 on both spines will be configured.

`uplink_vlan_mtu`

(optional) The virtual local area network (VLAN) maximum transmission unit (MTU) size for the uplink ports.

`uplink_netmask`

(optional) Netmask of the subnet that the Compute Cloud@Customer infrastructure is connected to.

`uplink_port_forward_error_correction`

(optional) The port forward error correction (FEC) setting for the uplink port on the Compute Cloud@Customer infrastructure.

Allowed values are: 'AUTO', 'FIRE_CODE_FEC', 'REED_SOLOMON_CONSORTIUM_16', 'REED_SOLOMON_FEC', 'REED_SOLOMON_IEEE'

`uplink_domain`

(optional) Domain name to be used as the base domain for the internal network and by public facing services.

`uplink_gateway_ip`

(optional) Uplink gateway in the datacenter network that the Compute Cloud@Customer connects to.

`spine_ips`

(optional) Addresses of the network spine switches.

`spine_vip`

(optional) The spine switch public virtual IP (VIP). Traffic routed to the Compute Cloud@Customer infrastructure and and virtual cloud networks (VCNs) should have this address as next hop.

`mgmt_vip_hostname`

(optional) The hostname corresponding to the virtual IP (VIP) address of the management nodes.

`mgmt_vip_ip`

(optional) The IP address used as the virtual IP (VIP) address of the management nodes.

`dns_ips`

(optional) The domain name system (DNS) addresses that the Compute Cloud@Customer infrastructure uses for the data center network.

`infrastructure_routing_static`

(optional)

`infrastructure_routing_dynamic`

(optional)

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_INFORMATION_T Type

Upgrade information that relates to a Compute Cloud@Customer infrastructure. This information cannot be updated.

Syntax
```

```

Fields

Field Description

`current_version`

(optional) The current version of software installed on the Compute Cloud@Customer infrastructure.

`time_of_scheduled_upgrade`

(optional) Compute Cloud@Customer infrastructure next upgrade time. The rack might have performance impacts during this time.

`scheduled_upgrade_duration`

(optional) Expected duration of Compute Cloud@Customer infrastructure scheduled upgrade. The actual upgrade time might be longer or shorter than this duration depending on rack activity, this is only an estimate.

`is_active`

(optional) Indication that the Compute Cloud@Customer infrastructure is in the process of an upgrade or an upgrade activity (such as preloading upgrade images).

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_T Type

The Oracle Cloud Infrastructure resource representing the connection to the hardware and software located in a customer's data center running the Compute Cloud@Customer IaaS services.

Syntax
```

```

Fields

Field Description

`id`

(required) The Compute Cloud@Customer infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This cannot be changed once created.

`short_name`

(optional) The Compute Cloud@Customer infrastructure short name. This cannot be changed once created. The short name is used to refer to the infrastructure in several contexts and is unique.

`display_name`

(required) The name that will be used to display the Compute Cloud@Customer infrastructure in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed. Avoid entering confidential information.

`description`

(optional) A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure. Avoid entering confidential information.

`compartment_id`

(required) The infrastructure compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`subnet_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network subnet that is used to communicate with Compute Cloud@Customer infrastructure.

`connection_state`

(optional) The current connection state of the infrastructure. A user can only update it from REQUEST to READY or from any state back to REJECT. The system automatically handles the REJECT to REQUEST, READY to CONNECTED, or CONNECTED to DISCONNECTED transitions.

Allowed values are: 'REJECT', 'REQUEST', 'READY', 'CONNECTED', 'DISCONNECTED'

`connection_details`

(optional) A message describing the current connection state in more detail.

`ccc_upgrade_schedule_id`

(optional) Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.

`provisioning_fingerprint`

(optional) Fingerprint of a Compute Cloud@Customer infrastructure in a data center generated during the initial connection to this resource. The fingerprint should be verified by the administrator when changing the connectionState from REQUEST to READY.

`provisioning_pin`

(optional) Code that is required for service personnel to connect a Compute Cloud@Customer infrastructure in a data center to this resource. This code will only be available when the connectionState is REJECT (usually at create time of the Compute Cloud@Customer infrastructure).

`time_created`

(required) Compute Cloud@Customer infrastructure creation date and time, using an RFC3339 formatted datetime string.

`time_updated`

(optional) Compute Cloud@Customer infrastructure updated date and time, using an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Compute Cloud@Customer infrastructure.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current lifecycle state in more detail. For example, this can be used to provide actionable information for a resource that is in a Failed state.

`infrastructure_inventory`

(optional)

`infrastructure_network_configuration`

(optional)

`upgrade_information`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_SUMMARY_T Type

Summary information about a Compute Cloud@Customer infrastructure.

Syntax
```

```

Fields

Field Description

`id`

(required) The Compute Cloud@Customer infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This cannot be changed once created.

`short_name`

(optional) The Compute Cloud@Customer infrastructure short name. This is generated at the time the resource is created and cannot be changed. The short name can be used when communicating with Oracle Service and may be used during the configuration of the data center network.

`display_name`

(required) The name that will be used to display the Compute Cloud@Customer infrastructure in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed. Avoid entering confidential information.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the infrastructure.

`subnet_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network subnet that is used to communicate with Compute Cloud@Customer infrastructure.

`time_created`

(required) Compute Cloud@Customer infrastructure creation date and time. An RFC3339 formatted datetime string.

`connection_state`

(optional) The current connection state of the infrastructure.

`lifecycle_state`

(required) The current state of the Compute Cloud@Customer infrastructure.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_ccc_infrastructure_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_COLLECTION_T Type

Results of a Compute Cloud@Customer infrastructure search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Compute Cloud@Customer infrastructures.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_SCHEDULE_EVENT_T Type

A period where upgrades may be applied to Compute Cloud@Customer infrastructures associated with the schedule. All upgrade windows may not be used.

Syntax
```

```

Fields

Field Description

`name`

(required) Generated name associated with the event.

`description`

(required) A description of the Compute Cloud@Customer upgrade schedule time block.

`time_start`

(required) The date and time when the Compute Cloud@Customer upgrade schedule event starts, inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences, this is the date that a recurrence can start being applied.

`schedule_event_duration`

(required) The duration of this block of time. The duration must be specified and be of the ISO-8601 format for durations.

`schedule_event_recurrences`

(optional) Frequency of recurrence of schedule block. When this field is not included, the event is assumed to be a one time occurrence. The frequency field is strictly parsed and must conform to RFC-5545 formatting for recurrences.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_SCHEDULE_EVENT_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_ccc_schedule_event_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_T Type

Defines a schedule for preferred upgrade times.

Syntax
```

```

Fields

Field Description

`id`

(required) Upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This cannot be changed once created.

`display_name`

(required) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.

`description`

(optional) An optional description of the Compute Cloud@Customer upgrade schedule. Avoid entering confidential information.

`compartment_id`

(required) Compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the Compute Cloud@Customer upgrade schedule.

`time_created`

(required) The time the upgrade schedule was created, using an RFC3339 formatted datetime string.

`time_updated`

(optional) The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.

`lifecycle_state`

(required) Lifecycle state of the resource.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, the message can be used to provide actionable information for a resource in a Failed state.

`events`

(optional) List of preferred times for Compute Cloud@Customer infrastructures associated with this schedule to be upgraded.

`infrastructure_ids`

(optional) List of Compute Cloud@Customer infrastructure[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that are using this upgrade schedule.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_SUMMARY_T Type

Basic information about a Compute Cloud@Customer schedule. This summary only includes high level resource information, not the schedule events.

Syntax
```

```

Fields

Field Description

`id`

(required) The upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This cannot be changed once created.

`display_name`

(required) Compute Cloud@Customer upgrade schedule display name. Avoid entering any confidential information.

`compartment_id`

(required) Compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the Compute Cloud@Customer Upgrade Schedule.

`time_created`

(required) The time the upgrade schedule was created. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Compute Cloud@Customer upgrade schedule.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_ccc_upgrade_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_COLLECTION_T Type

Results of a Compute Cloud@Customer upgrade schedule search. Contains the summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Compute Cloud@Customer upgrade schedules.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CHANGE_CCC_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type

Information required for the compartment change operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CHANGE_CCC_UPGRADE_SCHEDULE_COMPARTMENT_DETAILS_T Type

Change the compartment of a Compute Cloud@Customer upgrade schedule.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_INFRASTRUCTURE_DETAILS_T Type

The configuration details for creating Compute Cloud@Customer infrastructure.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name that will be used to display the Compute Cloud@Customer infrastructure in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed. Avoid entering confidential information.

`description`

(optional) A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure. Avoid entering confidential information.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the infrastructure.

`subnet_id`

(required) Identifier for network subnet that will be used to communicate with Compute Cloud@Customer infrastructure.

`connection_state`

(optional) The current connection state of the Compute Cloud@Customer infrastructure. This value will default to REJECT if the value is not provided. The only valid value at creation time is REJECT.

`connection_details`

(optional) A message describing the current connection state in more detail.

`ccc_upgrade_schedule_id`

(optional) Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be upgraded at any time.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_SCHEDULE_EVENT_T Type

A period where upgrades may be applied to Compute Cloud@Customer infrastructures associated with the schedule. All upgrade windows may not be used.

Syntax
```

```

Fields

Field Description

`description`

(required) A description of the Compute Cloud@Customer upgrade schedule time block.

`time_start`

(required) The date and time when the Compute Cloud@Customer upgrade schedule event starts, inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences, this is the date that a recurrence can start being applied.

`schedule_event_duration`

(required) The duration of this block of time. The duration must be specified and be of the ISO-8601 format for durations.

`schedule_event_recurrences`

(optional) Frequency of recurrence of schedule block. When this field is not included, the event is assumed to be a one time occurrence. The frequency field is strictly parsed and must conform to RFC-5545 formatting for recurrences.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_SCHEDULE_EVENT_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_create_ccc_schedule_event_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_UPGRADE_SCHEDULE_DETAILS_T Type

Defines a schedule for times when automated Compute Cloud@Customer upgrades are preferred. A created upgrade schedule must supply events with a minimum frequency and duration or the schedule will be rejected. Upgrades may impact performance of Compute Cloud@Customer infrastructures when they are being applied.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.

`compartment_id`

(required) Compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the Compute Cloud@Customer Upgrade Schedule.

`description`

(optional) An optional description of the Compute Cloud@Customer upgrade schedule. Avoid entering confidential information.

`events`

(required) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_ERROR_T Type

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

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_INFRASTRUCTURE_DETAILS_T Type

Updates Compute Cloud@Customer infrastructure configuration details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name that will be used to display the Compute Cloud@Customer infrastructure in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed. Avoid entering confidential information.

`description`

(optional) A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure. Avoid entering confidential information.

`subnet_id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network subnet that is used to communicate with Compute Cloud@Customer infrastructure.

`connection_state`

(optional) An updated connection state of the Compute Cloud@Customer infrastructure.

`connection_details`

(optional) A message describing the current connection state in more detail.

`ccc_upgrade_schedule_id`

(optional) Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_SCHEDULE_EVENT_T Type

A period where upgrades may be applied to Compute Cloud@Customer infrastructures associated with the schedule. All upgrade windows may not be used.

Syntax
```

```

Fields

Field Description

`description`

(required) A description of the Compute Cloud@Customer upgrade schedule time block.

`time_start`

(required) The date and time when the Compute Cloud@Customer upgrade schedule event starts, inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences, this is the date that a recurrence can start being applied.

`schedule_event_duration`

(required) The duration of this block of time. The duration must be specified and be of the ISO-8601 format for durations.

`schedule_event_recurrences`

(optional) Frequency of recurrence of schedule block. When this field is not included, the event is assumed to be a one time occurrence. The frequency field is strictly parsed and must conform to RFC-5545 formatting for recurrences.

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_SCHEDULE_EVENT_TBL Type

Nested table type of dbms_cloud_oci_compute_cloud_at_customer_update_ccc_schedule_event_t.

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_UPGRADE_SCHEDULE_DETAILS_T Type

Updates the schedule details, all schedule information must be entered, similar to an initial schedule create. Include all events in the update.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.

`description`

(optional) An optional description of the Compute Cloud@Customer upgrade schedule. Avoid entering confidential information.

`events`

(optional) List of preferred times for a Compute Cloud@Customer infrastructure to be upgraded.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

- [Compute Cloud at Customer Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-362A3D80-1AA8-4287-93CA-BCC5D08E78A7)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-72E140A5-34D4-461A-BD53-1A5CC81A3A22)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_INVENTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-EE295596-9F9E-4C20-ACAB-AD04D5D064EA)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_MANAGEMENT_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-F517CF15-C733-48A1-B4F7-C7A9D76623E8)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_ROUTING_STATIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-70132F0B-4116-40B1-A01C-F30161D9C027)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_PEER_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-275AD01C-8DF9-466F-B716-BE0C8175291A)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_PEER_INFORMATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-6E18F76B-2826-4F60-9180-575AE2C81889)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_ROUTING_DYNAMIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-69BDEAFE-EE64-49CD-AD91-C05FD6DD6262)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_MANAGEMENT_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-96925EC6-F5B2-44E6-8E1E-D934DD0D7C16)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-A5E8C1A9-AEC4-461C-8902-49728E32988B)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-FAF06F88-5DFB-461B-B8A8-020C1ACD8563)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-FF7FB0FE-1C5F-4C48-8055-FF6A36074242)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-7A5F4EC1-FB56-4E0A-B8C8-11294A5FA07F)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-905A15AD-5DA5-49B2-92E0-04FEF2BF382D)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_INFRASTRUCTURE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-87CC7B5B-0370-4C26-BA1A-908FD79DEB5C)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_SCHEDULE_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-1C081852-3C92-46FB-ACF0-EB7D699CCA9C)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_SCHEDULE_EVENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-BAF4038C-B96A-4D36-B958-791A0D4FE5A1)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-AB3C7C4F-AF2E-4D90-8E9B-CA987E404A19)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-E8391B06-259B-4EE8-950D-3A1ED5AE83A4)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-8359005C-FA0C-4E0A-8F0E-C0EA4DB60640)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CCC_UPGRADE_SCHEDULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-6BED5188-8053-42BF-AA93-06E353749887)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CHANGE_CCC_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-E417212F-348D-4720-8B9C-C37866F78079)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CHANGE_CCC_UPGRADE_SCHEDULE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-4A4869D9-0CEB-41F8-8823-9FE3DB1CFA18)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-3B634251-D50F-497C-BDB6-9997DF438996)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_SCHEDULE_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-7F1EDDED-ACD0-413F-BB1D-66169C99CB5B)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_SCHEDULE_EVENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-263F4EB9-32AC-4076-8060-E39F86E8220D)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_CREATE_CCC_UPGRADE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-5E3CAC9F-7C8B-4F39-9C9D-3AC65AEA5BC1)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-5C3B2E1B-70AC-4FFB-ACF1-56511F26E45A)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-685B44ED-0306-4F26-B4AD-E8D0E8229B65)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_SCHEDULE_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-FC78372B-EB91-4DDA-9ADC-7BD36198109B)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_SCHEDULE_EVENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-7EE44D11-813E-4D46-A1D2-CCB0A9B0EE55)
- [DBMS_CLOUD_OCI_COMPUTE_CLOUD_AT_CUSTOMER_UPDATE_CCC_UPGRADE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_cloud_at_customer_t.html#ADSDK-GUID-9CDB7E67-4B45-42F7-8949-90CBA3DCC5E3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
