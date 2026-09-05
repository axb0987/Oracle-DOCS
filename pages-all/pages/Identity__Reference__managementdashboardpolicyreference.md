# Details for Management Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/managementdashboardpolicyreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for Management Dashboards

Write policies to control access to Management Dashboards.

## Resource-Types

### Individual Resource-Types

`management-dashboard`

`management-saved-search`

### Aggregate Resource-Type

`management-dashboard-family`

### Comments

A policy that uses`<verb> management-dashboard-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual resource-types. The resource-type`management-dashboard`allows a user group to work with dashboards while the resource-type`management-saved-search`allows a user group to work with saved searches (widgets) that are displayed in dashboards.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/managementdashboardpolicyreference.htm#details)for details of the API operations covered by each verb, for each individual resource-type included in`management-dashboard-family`.

## Supported Variables

Only the general variables are supported (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[management-dashboard](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/managementdashboardpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

MANAGEMENT_DASHBOARD_INSPECT

`GetManagementDashboard`

`ListManagementDashboards`

none
read

INSPECT +

MANAGEMENT_DASHBOARD_READ`ExportDashboard`

none
use

READ +

MANAGEMENT_DASHBOARD_UPDATE

`UpdateManagementDashboard`

none
manage

USE +

MANAGEMENT_DASHBOARD_CREATE

MANAGEMENT_DASHBOARD_DELETE

MANAGEMENT_DASHBOARD_MOVE

`ChangeManagementDashboardsCompartment`

`CreateManagementDashboard`

`DeleteManagementDashboard`

`ImportDashboard`

none

[management-saved-search](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/managementdashboardpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

MANAGEMENT_SAVED_SEARCH_INSPECT

`GetManagementSavedSearch`

`ListManagementSavedSearches`

none
read

INSPECT +

MANAGEMENT_SAVED_SEARCH_READ

no extra

none
use

READ +

MANAGEMENT_SAVED_SEARCH_UPDATE

`UpdateManagementSavedSearch`

none
manage

USE +

MANAGEMENT_SAVED_SEARCH_CREATE

MANAGEMENT_SAVED_SEARCH_DELETE

MANAGEMENT_SAVED_SEARCH_MOVE

`ChangeManagementSavedSearchesCompartment`

`CreateManagementSavedSearch`

`DeleteManagementSavedSearch`

none

## Permissions Required for Each API Operation

The following table lists the API operations in alphabetical order.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
ChangeManagementDashboardsCompartment MANAGEMENT_DASHBOARD_MOVE
ChangeManagementSavedSearchesCompartment MANAGEMENT_SAVED_SEARCH_MOVE
CreateManagementDashboard MANAGEMENT_DASHBOARD_CREATE
CreateManagementSavedSearch MANAGEMENT_SAVED_SEARCH_CREATE
DeleteManagementDashboard MANAGEMENT_DASHBOARD_DELETE
DeleteManagementSavedSearch MANAGEMENT_SAVED_SEARCH_DELETE
ExportDashboard MANAGEMENT_DASHBOARD_READ
GetManagementDashboard MANAGEMENT_DASHBOARD_INSPECT
GetManagementSavedSearch MANAGEMENT_SAVED_SEARCH_INSPECT
ImportDashboard MANAGEMENT_DASHBOARD_CREATE
ListManagementDashboards MANAGEMENT_DASHBOARD_INSPECT
ListManagementSavedSearches MANAGEMENT_SAVED_SEARCH_INSPECT
UpdateManagementDashboard MANAGEMENT_DASHBOARD_UPDATE
UpdateManagementSavedSearch MANAGEMENT_SAVED_SEARCH_UPDATE

## Example Policies

This section provides example policies for use with Management Dashboards.

### Dashboard Policies

Here are examples of policy statements that authorize access to dashboards (`management-dashboard`resource-type):
- 

To allow a user group to list the dashboards in a compartment, use the`inspect`verb:
```

```

- 

To allow a user group to list dashboards and obtain details regarding the dashboards in a compartment, use the`read`verb:
```

```

- 

To allow a group of administrators to list dashboards, obtain details regarding dashboards, and update the dashboards in a compartment, use the`use`verb:
```

```

- 

To allow a group of administrators to list dashboards, obtain details regarding dashboards, update dashboards, and manage (create, move, and delete) the dashboards in a compartment, use the`manage`verb:
```

```

### Saved Search Policies

Here are examples of policy statements that authorize access to saved searches (`management-saved-search`resource-type):
- 

To allow a user group to list the saved searches in a compartment, use the`inspect`verb:
```

```

- 

To allow a user group to list saved searches and obtain details regarding the saved searches in a compartment, use the`read`verb:
```

```

- 

To allow a group of administrators to list saved searches, obtain details regarding saved searches, update the saved searches in a compartment, use the`use`verb:
```

```

- 

To allow a group of administrators to list saved searches, obtain details regarding saved searches, update saved searches, and manage (create, move, and delete) the saved searches in a compartment, use the`manage`verb:
```

```

### Aggregate Policies

Here's an example of a policy that simultaneously authorizes access to both dashboards and saved searches by using the aggregate`management-dashboard-family`resource-type. In this example, the`inspect`verb is used to allow a user group to list both the dashboards and saved searches in a compartment:
```

```
