# Managing Locks for Tag Namespaces and Tag Defaults
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managing_resourcelocks.htm
- Fetched: 2026-09-05 03:06 CDT

# Managing Locks for Tag Namespaces and Tag Defaults

Resource Locking provides a consistent and standard way of protecting tag defaults and tag namespaces against tampering. An authorized user can create tag defaults or tag namespaces with a lock, or add the lock later. When the lock is applied, a lock symbol is displayed and users other than the lock owner can't retire, edit, or move the locked tag namespace to another compartment. All the tag key definitions within the locked tag namespace inherit the same lock.

Resource locks are of two types:

- Delete lock : With delete lock, authorized users can read and change the resource, but can't delete it.
- Full lock: With full lock, authorized users can't change the resource; they can only read from the resource.

The user who places a lock is displayed as the lock owner. However, any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy.

## Required IAM Policy

Users must have Administrator or manage resources to add or remove locks.
For example, to allow a serviceA to add or remove locks in service CompartmentA requires`RESOURCE_LOCK_ADD`and`RESOURCE_LOCK_REMOVE`access.
```

```

## Using the API

Use these API operations to manage locks for tag namespaces:
- [AddTagNamespaceLock](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/AddTagNamespaceLock)
- [RemoveTagNamespaceLock](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/RemoveTagNamespaceLock)

Use these API operations to manage locks for tag defaults:
- [AddTagDefaultLock](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagDefault/AddTagDefaultLock)
- [RemoveTagDefaultLock](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagDefault/RemoveTagDefaultLock)
