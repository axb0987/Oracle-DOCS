# Creating Cloud Advisor policies
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Reference/cloudadvisorpolicyreference.htm
- Fetched: 2026-09-05 01:47 CDT

# Creating Cloud Advisor policies

This section describes the advanced details of writing policies for Cloud Advisor. Use policies to control access to Cloud Advisor.

## Resource-Types

`optimizer-api-family`

`optimizer-category`

`optimizer-enrollment`

`optimizer-history`

`optimizer-profile`

`optimizer-profile-level`

`optimizer-recommendation`

`optimizer-recommendation-strategy`

`optimizer-resource-action`

`optimizer-resource-metadata`

`optimizer-workrequest`

## Supported Variables

Cloud Advisor supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the variables listed in the following table:

Operations for this resource-type... Can Use These Variables... Variable Type Comments
`recommendation``target.recommendation.name`String Available for ListHistories, ListResourceActions, and GetResourceAction
r`esource-type``target.resource.type`String Available for ListHistories, ListResourceActions, and GetResourceAction

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

### optimizer-category

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_CATEGORY_INSPECT

`ListCategories`

none
read

INSPECT +

OPTIMIZER_CATEGORY_READ

INSPECT +

`GetCategory`

none
use

no extra

no extra

none
manage

no extra

no extra

none

### optimizer-enrollment

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_ENROLLMENT_INSPECT

`ListEnrollmentStatuses`

none
read

INSPECT +

OPTIMIZER_ENROLLMENT_READ

INSPECT +

`GetEnrollmentStatus`

none
use

READ +

OPTIMIZER_ENROLLMENT_UPDATE

READ +

`UpdateEnrollmentStatus`

none
manage

no extra

no extra

none

### optimizer-history

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_HISTORY_INSPECT

no extra ListHistories

( optimizer-resource-metadata )
read

no extra

no extra

none
use

no extra

no extra

none
manage

no extra

no extra

none

### optimizer-profile

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_PROFILE_INSPECT

`ListProfiles`

none
read

INSPECT +

OPTIMIZER_PROFILE_READ

INSPECT +

`GetProfile`

none
use

READ +

OPTIMIZER_PROFILE_UPDATE

READ +

`UpdateProfile`

none
manage

USE +

OPTIMIZER_PROFILE_CREATE

OPTIMIZER_PROFILE_DELETE

USE +

`CreateProfile`

`DeleteProfile`

none

### optimizer-profile-level

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_PROFILE_LEVEL_INSPECT

`ListProfileLevels`

none
read

no extra

no extra

none
use

no extra

no extra

none
manage

no extra

no extra

none

### optimizer-recommendation

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_RECOMMENDATION_INSPECT

`ListRecommendations`

none
read

INSPECT +

OPTIMIZER_RECOMMENDATION_READ

INSPECT +

`GetRecommendation`

none
use

READ +

OPTIMIZER_RECOMMENDATION_UPDATE

READ +

`UpdateRecommendation`

none
manage

no extra

no extra

none

### optimizer-recommendation-strategy

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_RECOMMENDATION_STRATEGY_INSPECT

`ListRecommendationStrategies`

none
read

no extra

no extra

none
use

no extra

no extra

none
manage

no extra

no extra

none

### optimizer-resource-action

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect OPTIMIZER_RESOURCE_ACTION_INSPECT

`ListResourceActionQueryableFields``ListResourceActions`

(optimizer-resource-metadata)
read

INSPECT +

OPTIMIZER_RESOURCE_ACTION_READ

INSPECT +

no extra

`GetResourceActions`

(optimizer-resource-metadata)
use

READ +

OPTIMIZER_RESOURCE_ACTION_UPDATE

READ +

`UpdateResourceAction`

`BulkApplyRecommendations`

none

READ + no extra
manage no extra no extra

none no extra

### optimizer-resource-metadata

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect OPTIMIZER_RESOURCE_METADATA_INSPECT None None
read

OPTIMIZER_RESOURCE_METADATA_READ None`ListResourceActions, ListHistories, GetResourceAction`
use

READ +

OPTIMIZER_RESOURCE_METADATA_UPDATE None None

no extra
manage OPTIMIZER_RESOURCE_METADATA_MANAGE None no extra

### optimizer-workrequest

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OPTIMIZER_WORKREQUEST_INSPECT

`ListWorkRequestLogs`

`ListWorkRequestErrors`

`ListWorkRequests`

none
read

INSPECT +

OPTIMIZER_WORKREQUEST_READ

INSPECT +

`GetWorkRequest`

none
use

no extra

no extra

none
manage

no extra

no extra

none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`GetCategory`OPTIMIZER_CATEGORY_READ
`ListCategories`OPTIMIZER_CATEGORY_INSPECT
`GetEnrollmentStatus`OPTIMIZER_ENROLLMENT_READ
`UpdateEnrollmentStatus`OPTIMIZER_ENROLLMENT_UPDATE
`ListEnrollmentStatuses`OPTIMIZER_ENROLLMENT_INSPECT
`ListHistories`OPTIMIZER_HISTORY_INSPECT
`CreateProfile`OPTIMIZER_PROFILE_CREATE
`GetProfile`OPTIMIZER_PROFILE_READ
`ListProfiles`OPTIMIZER_PROFILE_INSPECT
`UpdateProfile`OPTIMIZER_PROFILE_UPDATE
`DeleteProfile`OPTIMIZER_PROFILE_DELETE
`GetRecommendation`OPTIMIZER_RECOMMENDATION_READ
`ListRecommendations`OPTIMIZER_RECOMMENDATION_INSPECT
`UpdateRecommendation`OPTIMIZER_RECOMMENDATION_UPDATE
`ListRecommendationStrategies`OPTIMIZER_RECOMMENDATION_STRATEGY_INSPECT
`GetResourceAction`OPTIMIZER_RESOURCE_ACTION_READ
`UpdateResourceAction`OPTIMIZER_RESOURCE_ACTION_UPDATE
`FilterResourceActions`OPTIMIZER_RESOURCE_ACTION_INSPECT
`ListResourceActionQueryableFields`OPTIMIZER_RESOURCE_ACTION_INSPECT
`BulkApplyRecommendations`OPTIMIZER_RESOURCE_ACTION_UPDATE
`ListResourceActions`OPTIMIZER_RESOURCE_ACTION_INSPECT
`ListProfileLevels`OPTIMIZER_PROFILE_LEVEL_INSPECT
`GetWorkRequest`OPTIMIZER_WORKREQUEST_READ
`ListWorkRequests`OPTIMIZER_WORKREQUEST_INSPECT
`ListWorkRequestErrors`OPTIMIZER_WORKREQUEST_INSPECT
`ListWorkRequestLogs`
