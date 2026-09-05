# Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm
- Fetched: 2026-09-05 01:39 CDT

# Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments

Find out how to use single-argument authorizer functions and access tokens to add authentication and authorization functionality to API gateways with the API Gateway service.

You can add authentication and authorization functionality to an API gateway by having the API gateway pass a multi-argument or single-argument access token included in a request to an authorizer function deployed on OCI Functions for validation (as described in this topic). Alternatively, you can have the API gateway itself validate the tokens included in a request (as described in[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)).

You can add authentication and authorization functionality to API gateways by writing an 'authorizer function' that:
- Processes request attributes to verify the identity of an API client with an identity provider.
- Determines the operations that the API client is allowed to perform.
- Returns the operations the API client is allowed to perform as a list of 'access scopes' (an 'access scope' is an arbitrary string used to determine access).
- Optionally returns a key-value pair for use by the API deployment. For example, as a context variable for use in an HTTP back end definition (see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)).

Depending on the functionality you require, you can write:
- (Recommended) A multi-argument authorizer function that accepts a user-defined, multi-argument access token comprising one or more elements of a request (see[Creating a Multi-Argument Authorizer Function (Recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Multiargument_Authorizer_Function)). Note that multi-argument authorizer functions can accept single access tokens contained in a request header or query parameter.
- A single-argument authorizer function that accepts a single-argument access token comprising a single value contained in a request header or query parameter in a request (see[Creating a Single-Argument Authorizer Function](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Single-Argument_Authorizer_Function)).

Using a multi-argument (rather than a single-argument) authorizer function enables an API gateway to perform finer-grained, request-based authentication. A multi-argument authorizer function can query decision services and policy agents with attributes from the access token and with other request elements such as query parameters, hostname, and subdomain.
Note  
  
Oracle recommends the use of multi-argument authorizer functions rather than single-argument authorizer functions because of their additional versatility. Single-argument authorizer functions were provided in earlier releases, and continue to be supported. However, since multi-argument authorizer functions can also accept single-argument access tokens contained in request headers and query parameter, there is no reason to create new single-argument authorizer functions. Furthermore, single-argument authorizer functions are planned for deprecation in a future release.

Having written the authorizer function, you can then deploy it to OCI Functions (see[Deploying an Authorizer Function](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Deploying_an_Authorizer_Function.htm)).

For a related Developer Tutorial containing an example single-argument authorizer function, see[Functions: Validate an API Key with API Gateway](https://docs.oracle.com/iaas/Content/developer/functions/func-api-gtw-token/01-summary.htm).

Having deployed the authorizer function, you enable authentication and authorization for an API deployment by including two different kinds of request policy in the API deployment specification:
- An authentication request policy for the entire API deployment that specifies:
- The OCID of the authorizer function that you deployed to OCI Functions that will perform authentication and authorization.
- The request attributes to pass to the authorizer function.
- Whether unauthenticated API clients can access routes in the API deployment.
- An authorization request policy for each route that specifies the operations an API client is allowed to perform, based on the API client's access scopes as returned by the authorizer function.

You can add authentication and authorization request policies to an API deployment specification by:
- Using the Console.
- Editing a JSON file.
Tip  
  

To help troubleshoot issues with the authorizer function, consider adding an execution log to the API deployment, with its log level set to Info (see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)).

To see details in the log files related to authentication and authorization, search for`customAuth`
