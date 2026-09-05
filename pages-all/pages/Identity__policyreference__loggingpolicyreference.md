# Details for Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/loggingpolicyreference.htm
- Fetched: 2026-09-05 02:26 CDT

# Details for Logging

This topic covers details for writing policies to control access to Logging.

## Resource-Types

Aggregate Resource-Type
- `logging-family`

Individual Resource-Types
- `log-groups`
- `log-content`
- `unified-configuration`

### Comments

A policy that uses`<verb> logs`is equivalent to writing one with a separate &lt;verb&gt; &lt;individual resource-type&gt; statement for each of the individual resource-types.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/loggingpolicyreference.htm#loggingpolicyreference_details_for_verb_resource_type_combinations)for a detailed breakout of the API operations covered by each verb, for each individual resource-type included in`logs`.

## Supported Variables

Logging supports all the general variables (see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)), plus additional ones listed here:

Operations for This Resource-Type... Can Use These Variables... Variable Type Comments
`log-groups``target.loggroup.id`Entity (OCID)
`log-content``target.loggroup.id`Entity (OCID)

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

For example, the`read`verb for the`log-groups`resource-type includes the same permissions and API operations as the`inspect`verb, plus the LOG_GROUPS_READ permission and the corresponding API operations`GetLog`and`GetLogGroup`.

[log-groups](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/loggingpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT

LOG_GROUP_INSPECT

`ListLogGroups`

`ListLogs`

none
READ

INSPECT +

LOG_GROUP_READ

INSPECT +

`GetLogGroup`

`GetLog`

`ListSearchLogs`none
USE

READ +

LOG_GROUP_UPDATE

READ +

`UpdateLogGroup`

`ChangeLogGroupCompartment`

`UpdateLog`none
MANAGE

USE +

LOG_GROUP_CREATE

LOG_GROUP_DELETE

USE +

`CreateLogGroup`

`DeleteLogGroup`

`CreateLog`

`DeleteLog`none

[log-content](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/loggingpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT none none

none
READ

INSPECT +

LOG_CONTENT_READ

INSPECT +

`ListSearchLogs`none
USE

READ +

LOG_CONTENT_PUSH

UNIFIED_AGENT_CONFIG_GENERATE none none
MANAGE

READ +

LOG_CONTENT_PUSH

UNIFIED_AGENT_CONFIG_GENERATE none none

[unified-configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/loggingpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT UNIFIED_AGENT_CONFIG_INSPECT`ListUnifiedAgentConfiguration`

none
READ

INSPECT +

UNIFIED_AGENT_CONFIG_READ

INSPECT +

`GetUnifiedAgentConfiguration`none
USE

READ +

UNIFIED_AGENT_CONFIG_UPDATE

READ +

`UpdateUnifiedAgentConfiguration`none
MANAGE USE +

UNIFIED_AGENT_CONFIG_CREATE

UNIFIED_AGENT_CONFIG_DELETE

USE +

`CreateUnifiedAgentConfiguration`

`DeleteUnifiedAgentConfiguration`none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../policies/permissions.htm).

API Operation Permissions Required to Use the Operation
`ListSearchLogs`LOG_CONTENT_READ
`ListLogs`LOG_GROUP_INSPECT
`GetLog`LOG_GROUP_READ
`UpdateLog`LOG_GROUP_UPDATE
`CreateLog`LOG_GROUP_CREATE
`DeleteLog`LOG_GROUP_DELETE
`ListLogGroups`LOG_GROUP_INSPECT
`GetLogGroup`LOG_GROUP_READ
`UpdateLogGroup`LOG_GROUP_UPDATE
`CreateLogGroup`LOG_GROUP_CREATE
`DeleteLogGroup`LOG_GROUP_DELETE
`ChangeLogGroupCompartment`LOG_GROUP_UPDATE
`CreateUnifiedAgentConfiguration`UNIFIED_AGENT_CONFIG_CREATE
`GetUnifiedAgentConfiguration`UNIFIED_AGENT_CONFIG_READ
`UpdateUnifiedAgentConfiguration`UNIFIED_AGENT_CONFIG_UPDATE
`DeleteUnifiedAgentConfiguration`UNIFIED_AGENT_CONFIG_DELETE
`ListUnifiedAgentConfigurations`
