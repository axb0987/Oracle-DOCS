# Details for Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/notificationpolicyreference.htm
- Fetched: 2026-09-05 02:26 CDT

# Details for Notifications

Write policies to control access to the Notifications service.

## Resource-Types

### Aggregate Resource-Type

`ons-family`

The`ons-family`aggregate resource-type covers these individual resource-types:
- `ons-topics`
- `ons-subscriptions`

### Individual Resource-Types

`ons-topics`

`ons-subscriptions`

## Supported Variables

Only the general variables are supported (see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[ons-topics](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/notificationpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

ONS_TOPIC_INSPECT`ListTopics`

none
read

INSPECT +

ONS_TOPIC_READ`GetTopic`

none
use

READ +

ONS_TOPIC_PUBLISH

ONS_TOPIC_SUBSCRIBE

`CreateSubscription`

`UpdateSubscription`

`DeleteSubscription`

`GetSubscription`

`ResendSubscriptionConfirmation`

`PublishMessage`

none
manage

USE +

ONS_TOPIC_CREATE

ONS_TOPIC_MOVE

ONS_TOPIC_UPDATE

ONS_TOPIC_DELETE

`CreateTopic`

`ChangeTopicCompartment`

`UpdateTopic`

`DeleteTopic`

none

[ons-subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/notificationpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

ONS_SUBSCRIPTION_INSPECT`ListSubscriptions`

none
read

INSPECT +

no extra

no extra

none
use

READ +

no extra

no extra

none
manage

USE +

ONS_SUBSCRIPTION_MOVE

ONS_TOPIC_SUBSCRIBE

`ChangeSubscriptionCompartment`

`CreateSubscription`

`UpdateSubscription`

`DeleteSubscription`

`GetSubscription`

`ResendSubscriptionConfirmation`

none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../policies/permissions.htm).

API Operation Permissions Required to Use the Operation
`ListTopics`ONS_TOPIC_INSPECT
`GetTopic`ONS_TOPIC_READ
`CreateTopic`ONS_TOPIC_CREATE
`ChangeTopicCompartment`ONS_TOPIC_MOVE
`UpdateTopic`ONS_TOPIC_UPDATE
`AddTopicLock`RESOURCE_LOCK_ADD
`RemoveTopicLock`RESOURCE_LOCK_REMOVE
`DeleteTopic`ONS_TOPIC_DELETE
`ListSubscriptions`ONS_SUBSCRIPTION_INSPECT
`CreateSubscription`ONS_TOPIC_SUBSCRIBE
`ChangeSubscriptionCompartment`ONS_SUBSCRIPTION_MOVE
`UpdateSubscription`ONS_TOPIC_SUBSCRIBE
`DeleteSubscription`ONS_TOPIC_SUBSCRIBE
`GetSubscription`ONS_TOPIC_SUBSCRIBE
`GetConfirmSubscription`(no permissions required)
`ResendSubscriptionConfirmation`ONS_TOPIC_SUBSCRIBE
`GetUnsubscription`(no permissions required)
`PublishMessage`
