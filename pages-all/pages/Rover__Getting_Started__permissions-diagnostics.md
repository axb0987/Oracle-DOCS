# Diagnostics Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-diagnostics.htm
- Fetched: 2026-09-05 02:59 CDT

# Diagnostics Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the diagnostics capability of a Roving Edge Infrastructure device.

## Resource-Types

`diag-bundle`

`diag-command`

`diag-family`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### diag-bundle

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

DIAG_BUNDLE_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

None

read

DIAG_BUNDLE_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

None

use

DIAG_BUNDLE_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

None

manage

DIAG_BUNDLE_READ

DIAG_BUNDLE_CREATE

DIAG_BUNDLE_DELETE

CreateDiagBundle

ListDiagBundles

CancelDiagBundle

GetDiagBundle

ViewDiagBundleSummary

None

### diag-command

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

DIAG_COMMAND_READ

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

read

DIAG_COMMAND_READ

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

use

DIAG_COMMAND_READ

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

manage

DIAG_COMMAND_READ

DIAG_COMMAND_CREATE

DIAG_COMMAND_DELETE

CreateDiagCommand

ListDiagCommands

CancelDiagCommand

GetDiagCommand

ViewDiagCommandSummary

None

### diag-family

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

DIAG_BUNDLE_READ

DIAG_COMMAND_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

read

DIAG_BUNDLE_READ

DIAG_COMMAND_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

use

DIAG_BUNDLE_READ

DIAG_COMMAND_READ

ListDiagBundles

GetDiagBundle

ViewDiagBundleSummary

ListDiagCommands

GetDiagCommand

ViewDiagCommandSummary

None

manage

DIAG_BUNDLE_READ

DIAG_BUNDLE_CREATE

DIAG_BUNDLE_DELETE

DIAG_COMMAND_READ

DIAG_COMMAND_CREATE

DIAG_COMMAND_DELETE

CreateDiagBundle

ListDiagBundles

CancelDiagBundle

GetDiagBundle

ViewDiagBundleSummary

CreateDiagCommand

ListDiagCommands

CancelDiagCommand

GetDiagCommand

ViewDiagCommandSummary
