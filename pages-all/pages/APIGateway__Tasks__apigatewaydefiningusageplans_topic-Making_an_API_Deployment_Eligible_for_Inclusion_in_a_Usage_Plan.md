# Making an API Deployment Eligible for Inclusion in a Usage Plan
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm
- Fetched: 2026-09-05 01:38 CDT

# Making an API Deployment Eligible for Inclusion in a Usage Plan

Find out how to use a request policy to make an API deployment eligible for inclusion in a usage plan with API Gateway.

As an API plan manager, you can monitor and manage API access and set up access tiers by creating usage plans and subscribers. See[Usage Plans and Entitlements, Subscribers, and Client Tokens](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayconcepts.htm#Usage_plans_and_entitlements_subscribers_and_client_tokens).

To make an API deployment eligible for inclusion in a usage plan, you have to specify the location of a client token passed in a request to an API gateway. Once the API deployment has been included in a usage plan, requests from subscribed API clients must include the client token in this location in order to access the API deployment. You specify the client token location in a global usage plan request policy for all routes in an API deployment specification (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)).
You can specify that a client token is in one of the following locations:
- an authentication parameter returned by an authorizer function or contained in a JWT token
- a request header
- a query parameter in the request
- a path parameter in the request
- the`Host`header field in the request

The API gateway only forwards a request to the API deployment if the value of the client token in the location you specify matches the client token of one of the subscribers to a usage plan that includes the API deployment.

You specify the client token's location by setting the Token location property of the API deployment's usage plan request policy. You specify the Token location property in the format`<context-table-name>[<client-token-location-name>]`, where:
- `<context-table-name>`is one of`request.auth`,`request.headers`,`request.query`,`request.path`, or`request.host`
- `<client-token-location-name>`is a name of your choice for the client token location (for example,`client-id`,`client-token`,`my-token`).

For example,`request.headers[client-id]`specifies the client token must be in the`client-id`request header.

You have to set the Token location property of an API deployment's usage plan request policy before you can create usage plans and subscribers to access the API deployment.

When setting the Token location property, the client token location you specify determines both:
- how API clients must pass the client token when making the request (for example, as a header, as a query parameter)
- the context table from which the API gateway handling the request retrieves the value of the client token (for example, from the`request.query`table, from the`request.headers`table).

If you want API clients to pass the client token as: Set Token location property of usage plan request policy to: Example
authentication parameter returned by an authorizer function or contained in a JSON Web Token (JWT)`request.auth[<authentication-parameter-name>]``request.auth[a-token-name]`
header`request.headers[<header-name>]``request.headers[client-id]`
query parameter`request.query[<query-parameter-name>]``request.query[client-token]`
path parameter`request.path[<path-parameter-name>]``request.path[my-token]`
the name of a host to which the request was sent (extracted from the`Host`header field in the request)`request.host``request.host`

Note the following:
- For a given usage plan, you can only specify one client token location.
- The Token location property does not have a default value. To make an API deployment eligible for inclusion in a usage plan, you must explicitly set the Token location property to specify the location of the client token.
- If you want API clients to pass the client token as a path parameter, you also have to include the`<path-parameter-name>`in the corresponding segment of a route path in the API deployment specification. You must enclose the`<path-parameter-name>`within curly brackets. For example, if you set the Token location property to`request.path[my-token]`, you might include`{my-token}`in an API deployment specification as follows:

```

```

You can set the Token location property of the API deployment's usage plan request policy by:
- using the Console
- editing a JSON file

## Using the Console to Make an API Deployment Eligible for Inclusion in a Usage Plan

To make an API deployment eligible for inclusion in a usage plan, you have to specify the location of a client token passed in a request. To specify the location for the client token by adding a usage plan request policy to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API request policies section of the Basic information page, select the Add button for Usage plans and specify:
- Token location: The location of a client token that subscribed API clients must include in their requests in the format`<context-table-name>[<client-token-location-name>]`, where:
- `<context-table-name>`is one of`request.path`,`request.query`,`request.headers`,`request.auth`or`request.host`, depending on how you want API clients to pass the client token when making requests.
- `<client-token-location-name>`is a name of your choice for the client token location (for example,`client-id`,`client-token`,`my-token`). Not applicable for`request.host`.

For example,`request.headers[client-id]`
- 

Select Update , and then select Next to enter details for individual routes in the API deployment on the Routes page. Note that you cannot apply usage plan request policies to individual routes in the API deployment specification.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Make an API Deployment Eligible for Inclusion in a Usage Plan

To make an API deployment eligible for inclusion in a usage plan, you have to specify the location of a client token passed in a request. To specify the location for the client token by adding a usage plan request policy to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a usage plan request policy, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Insert a`requestPolicies`section before the`routes`section, if one doesn't exist already. For example:

```

```

- 

Add the following`usagePlans`policy to the new`requestPolicies`section to apply to all routes defined in the specification:

```

```

where:
- `<context-table-name>`is one of`request.path`,`request.query`,`request.headers`,`request.auth`, or`request.host`, depending on how you want API clients to pass the client token when making requests.
- `<client-token-location-name>`is a name of your choice for the client token location (for example,`client-id`,`client-token`,`my-token`). Not applicable for`request.host`.

Note that for any given usage plan, you can only specify one client token location.

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
