# Policy Details for Console Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Reference/dashboardspolicyreference.htm
- Fetched: 2026-09-05 01:59 CDT

# Policy Details for Console Dashboards

You can write policies to control access to the Console Dashboards service.

## Resource-Types

`dashboards`

`dashboard-groups`

`dashboards-family`

## Supported Variables

The Console Dashboards service supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Reference/dashboardspolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

DASHBOARD_INSPECT

none

`ListDashboards`

Also need`read dashboard-groups`.
read

INSPECT +

DASHBOARD_READ

none

INSPECT +

`GetDashboard`

Also need`read dashboard-groups`.
use

READ +

DASHBOARD_UPDATE

none

READ +

`UpdateDashboard`

Also need`read dashboard-groups`.
manage

USE +

DASHBOARD_CREATE

DASHBOARD_DELETE

none

USE +

`CreateDashboard`

`DeleteDashboard`

Also need`read dashboard-groups`.

[dashboard-groups](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Reference/dashboardspolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

DASHBOARD_GROUP_INSPECT

`ListDashboardGroups`

none
read

INSPECT +

DASHBOARD_GROUP_READ

INSPECT +

`GetDashboardGroup`

none
use

READ +

DASHBOARD_GROUP_UPDATE

READ +

`UpdateDashboardGroup`

none
manage

USE +

DASHBOARD_GROUP_CREATE

DASHBOARD_GROUP_DELETE

USE +

`CreateDashboardGroup`

`DeleteDashboardGroup`

none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm).

API Operation Permissions Required to Use the Operation
`ListDashboards`DASHBOARD_INSPECT and DASHBOARD_GROUP_READ
`GetDashboard`DASHBOARD_READ and DASHBOARD_GROUP_READ
`CreateDashboard`DASHBOARD_CREATE and DASHBOARD_GROUP_READ
`UpdateDashboard`DASHBOARD_UPDATE and DASHBOARD_GROUP_READ
`DeleteDashboard`DASHBOARD_DELETE and DASHBOARD_GROUP_READ
`ListDashboardGroups`DASHBOARD_GROUP_INSPECT
`GetDashboardGroup`DASHBOARD_GROUP_READ
`CreateDashboardGroup`DASHBOARD_GROUP_CREATE
`UpdateDashboardGroup`DASHBOARD_GROUP_UPDATE
`DeleteDashboardGroup`
