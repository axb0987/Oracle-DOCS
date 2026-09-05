# Limiting the Number of Requests to API Gateway Back Ends
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm
- Fetched: 2026-09-05 01:38 CDT

# Limiting the Number of Requests to API Gateway Back Ends

Find out how to use a request policy to limit the number of requests sent to back-end services with API Gateway.

Having created an API gateway and deployed one or more APIs on it, you'll typically want to limit the rate at which API clients can make requests to back-end services. For example, to:
- maintain high availability and fair use of resources by protecting back ends from being overwhelmed by too many requests
- prevent denial-of-service attacks
- constrain costs of resource consumption
- restrict usage of APIs by your customers' users in order to monetize APIs

You apply a rate limit globally to all routes in an API deployment specification.

If a request is denied because the rate limit has been exceeded, the response header specifies when the request can be retried.

You use a request policy to limit the number of requests (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).

You can add a rate-limiting request policy to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Rate-Limiting Request Policies

To add a rate-limiting request policy to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API request policies section of the Basic information page, select the Add button beside Rate Limiting and specify:
- Number of requests per second: The maximum number of requests per second to send to the API deployment.
- Type of rate limit: How the maximum number of requests per second threshold is applied:
- Select Total as the rate key to specify that the maximum applies to the total number of requests sent from all API clients.
- Select Per client (IP) as the rate key to specify that the maximum applies to the number of requests sent from an API client (identified by its IP address). For IPv4 clients, rate limiting is based on individual API client IPv4 addresses. For IPv6 clients, rate limiting is based on the API client’s IPv6 /64 prefix rather than the full address. API clients that have the same IPv6 /64 prefix are considered to be the same client, for rate limiting purposes.
- 

Select Update .
- 

Select Next and specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page. Note that you cannot apply rate-limiting policies to individual routes in the API deployment specification.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Rate-Limiting Request Policies

To add a rate-limiting request policy to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a request limit, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Insert a`requestPolicies`section before the`routes`section, if one doesn't exist already. For example:

```

```

- 

Add the following`rateLimiting`policy to the new`requestPolicies`section to apply to all routes defined in the specification:

```

```

where:
- `<ratekey-value>`specifies how the maximum number of requests per second threshold is applied:
- Use`TOTAL`as the rate key to specify that the maximum applies to the total number of requests sent from all API clients.
- Use`CLIENT_IP`as the rate key to specify that the maximum applies to the number of requests sent from an API client (identified by its IP address). For IPv4 clients, rate limiting is based on individual API client IPv4 addresses. For IPv6 clients, rate limiting is based on the API client’s IPv6 /64 prefix rather than the full address. API clients that have the same IPv6 /64 prefix are considered to be the same client, for rate limiting purposes.
- `<requests-per-second>`is the maximum number of requests per second to send to the API deployment.

For example:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
