# Adding Request Policies and Response Policies to API Deployment Specifications
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Request Policies and Response Policies to API Deployment Specifications

Find out how to control the behavior of API deployments by adding request and response policies to API specifications that you previously created with API Gateway.

You can control the behavior of an API deployment you create on an API gateway by adding request and response policies to the API deployment specification:
- a request policy describes actions to be performed on an incoming request from an API client before it is sent to a back end
- a response policy describes actions to be performed on a response returned from a back end before it is sent to an API client

You can use request policies and/or response policies to:
- limit the number of requests sent to back-end services
- enable CORS (Cross-Origin Resource Sharing) support
- provide authentication and authorization
- add mTLS support
- validate requests before sending them to back-end services
- modify incoming requests and outgoing responses
- cache responses to improve performance and reduce load on back-end services
- make API deployments eligible for inclusion in usage plans that monitor and manage subscriber access

You can add policies to an API deployment specification that apply globally to all routes in the API deployment specification, as well as policies that apply only to particular routes.

Note that API Gateway request policies and response policies are different to IAM policies, which control access to Oracle Cloud Infrastructure resources.

You can add request and response policies to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Request Policies and Response Policies

To add request policies and response policies to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API request policies section of the Basic information page, specify request policies that apply globally to all routes in the API deployment specification:
- Mutual-TLS: A policy to control access to APIs you deploy to API gateways based on the TLS certificate presented by the API client making a request. You can only apply an mTLS policy globally to all routes in the API deployment specification (not to individual routes). See[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).
- CORS: A policy to enable CORS support in the APIs you deploy to API gateways. You can also specify CORS policies that apply to individual routes in the API deployment specification (you don't need to have entered a global CORS policy first). See[Adding CORS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm).
- Rate Limiting: A policy to limit the rate at which API clients can make requests to back-end services. You can only apply a rate-limiting policy globally to all routes in the API deployment specification (not to individual routes). See[Limiting the Number of Requests to API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm).
- Usage plans: A policy to make an API deployment eligible for inclusion in a usage plan by specifying the location of a client token passed in a request. See[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm).
- 

Select Next to specify options to define a global authentication request policy on the Authentication page.

The authentication request policy controls access to the APIs you deploy to API gateways. Having specified a global authentication policy first, you can then specify authorization policies that apply to individual routes in the API deployment specification. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page.
- 

Select Add route and specify request policies that apply to an individual route by selecting Show route request policies and specify:
- Authorization: A policy to specify the operations an end user is allowed to perform, based on the end user's access scopes. Note that you must have already specified a global authentication policy before you can specify an authorization policy on an individual route. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- CORS: A policy to enable CORS support for individual routes in the API deployment specification (you don't need to have entered a global CORS policy first). See[Adding CORS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm).
- Header validations: A policy to validate headers in requests. See[Using the Console to Add Validation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestvalidation.htm#usingconsoletoaddrequestvalidationrequestpolicies).
- Query parameter validations: A policy to validate query parameters in requests. See[Using the Console to Add Validation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestvalidation.htm#usingconsoletoaddrequestvalidationrequestpolicies).
- Body validation: A policy to validate the content in the body of requests. See[Using the Console to Add Validation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestvalidation.htm#usingconsoletoaddrequestvalidationrequestpolicies)
- Header transformations: A policy to add, remove, and modify headers in requests. See[Adding Header Transformation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingheadertransformrequestpolicies.htm).
- Query parameter transformations: A policy to add, remove, and modify query parameters in requests. See[Adding Query Parameter Transformation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingqueryparamtransformrequestpolicies.htm).
- 

To specify response policies that apply to an individual route, select Show route response policies and specify:
- Header transformations: A policy to add, remove, and modify headers in responses. See[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Request Policies and Response Policies

To add request policies and response policies to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a request policy or response policy, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

At a minimum, the API deployment specification will include a`routes`section containing:
- A path. For example,`/hello`
- One or more methods. For example,`GET`
- A definition of a back end. For example, a URL, or the OCID of a function in OCI Functions.

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

To add a request policy that applies globally to all routes in the API deployment specification:
- 

Insert a`requestPolicies`section before the`routes`section. For example:

```

```

- 

Include a request policy in the`requestPolicies`section.

For example, to limit the number of requests sent to all routes in an API deployment specification, you'd include the`rateLimiting`policy in the`requestPolicies`section as follows:

```

```

For more information about the`rateLimiting`request policy, see[Limiting the Number of Requests to API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm).
- 

To add a request policy that applies to an individual route in the API deployment specification:
- 

Insert a`requestPolicies`section after the route's`backend`section. For example:

```

```

- 

Include a request policy in the`requestPolicies`section.

For example, to enable CORS support in an API deployment for a particular route, you'd include the`cors`policy in the`requestPolicies`section as follows:

```

```

For more information about the`cors`request policy, see[Adding CORS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm).
- 

To add a response policy that applies to an individual route in the API deployment specification:
- 

Insert a`responsePolicies`section after the route's`backend`section. For example:

```

```

- 

Include a response policy in the`responsePolicies`section.

For example, to rename any`X-Username`header to`X-User-ID`in the response from a particular route, you'd include the`headerTransformations`policy in the`responsePolicies`section as follows:

```

```

For more information about the`headerTransformations`response policy, see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)
