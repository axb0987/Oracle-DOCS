# Adding a Topic Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/add-topic-lock.htm
- Fetched: 2026-09-05 02:49 CDT

# Adding a Topic Lock

Lock a topic in Notifications to prevent updates, moves, and deletions. Locks help protect resources against tampering.

You must have`RESOURCE_LOCK_ADD, RESOURCE_LOCK_REMOVE`permissions to add a lock to a topic.
OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can[override topic locks](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/override-topic-lock.htm).

Topic locking is available using the API only.

Run the[AddTopicLock](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/AddTopicLock)
