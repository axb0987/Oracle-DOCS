# Adding Locks to API Gateways and Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingresourcelocks.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Locks to API Gateways and Resources

Find out how to add resource locks to API gateways and related resources with API Gateway.

You can add locks to the following API Gateway resources:
- API gateways
- APIs
- API deployments
- API Gateway certificates
- SDKs
- subscribers
- usage plans

## Required IAM Policy

To add locks to API gateways and related resources, you must belong to a group to which an IAM policy has granted the`RESOURCE_LOCK_ADD`permission in addition to permissions to manage the resources, or be a tenancy administrator.

For example, the policy might contain a policy statement similar to the following:
```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingresourcelocks.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingresourcelocks.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingresourcelocks.htm#)
- 

You can't use the Console to add a lock to an API gateway or related resource. Use the CLI or API.
- 

To add a lock to a new API gateway or related resource that you are creating, use the`--locks`option with the appropriate`oci api-gateway <resource> create`command. For example:
```

```

To add a lock to an existing API gateway or related resource, use the appropriate`oci api-gateway <resource> add-lock`command. For example:
```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Use these API operations to add locks to existing API gateways and related resources:
- [AddGatewayLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/AddGatewayLock)
- [AddApiLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Api/AddApiLock)
- [AddDeploymentLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/AddDeploymentLock)
- [AddCertificateLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/AddCertificateLock)
- [AddSdkLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Sdk/AddSdkLock)
- [AddSubscriberLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Subscriber/AddSubscriberLock)
- [AddUsagePlanLock](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/UsagePlan/AddUsagePlanLock)

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
