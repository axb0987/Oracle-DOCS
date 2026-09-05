# Events Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-events.htm
- Fetched: 2026-09-05 02:59 CDT

# Events Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the Events service for a Roving Edge Infrastructure device.

## Resource-Types

`cloudevents-rules`

`cloudevents-family`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### cloudevents-rules

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

EVENTRULE_LIST

ListRules

ListSchemas

None

read

EVENTRULE_LIST

EVENTRULE_READ

ListRules

ListSchemas

GetRule

None

use

EVENTRULE_LIST

EVENTRULE_READ

ListRules

ListSchemas

GetRule

None

manage

EVENTRULE_LIST

EVENTRULE_READ

EVENTRULE_MODIFY

EVENTRULE_CREATE

EVENTRULE_DELETE

ListRules

ListSchemas

GetRule

ChangeRuleCompartment

UpdateRule

CreateRule

DeleteRule

None

### cloudevents-family

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

EVENTRULE_LIST

ListRules

ListSchemas

None

read

EVENTRULE_LIST

EVENTRULE_READ

ListRules

ListSchemas

GetRule

None

use

EVENTRULE_LIST

EVENTRULE_READ

EVENT_CONSUME

ListRules

ListSchemas

GetRule

None

manage

EVENTRULE_LIST

EVENTRULE_READ

EVENTRULE_MODIFY

EVENTRULE_CREATE

EVENTRULE_DELETE

EVENT_CONSUME

EVENT_PUBLISH

ListRules

ListSchemas

GetRule

ChangeRuleCompartment

UpdateRule

CreateRule

DeleteRule
