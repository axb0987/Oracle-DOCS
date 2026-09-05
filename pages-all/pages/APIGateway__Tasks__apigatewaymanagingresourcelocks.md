# Managing Locks for API Gateways and Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymanagingresourcelocks.htm
- Fetched: 2026-09-05 01:38 CDT

# Managing Locks for API Gateways and Resources

Find out about locking API gateways and related resources, and how to add and remove resource locks with API Gateway.

Resource locking provides a consistent and standard way of protecting API gateways and related resources against tampering.

Resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource. Authorized users can read, update, and move the resource, but cannot delete it.
- Full lock: Prevents update, move, and deletion of the locked resource. Authorized users can read the resource, but cannot update, move, or delete it.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. A user with appropriate lock management permissions (`RESOURCE_LOCK_ADD`and`RESOURCE_LOCK_REMOVE`), and tenancy administrators, can create and remove any lock in the tenancy.

For more information, see:
- [Adding Locks to API Gateways and Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingresourcelocks.htm)
- [Removing Locks from API Gateways and Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm)
- [Overriding Locks on API Gateways and Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm)
