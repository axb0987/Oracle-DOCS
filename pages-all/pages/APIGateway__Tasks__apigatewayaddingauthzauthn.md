# Adding Authentication and Authorization to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Authentication and Authorization to API Deployments

Find out how to add authentication and authorization functionality to API gateways with the API Gateway service.

You can control access to APIs you deploy to API gateways based on the API client sending a request, and define what it is that they are allowed to do. For the APIs you deploy, you'll typically provide:
- Authentication functionality to determine an API client's identity. Is the API client really who they claim to be?
- Authorization functionality to determine appropriate access for an API client, and grant the necessary permissions. What is the API client allowed to do?

You can add authentication and authorization functionality to API gateways to support:
- HTTP Basic Authentication
- API Key Authentication
- OAuth Authentication and Authorization
- Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) with Identity Domains Authentication
- Oracle Identity Cloud Service (IDCS) Authentication

You can add authentication and authorization functionality to an API gateway as follows:
- You can have the API gateway pass a multi-argument or single-argument access token included in a request to an authorizer function deployed on OCI Functions to perform validation (see[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)).
- You can have the API gateway itself validate a JSON Web Token (JWT) included in the request with an identity provider (see[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)).

For convenience, these different types of authentication and authorization functionality are referred to as 'authentication servers'. You can set up multiple authentication servers for the same API deployment. The authentication servers you set up can be of the same type or a different type. Setting up multiple authentication servers for the same API deployment enables a request to be dynamically routed to the correct authentication server based on an element in the request. For more information, see[Adding Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm)
