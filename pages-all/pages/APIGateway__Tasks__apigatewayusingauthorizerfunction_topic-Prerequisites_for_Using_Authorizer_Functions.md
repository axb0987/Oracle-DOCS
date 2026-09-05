# Prerequisites for Using Authorizer Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Prerequisites_for_Using_Authorizer_Functions.htm
- Fetched: 2026-09-05 01:39 CDT

# Prerequisites for Using Authorizer Functions

Find out about the prerequisites for using authorizer functions with API Gateway.

Before you can enable authentication and authorization for API deployments using authorizer functions:
- An identity provider must have already been set up, containing access scopes for API clients allowed to access the API deployment. API Gateway supports the use of any OAuth2-compliant identity provider, such as OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), and Auth0. See the identity provider documentation for more information (for example, the[OCI IAM with Identity Domains documentation](https://docs.oracle.com/iaas/Content/Identity/applications/overview.htm), the[Oracle Identity Cloud Service (IDCS) documentation](https://docs.oracle.com/en/cloud/paas/identity-cloud/index.html), the[Auth0 documentation](https://auth0.com/docs/getting-started)).
- An authorizer function must have been deployed to OCI Functions already, and an appropriate policy must give API gateways access to OCI Functions. For more information, see[Creating an Authorizer Function](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm).

If you use the Console to include an authentication request policy (rather than by editing a JSON file), you select the authorizer function and the application that contains it from a list.

Note that to use the Console (rather than a JSON file) to define an authentication request policy and specify an authorizer function, your user account must belong to a group that has been given access to the authorizer function by an IAM policy (see[Create a Policy to Give API Gateway Users Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersfunctionspolicy)
