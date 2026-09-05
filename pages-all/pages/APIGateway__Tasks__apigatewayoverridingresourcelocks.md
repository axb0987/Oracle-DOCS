# Overriding Locks on API Gateways and Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm
- Fetched: 2026-09-05 01:38 CDT

# Overriding Locks on API Gateways and Resources

Find out how to override resource locks on API gateways and related resources with API Gateway.

You can temporarily override locks on API gateways and related resources when performing an action such as an update, move, or deletion.

Note that you can also permanently remove locks (see[Removing Locks from API Gateways and Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm)).

## Required IAM Policy

To override locks on API gateways and related resources, you must belong to a group to which an IAM policy has granted the necessary lock management permissions in addition to permissions to manage the resources, or be a tenancy administrator.

The lock management permissions you require depend on the operation to perform, and the type of lock to override:
- 

To update an API gateway or related resource and override a full lock, you must have both`RESOURCE_LOCK_REMOVE`and`RESOURCE_LOCK_ADD`permissions. For example, the policy might contain a policy statement similar to the following:
```

```

- To delete an API gateway or related resource and override a full lock or delete lock, you must have both`RESOURCE_LOCK_REMOVE`and`RESOURCE_LOCK_ADD`permissions.
- To move an API gateway or related resource and override a full lock, you must have`RESOURCE_LOCK_REMOVE`permission in the source compartment and`RESOURCE_LOCK_ADD`in the target compartment. Note that you can move an API gateway or related resource to which a delete lock has been applied, without additional lock management permissions, and without overriding the delete lock.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm#)
- 

You can't use the Console to override locks on an API gateway or related resource. Use the CLI or API.
- 

To override a full or delete lock on an API gateway or related resource, use the`--is-lock-override true`option with the required`oci api-gateway <resource>`command. For example:
- To update an SDK resource and override a full lock:
```

```

- To delete an SDK resource and override a delete lock or a full lock:
```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

To override a full lock or delete lock on an existing API gateway or related resource, use the appropriate operation and include the`isLockOverride`parameter set to`true`.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
