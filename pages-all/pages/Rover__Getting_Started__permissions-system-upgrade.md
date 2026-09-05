# System Upgrade Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-system-upgrade.htm
- Fetched: 2026-09-05 02:59 CDT

# System Upgrade Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the system upgrade capability of a Roving Edge Infrastructure device.

## Resource-Types

`systemupgrade`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### systemupgrade

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

SYSTEM_UPGRADE_INSPECT

ListTasks

None

read

SYSTEM_UPGRADE_INSPECT

SYSTEM_UPGRADE_READ

ListTasks

ListSystemUpgrades

GetTask

None

use

SYSTEM_UPGRADE_INSPECT

SYSTEM_UPGRADE_READ

SYSTEM_UPGRADE_UPDATE

ListTasks

ListSystemUpgrades

GetTask

None

manage

SYSTEM_UPGRADE_INSPECT

SYSTEM_UPGRADE_READ

SYSTEM_UPGRADE_UPDATE

SYSTEM_UPGRADE_DELETE

ListTasks

ListSystemUpgrades

GetTask

NodeReboot

SystemUpgradesDownload

UpgradeNode

RollbackNode

UnlockNode

StartTask

SystemUpgradesDelete
