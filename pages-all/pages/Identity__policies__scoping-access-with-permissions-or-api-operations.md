# Scoping Access with Permissions or API Operations
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-access-with-permissions-or-api-operations.htm
- Fetched: 2026-09-05 02:25 CDT

# Scoping Access with Permissions or API Operations

In a policy statement, you can use Conditions combined with permissions or API operations to reduce the scope of access granted by a particular verb.

For example, let's say you want group XYZ to list, get, create, or update groups (change their description), but not delete them. To list, get, create, and update groups, you need a policy with`manage groups`as the verb and resource-type. According to the table in[Details for Verbs + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/../policyreference/iampolicyreference.htm#Identity), the permissions covered are:
- GROUP_INSPECT
- GROUP_UPDATE
- GROUP_CREATE
- GROUP_DELETE

To restrict access to only the required permissions, you could add a condition that explicitly states the permissions you want to allow :

```

```

An alternative would be a policy that allows all permissions except GROUP_DELETE:

```

```

However, with this approach, be aware that any new permissions the service might add in the future would automatically be granted to group XYZ. Only GROUP_DELETE would be omitted.

Another alternative would be to write a condition based on the specific API operations . Notice that according to the table in[Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/../policyreference/iampolicyreference.htm#Details), both`ListGroups`and`GetGroup`require only the GROUP_INSPECT permission. Here's the policy:

```

```

It can be beneficial to use permissions instead of API operations in conditions. In the future, if a new API operation is added that requires one of the permissions listed in the permissions-based policy above, that policy will already control XYZ group's access to that new API operation.

But notice that you can further scope a user's access to a permission by also specifying a condition based on API operation. For example, you could give a user access to GROUP_INSPECT, but then only to`ListGroups`.

```

```
