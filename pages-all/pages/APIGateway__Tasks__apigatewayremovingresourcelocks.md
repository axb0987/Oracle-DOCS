# Removing Locks from API Gateways and Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm
- Fetched: 2026-09-05 01:38 CDT

# Removing Locks from API Gateways and Resources

Find out how to remove resource locks from API gateways and related resources with API Gateway.

You can remove locks that have been added to API gateways and related resources to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

Note that you can also temporarily override locks (see[Overriding Locks on API Gateways and Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayoverridingresourcelocks.htm)).

## Required IAM Policy

To remove locks from API gateways and related resources, you must belong to a group to which an IAM policy has granted the`RESOURCE_LOCK_REMOVE`permission in addition to permissions to manage the resources, or be a tenancy administrator.

For example, the policy might contain a policy statement similar to the following:
```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayremovingresourcelocks.htm#)
- 

You can't use the Console to remove a lock from an API gateway or related resource. Use the CLI or API.
- 

To remove a lock from an existing API gateway or related resource, use the appropriate`oci api-gateway <resource> remove-lock`command. For example:
```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Use these API operations to remove locks from existing API gateways and related resources:
- [RemoveGatewayLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/RemoveGatewayLock)
- [RemoveApiLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Api/RemoveApiLock)
- [RemoveDeploymentLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/RemoveDeploymentLock)
- [RemoveCertificateLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/RemoveCertificateLock)
- [RemoveSdkLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/RemoveSdkLock)
- [RemoveSubscriberLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Subscriber/RemoveSubscriberLock)
- [RemoveUsagePlanLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/UsagePlan/RemoveUsagePlanLock)

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
