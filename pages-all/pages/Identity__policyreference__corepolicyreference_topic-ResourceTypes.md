# Resource-Types
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-ResourceTypes.htm
- Fetched: 2026-09-05 02:26 CDT

# Resource-Types

Core services resource types

[Networking](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-ResourceTypes.htm#)

### Aggregate Resource-Type

`virtual-network-family`

`drgs`(covers`drg-object`,`drg-route-table`,`drg-route-distribution`,`drg-attachment`)

### Individual Resource-Types

`vcns`

`subnets`

`route-tables`

`network-security-groups`

`security-lists`

`dhcp-options`

`private-ips`

`public-ips`

`ipv6s`

`internet-gateways`

`nat-gateways`

`service-gateways`

`local-peering-gateways`(which includes`local-peering-from`, and`local-peering-to`)

`remote-peering-connections`(which includes`remote-peering-from`, and`remote-peering-to`)

`drg-object`

`drg-attachments`

`drg-route-tables`

`drg-route-distributions`

`cpes`

`ipsec-connections`

`cross-connects`

`cross-connect-groups`

`virtual-circuits`

`vnics`

`vtaps`

`vnic-attachments`

`vlans`

`byoiprange`

`publicippool`

`ipam`

### Comments

A policy that uses`<verb> virtual-network-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual resource-types.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-Details_for_Verb__ResourceType_Combinations.htm)for details of the API operations covered by each verb, for each individual resource-type included in`virtual-network-family`.

[Compute](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-ResourceTypes.htm#)

### instance-family Aggregate Resource-Type

The`instance-family`aggregate resource-type covers these individual resource-types:

`app-catalog-listing`

`console-histories`

`instances`

`instance-console-connection`

`instance-images`

`volume-attachments`(includes only the permissions required for attaching volumes to instances)

### compute-management-family Aggregate Resource-Type

The`compute-management-family`aggregate resource-type covers these individual resource-types:

`instance-configurations`

`instance-pools`

`cluster-networks`

### instance-agent-family Aggregate Resource-Type

The`instance-agent-family`aggregate resource-type covers this individual resource-type:

`instance-agent-plugins`

### instance-agent-command-family Aggregate Resource-Type

The`instance-agent-command-family`aggregate resource-type covers this individual resource-type:

`instance-agent-commands`

### Additional Individual Resource-Types

`auto-scaling-configurations`

`compute-bare-metal-hosts`

`compute-capacity-reports`

`compute-capacity-reservations`

`compute-clusters`

`compute-global-image-capability-schema`

`compute-gpu-memory-clusters`

`compute-gpu-memory-fabrics`

`compute-host-groups`

`compute-image-capability-schema`

`dedicated-vm-hosts`

`instance-agent-commands`

`work-requests`

### Comments

A policy that uses`<verb> instance-family`or`<verb> compute-management-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual resource-types in the family.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-Details_for_Verb__ResourceType_Combinations.htm)for details of the API operations covered by each verb, for each individual resource-type.

[Block Volume](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-ResourceTypes.htm#)

### Aggregate Resource-Type

`volume-family`

### Individual Resource-Types

`volumes`

&gt;`volume-attachments`

&gt;`volume-backups`

&gt;`boot-volume-backups`

&gt;`backup-policies`

&gt;`backup-policy-assignments`

&gt;`volume-groups`

&gt;`volume-group-backups`

### Comments

A policy that uses`><verb> volume-family`is equivalent to writing one with a separate`><verb> <individual resource-type>`statement for each of the individual resource-types.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/corepolicyreference_topic-Details_for_Verb__ResourceType_Combinations.htm)for details of the API operations covered by each verb, for each individual resource-type included in`>volume-family`
