# Overriding a Topic Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/override-topic-lock.htm
- Fetched: 2026-09-05 02:49 CDT

# Overriding a Topic Lock

Override the lock for a topic in Notifications when performing some action on the topic, such as an update, move, or deletion.

You must have`RESOURCE_LOCK_ADD, RESOURCE_LOCK_REMOVE`permissions to override a topic lock when performing some action on the topic.

Overriding a topic lock is available using the API only.

Run the operation specific to the action you want to perform on the topic, and set`isLockOverride`to`true`.

Example request for overriding a lock when updating a topic:
```

```
