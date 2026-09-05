# Bastion IAM Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/bastionpolicyreference.htm
- Fetched: 2026-09-05 01:42 CDT

# Bastion IAM Policies

This topic covers details for writing policies to control access to the Bastion service.

## Individual Resource-Types

`bastion`

`bastion-session`

## Aggregate Resource-Type

`bastion-family`

A policy that uses`<verb> bastion-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual bastion resource-types.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/bastionpolicyreference.htm#Details)for a detailed breakout of the API operations covered by each verb, for each individual resource-type included in`bastion-family`.

## Supported Variables

Bastion supports all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/bastionpolicyreference.htm#Details).

Variable Variable Type Comments
`target.bastion.ocid`Entity (OCID) Use this variable to control whether to allow operations against a specific bastion in response to a request to read, update, delete, or move a bastion, to view information related to work requests for a bastion, or to create a session on a bastion.
`target.bastion.name`String Use this variable to control whether to allow operations against a specific bastion in response to a request to read, update, delete, or move a bastion, to view information related to work requests for a bastion, or to create a session on a bastion.
`target.bastion-session.username`String Use this variable to target a specific operating system user name when creating a session that connects to a Compute instance.
`target.resource.ocid`Entity (OCID) Use this variable to target a specific Compute instance by its Oracle Cloud Identifier (OCID) when creating a session.

## Details for Verb + Resource-Type Combinations

The level of access is cumulative as you go from`inspect`to`read`to`use`to`manage`.

A plus sign`(+)`in a table cell indicates incremental access when compared to the preceding cell, whereas`no extra`indicates no incremental access.

For example, the`read`verb for the`bastion`resource-type includes the same permissions and API operations as the`inspect`verb, but also adds the`GetBastion`API operation. Likewise, the`manage`verb for the`bastion`resource-type allows even more permissions when compared to the`use`permission. For the`bastion`resource-type, the`manage`verb includes the same permissions and API operations as the`use`verb, plus the`BASTION_CREATE`,`BASTION_UPDATE`,`BASTION_DELETE`, and`BASTION_MOVE`permissions and a number of API operations (`CreateBastion`,`UpdateBastion`,`DeleteBastion`, and`ChangeBastionCompartment`).

[bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/bastionpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

BASTION_INSPECT

`ListBastions`

none
read

INSPECT +

BASTION_READ

INSPECT +

`GetBastion`

`ListSessions`(also needs`inspect session`)
use

READ +

BASTION_USE

no extra

`CreateSession`(also needs`manage session`,`read instances`,`read subnets`, and`read vcns`)

`UpdateSession`(also needs`manage session`)

`DeleteSession`(also needs`manage session`)
manage

USE +

BASTION_CREATE

BASTION_UPDATE

BASTION_DELETE

BASTION_MOVE

USE +

`UpdateBastion`

`ChangeBastionCompartment`

`CreateBastion`(also needs`manage vcns`,`manage subnets`,`manage route-tables`,`manage security-lists`,`manage dhcp-options`,`use network-security-groups`, and`use vnics`)

`DeleteBastion`(also needs`manage vcns`,`use private-ips`,`use vnics`,`use subnets`, and`use network-security-groups`)

[session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/bastionpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

BASTION_SESSION_INSPECT

none

`ListSessions`(also needs`read bastion`)
read

INSPECT +

BASTION_SESSION_READ

INSPECT +

`GetSession`

none
use

READ +

BASTION_SESSION_UPDATE

READ +

no extra

`UpdateSession`(also needs`use bastion`)
manage

USE +

BASTION_SESSION_CREATE

BASTION_SESSION_DELETE

USE +

no extra

`CreateSession`(also needs`use bastion`,`read instances`,`read subnets`, and`read vcns`)

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`ListBastions`BASTION_INSPECT
`GetBastion`BASTION_READ
`CreateBastion`BASTION_CREATE and VCN_CREATE
`UpdateBastion`BASTION_UPDATE
`DeleteBastion`BASTION_DELETE and VCN_DELETE
`ChangeBastionCompartment`BASTION_MOVE
`CreateSession`

BASTION_USE, INSTANCE_READ, INSTANCE_INSPECT, VCN_READ, VNIC_ATTACHMENT_READ, VNIC_READ, BASTION_SESSION_CREATE, SUBNET_READ, and INSTANCE_AGENT_PLUGIN_READ

Note: INSTANCE_AGENT_PLUGIN_READ is required only for Managed SSH sessions.
`GetSession`BASTION_SESSION_READ
`ListSessions`BASTION_READ and BASTION_SESSION_INSPECT
`UpdateSession`BASTION_USE and BASTION_SESSION_UPDATE
`DeleteSession`BASTION_USE and BASTION_SESSION_DELETE

## Policy Examples

Learn about Bastion IAM policies from examples.

To create a bastion or session, users require the following permissions for other Oracle Cloud Infrastructure resources:
- Manage networks
- Read compute instances
- Read compute instance agent (Oracle Cloud Agent) plugins
- Inspect work requests

To learn more, see[Policy Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm).

Bastion policy examples:
- 

Allow users in the group`SecurityAdmins`to create, update, and delete all Bastion resources in the entire tenancy:

```

```

- 

Allow users in the group`BastionUsers`to create, connect to, and terminate sessions in the entire tenancy:

```

```

- 

Allow users in the group`BastionUsers`to create, connect to, and terminate sessions in the compartment`SalesApps`:

```

```

The example assumes that the networks and compute instances are in the same compartment as the bastion.
- 

Allow users in the group`SalesAdmins`to create, connect to, and terminate sessions for a specific target host in the compartment`SalesApps`:

```

```

&lt;session_username&gt; is the specific operating system user name when creating a session on the Compute instance.

The example assumes that the networks and compute instances are in the same compartment as the bastion.
- 

Allow users in the group`SecurityAuditors`to view all Bastion resources in the compartment`SalesApps`:

```

```
