# Details for License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/licensemanagerpolicyreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for License Manager

This topic covers details for writing policies to control access to the License Manager.

## Resource-Types

Individual Resource-Types
- `licensemanager-record`
- `licensemanager-settings`

## Supported Variables

License Manager supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus additional ones listed here:

Required variables (supplied by service for every request):

Variable Variable Type Comments
`target.resource.kind`String The resource kind name of the primary resource for the request.

Automatic Variables (supplied by the SDK for every request):

Variable Variable Type Comments
`target.tenant.id`Entity (OCID) The OCID of the target tenant ID.

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[licensemanager-settings](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/licensemanagerpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT LICENSE_MANAGER_SETTINGS_INSPECT`ListSettings`

none
READ

INSPECT + LICENSE_MANAGER_SETTINGS_READ

INSPECT +`GetSettings`none
USE

READ + LICENSE_MANAGER_SETTINGS_UPDATE

READ +`UpdateSettings`none
MANAGE

USE + LICENSE_MANAGER_SETTINGS_CREATE

LICENSE_MANAGER_SETTINGS_DELETE

USE +`CreateSettings`

`DeleteSettings`none

[licensemanager-record](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/licensemanagerpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT LICENSE_MANAGER_RECORD_INSPECT`ListLicenses`

none
READ

INSPECT + LICENSE_MANAGER_RECORD_READ

INSPECT +`GetLicense`none
USE

READ + LICENSE_MANAGER_RECORD_UPDATE

READ +`UpdateLicense`none
MANAGE

USE + LICENSE_MANAGER_RECORD_CREATE

LICENSE_MANAGER_RECORD_DELETE

LICENSE_MANAGER_RECORD_MOVE

USE +`CreateLicense`

`DeleteLicense`

`MoveLicense`none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
CreateLicense LICENSE_MANAGER_RECORD_CREATE
ListLicenses LICENSE_MANAGER_RECORD_INSPECT
GetLicense LICENSE_MANAGER_RECORD_READ
UpdateLicense LICENSE_MANAGER_RECORD_UPDATE
MoveLicense LICENSE_MANAGER_RECORD_MOVE
DeleteLicense LICENSE_MANAGER_RECORD_DELETE
CreateSettings LICENSE_MANAGER_SETTINGS_CREATE
UpdateSettings LICENSE_MANAGER_SETTINGS_UPDATE
ListSettings LICENSE_MANAGER_SETTINGS_INSPECT
GetSettings LICENSE_MANAGER_SETTINGS_READ
