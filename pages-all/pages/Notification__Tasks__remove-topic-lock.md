# Removing a Topic Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/remove-topic-lock.htm
- Fetched: 2026-09-05 02:49 CDT

# Removing a Topic Lock

Unlock a topic in Notifications to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You must have`RESOURCE_LOCK_ADD, RESOURCE_LOCK_REMOVE`permissions to remove a lock from a topic.

Topic unlocking is available using the API only.

Run the[RemoveTopicLock](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/RemoveTopicLock)
