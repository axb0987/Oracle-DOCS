# Data Synchronization Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-data-sync.htm
- Fetched: 2026-09-05 02:59 CDT

# Data Synchronization Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the data synchronization capability of a Roving Edge Infrastructure device.

## Resource-Types

`datasync`

`taskdefinition`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### datasync

Sub-Component Verbs Permissions APIs Fully Covered APIs Partially Covered

datasync

inspect

DATA_SYNC_TASK_READ

getTasks

None

read

DATA_SYNC_TASK_READ

getTasks

None

use

DATA_SYNC_TASK_READ

getTasks

None

manage

DATA_SYNC_TASK_READ

DATA_SYNC_TASK_CREATE

DATA_SYNC_TASK_DELETE

createTaskgetTasks

cancelTask

None

### taskdefinition

Sub-Component Verbs Permissions APIs Fully Covered APIs Partially Covered

taskdefinition

inspect

DATA_SYNC_TASK_DEF_INSPECT

listTaskDefinitions

None

read

DATA_SYNC_TASK_DEF_INSPECT

DATA_SYNC_TASK_DEF_READ

listTaskDefinitions

getTaskDefinition

None

use

DATA_SYNC_TASK_DEF_INSPECT

DATA_SYNC_TASK_DEF_READ

DATA_SYNC_TASK_DEF_UPDATE

listTaskDefinitions

getTaskDefinition

updateTaskDefinition

None

manage

DATA_SYNC_TASK_DEF_INSPECT

DATA_SYNC_TASK_DEF_READ

DATA_SYNC_TASK_DEF_UPDATE

DATA_SYNC_TASK_DEF_CREATE

DATA_SYNC_TASK_DEF_DELETE

createTaskDefinition

deleteTaskDefinition

listTaskDefinitions

getTaskDefinition

updateTaskDefinition
