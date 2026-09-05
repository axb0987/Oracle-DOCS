# "Bad request" HTTP-4xx errors when creating a new API deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm
- Fetched: 2026-09-05 01:38 CDT

# "Bad request" HTTP-4xx errors when creating a new API deployment

Find out how to troubleshoot "Bad request" HTTP 4xx errors when creating API deployments with the API Gateway service.
When creating API deployments, you might encounter "Bad request" HTTP 4xx errors for several reasons:
- ["Bad request" HTTP-4xx errors related to mTLS configuration](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_Bad_request_HTTP_400_errors_mTLS)

## "Bad request" HTTP-4xx errors related to mTLS configuration

### Creating a new API deployment fails with "Cannot enable mutual TLS because custom CA Bundles are not added to the Gateway. Please add a custom CA Bundle and try again." message

When trying to create an API deployment that has mutual TLS enabled, you might see the following message:
```

```

This error occurs when a custom CA bundle has not been added to the trust store of the API gateway on which you are trying to create the API deployment.

To address this issue, edit the API gateway to add a custom CA bundle to the API gateway's trust store. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

### Creating a new API deployment fails with "Duplicate SAN or CN values passed in input" message

When trying to create an API deployment that has mutual TLS enabled, you might see the following message:
```

```

This error occurs when there are duplicate values in the list of allowed Subject Alternative Names/Common Names (SANs/CNs) specified in the API deployment's mTLS request policy. The allowed SAN/CN list cannot contain duplicate values.

To address this issue, remove the duplicate values from the allowed SAN/CN list. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

### Creating a new API deployment fails with "Too many value, must not have more than 10 values" message

When trying to create an API deployment that has mutual TLS enabled, you might see the following message:
```

```

This error occurs when there are more than 10 values in the list of allowed Subject Alternative Names/Common Names (SANs/CNs) specified in the API deployment's mTLS request policy. The allowed SAN/CN list can contain a maximum of 10 values by default (although you can change this internal limit).

To address this issue, reduce the allowed SAN/CN list to 10 or fewer values. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

### Creating a new API deployment fails with "Length of SAN or CN string should be less than 256 characters" message

When trying to create an API deployment that has mutual TLS enabled, you might see the following message:
```

```

This error occurs when there is at least one item longer than 256 characters in the list of allowed Subject Alternative Names/Common Names (SANs/CNs) specified in the API deployment's mTLS request policy. The allowed SAN/CN list cannot contain items longer than 256 characters.

To address this issue, make sure no item in the allowed SAN/CN list is longer than 256 characters. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

### Creating a new API deployment fails with "Invalid format for SAN or CN"

When trying to create an API deployment that has mutual TLS enabled, you might see the following message:
```

```

This error occurs when the values in the list of allowed Subject Alternative Names/Common Names (SANs/CNs) specified in the API deployment's mTLS request policy are not in the required format. For example, only a single character wildcard can be used as a prefix or suffix in the allowed SAN/CN list.

To address this issue, make sure all values in the allowed SAN/CN list are in the required format. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm)
