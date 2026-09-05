# Details for Private Service Access
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/psa-policyreference.htm
- Fetched: 2026-09-05 02:27 CDT

# Details for Private Service Access

Learn the advanced details of writing policies to control access to the Oracle Cloud Infrastructure Private Service Access service.

## Resource-Types

`private-service-access`

## Supported Variables

Only the general variables are supported (see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)).

## Details for Verb + Resource-Type Combinations

### private-service-access

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

PRIVATE_SERVICE_ACCESS_INSPECT

`ListPrivateServiceAccesses`

none

read

INSPECT +

PRIVATE_SERVICE_ACCESS_READ

INSPECT +

`GetPrivateServiceAccess`

`ListPsaWorkRequests`

`ListPsaWorkRequestErrors`

`ListPsaWorkRequestLogs`

none

use

READ +

PRIVATE_SERVICE_ACCESS_UPDATE

READ +

`UpdatePrivateServiceAccess`

none

manage

USE +

PRIVATE_SERVICE_ACCESS_CREATE

PRIVATE_SERVICE_ACCESS_DELETE

PRIVATE_SERVICE_ACCESS_MOVE

USE +

`CreatePrivateServiceAccess`

`DeletePrivateServiceAccess`

`ChangePrivateServiceAccessCompartment`

none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`ListPrivateServiceAccesses`PRIVATE_SERVICE_ACCESS_INSPECT
`CreatePrivateServiceAccess`PRIVATE_SERVICE_ACCESS_CREATE
`GetPrivateServiceAccess`PRIVATE_SERVICE_ACCESS_READ
`UpdatePrivateServiceAccess`PRIVATE_SERVICE_ACCESS_UPDATE
`DeletePrivateServiceAccess`PRIVATE_SERVICE_ACCESS_DELETE
`ChangePrivateServiceAccessCompartment`PRIVATE_SERVICE_ACCESS_MOVE
`ListPsaServices`PRIVATE_SERVICE_ACCESS_INSPECT
`ListPsaWorkRequests`PRIVATE_SERVICE_ACCESS_READ
`GetPsaWorkRequest`PRIVATE_SERVICE_ACCESS_READ
`CancelPsaWorkRequest`PRIVATE_SERVICE_ACCESS_DELETE
`ListPsaWorkRequestErrors`PRIVATE_SERVICE_ACCESS_READ
`ListPsaWorkRequestLogs`
