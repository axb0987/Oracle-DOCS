# Gateway or deployment create or update fails because of missing IAM policies or inaccessible related resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-gateway_create_or_update_fails.htm
- Fetched: 2026-09-05 01:39 CDT

# Gateway or deployment create or update fails because of missing IAM policies or inaccessible related resources

Find out how to troubleshoot gateway create and update failures caused by missing IAM policies or inaccessible related resources when using the API Gateway service.

A request to create or update a gateway or deployment can fail even when the request body is valid. The failure can occur because the caller, the gateway, or a referenced resource does not satisfy the tenancy, compartment, tag, or related-resource prerequisites.

## Before You Troubleshoot

Review the following topics before you update policies or related resources:
- 

[Preparing for API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayprerequisites.htm)
- 

[Configuring Your Tenancy for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Tasks/apigatewayconfiguringtenancies.htm)
- 

[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Tasks/apigatewaycreatingpolicies.htm)
- 

[Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Tasks/apigatewaycreatingcompartment.htm)
- 

[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Tasks/apigatewaycreatinggateway.htm)

## Issue Symptoms

You might see one or more of the following symptoms:
- 

Gateway creation or update fails even though the request body is valid.
- 

Deployment creation or update fails even though the target gateway exists.
- 

The response includes`NotAuthorizedOrNotFound`.
- 

The response includes`RelatedResourceNotAuthorizedOrNotFound`.
- 

The caller has some API Gateway permissions, but the operation still fails.
- 

The request uses tag-based IAM conditions, and authorization still fails.

## Possible Causes

Create and update operations can require more than the policy that permits access to API Gateway resources. The caller must also have access to each related resource that the request uses.

Common causes include the following issues:
- 

The caller lacks`manage api-gateway-family`in the compartment that contains the gateway or deployment.
- 

The caller lacks`manage virtual-network-family`in the compartment that contains the subnet or related network resources.
- 

The deployment uses a feature, such as functions, certificates, certificate authorities, or vault secrets, but the required feature-specific policy is missing.
- 

The request references a resource in a compartment that is outside the policy scope.
- 

A tag-based IAM condition does not match the target resource or related resource.
- 

The request uses an incorrect Oracle Cloud Identifier (OCID) for the gateway, subnet, certificate, secret, or another related resource.

## Review Required Policies

Start by confirming that the caller has the core policies that apply to the most common HTTP back-end deployment scenario.

For gateways and deployments that use HTTP back-end services, the caller typically needs the following policies:
```

```

```

```

These policies cover only the common case. If the gateway or deployment uses additional features, add the policy that matches each feature.

Use the following feature-specific policies as a starting point:
- 

For a deployment that uses OCI Functions as a back-end service, grant access to the functions resources:
```

```

- 

For a custom domain that uses a Certificates service certificate, grant access to certificate associations:
```

```

- 

For custom certificate authorities (CAs) or CA bundles in a gateway trust store, grant access to certificate authority resources:
```

```

- 

For response-cache credentials or authentication-provider credentials stored in vaults in the Vault service, create a dynamic group for the gateway and grant the gateway access to read the secret bundle:
```

```

- 

For access to a specific secret, use a policy that limits access to that secret OCID:
```

```

## Review the Error Response

Use the failed response to identify which operation failed and which authorization error was returned.

Record the following response fields:
- 

`operation_name`
- 

`status`
- 

`code`
- 

`opc-request-id`

For this issue, a typical failed response includes the following values:
- 

`operation_name: create_deployment`
- 

`status: 404`
- 

`code: NotAuthorizedOrNotFound`

Keep the`opc-request-id`value so that you can correlate the failed request with diagnostics and support data.

## Review IAM Policy Scope

Match the failed operation to the policy scope that the operation requires.

For gateway create or update operations, verify the following requirements:
- 

The caller can manage API Gateway resources in the compartment that contains the gateway.
- 

The caller can manage network resources in the compartment that contains the subnet and related network resources.

For deployment create or update operations, verify the following requirements:
- 

The caller can manage API Gateway resources in the compartment that contains the deployment.
- 

The caller has each feature-specific policy required by the deployment configuration.

If the request uses a custom domain, CA bundle, vault secret, or Functions back end, verify the corresponding feature-specific policy.

## Review Compartments and Related Resources

A request can fail even when the main API Gateway policy exists. The failure can occur when a related resource is missing, inaccessible, or outside the policy scope.

Verify that the caller can access the following resources, as applicable:
- 

The target gateway.
- 

The target deployment compartment.
- 

The subnet referenced by the gateway.
- 

Any certificate resource.
- 

Any CA bundle or CA resource.
- 

Any Functions back-end service.
- 

Any vault secret required by the gateway or deployment flow.

Verify that each resource is in a compartment that the relevant policy covers.

## Review Tag-Based Policy Conditions

If the tenancy uses IAM conditions based on tags, confirm that the tag condition matches the caller and each target resource.

Typical tag-related failure points include the following issues:
- 

The request principal group tag does not match the target resource tag.
- 

The target resource tag value does not match the policy expression.
- 

The resource exists, but the tag condition evaluates to false.
- 

A required defined tag is missing from a related resource.

Do not stop after you confirm that a resource exists. Confirm that the resource tags also satisfy the policy.

## Review Gateway Network Configuration

If the failed operation creates or updates a gateway, confirm that the gateway references the expected subnet and endpoint type.

Review the following request fields:
- 

`gateway.subnetId`
- 

`gateway.endpointType`

Verify the following network requirements:
- 

The subnet exists.
- 

The subnet is regional.
- 

The subnet is in the expected compartment.
- 

The endpoint type matches the intended public or private design.
- 

The caller is authorized to use the subnet and related network resources.

## Validate the Request Context

For an existing gateway, get the gateway details directly:
```

```

Use the response to verify the following values:
- 

The gateway exists.
- 

The gateway is in the expected compartment.
- 

The gateway uses the intended subnet.
- 

The gateway uses the expected endpoint type.

If the failed operation creates a deployment, verify that the request targets the intended gateway and compartment.

## Fix Policy and Resource Access

Apply the fix that matches the failed authorization or resource-access check.

Use the following fixes as a guide:
- 

Add or correct`manage api-gateway-family`if the caller lacks API Gateway resource permissions.
- 

Add or correct`manage virtual-network-family`if the caller lacks subnet or network permissions.
- 

Add or correct`use functions-family`if the deployment uses Functions.
- 

Add or correct`manage certificate-associations`if the gateway uses certificate associations.
- 

Add or correct`manage certificate-authority-family`if the gateway uses custom CAs or CA bundles.
- 

Create or correct the gateway dynamic group and`read secret-bundles`policy if the gateway must read secrets.
- 

Correct the compartment scope if a resource is outside the allowed compartment.
- 

Correct the tag values or the IAM condition if tag-based authorization fails.
- 

Correct any incorrect OCID in the request.

## Common Root-Cause Checklist

Before retrying the request, confirm all of the following:
- 

The caller can manage API Gateway resources.
- 

The caller can manage network resources.
- 

The caller has the feature-specific policy required by the request.
- 

Any gateway dynamic group has the secret access it needs.
- 

All referenced resources exist.
- 

All referenced resources are in the expected compartments.
- 

All tag-based conditions match.
- 

The request uses the correct OCIDs.

## Verify the Resolution

After you correct IAM policies, tag conditions, or related-resource access, retry the same gateway or deployment operation.

Verify the following results:
- 

The operation no longer returns`NotAuthorizedOrNotFound`or`RelatedResourceNotAuthorizedOrNotFound`.
- 

The gateway or deployment enters the expected lifecycle state.
-
