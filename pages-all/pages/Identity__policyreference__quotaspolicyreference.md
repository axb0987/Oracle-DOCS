# Details for the Quotas Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/quotaspolicyreference.htm
- Fetched: 2026-09-05 02:27 CDT

# Details for the Quotas Service

This topic covers details for writing policies to control access to the Quotas service.

## Resource-Types

`quota`

## Supported Variables

The Quotas service supports all the general variables (see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)) plus the following:

Variable Variable Type Source
`target.quota.id`Entity (OCID) Request
`target.quota.name`String Request/Stored

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[quotas](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/quotaspolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

QUOTA_INSPECT`listQuotas`

none
read

INSPECT +

QUOTA_READ

`getQuota`

none
use

no extra

no extra

none
manage

USE +

QUOTA_CREATE

QUOTA_DELETE

QUOTA_UPDATE

`createQuota`

`deleteQuota`

`updateQuota`

none

## Permissions Required for Each API Operation

API Operation Permissions Required to Use the Operation
`listQuotas`QUOTA_INSPECT
`createQuota`QUOTA_CREATE
`getQuota`QUOTA_READ
`deleteQuota`QUOTA_DELETE
`updateQuota`
