# Adding Login as an API Gateway Back End
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Login as an API Gateway Back End

Find out how to define an OAuth 2.0 login back end with API Gateway.

You can use an OAuth 2.0 login back end to define a static login redirect path for authentication flows that use OpenID Connect. The login back end is used with an OAuth 2.0 validation failure policy in a token authentication request policy.

When an API client sends a request to a route that requires authentication and the request does not include a valid session, API Gateway redirects the API client to the configured identity provider. By default, the redirect URI is based on the URL that the API client originally requested. However, for applications with many routes, path parameters, or wildcard routes, it can be difficult or impractical to register every possible redirect URI with the identity provider.

To avoid registering many redirect URIs, you can configure a static login redirect path, such as`/auth/callback`. You then add a route with the same path to the API deployment specification, and configure that route to use an OAuth 2.0 login back end. The full callback URL, including the API gateway hostname, deployment path prefix, and static login redirect path, must also be configured as a valid redirect URL in the identity provider.

When defining an OAuth 2.0 token authentication policy, you can optionally specify a static login redirect path in the validation failure policy. The static login redirect path identifies the route to which the identity provider redirects API clients as part of the authentication flow. See[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm).

After the API client signs in, the identity provider redirects the API client to the static login redirect path as part of the authentication flow. API Gateway establishes a session and redirects the API client back to the route that the API client originally requested.

The route that uses the OAuth 2.0 login back end is reserved for redirects from the identity provider. The route is not intended to be called directly by API clients (calling the route directly results in a`400 Bad Request`error).

The route must:
- have a path that matches the static login redirect path configured in the OAuth 2.0 validation failure policy
- use the OAuth 2.0 login back end
- support the`GET`method
- use a static path, without path parameters or wildcards

You can add a login back end to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Login Back Ends to an API Deployment Specification

To add login back ends to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

On the Authentication page, specify authentication options:
- Configure a token authentication request policy and select OAuth 2.0 introspection endpoint from the Validation Type list.
- Configure a validation failure policy and select OAuth2.0 redirect client to identity provider .
- For Login path , specify a static login redirect path, such as`/auth/callback`.

The static login redirect path must be relative to the deployment path prefix. For example, if the deployment path prefix is`/apex`and the static login redirect path is`/auth/callback`, the full callback path is`/apex/auth/callback`.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)and[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm).
- 

On the Routes page, create a new route and specify:
- 

Path : The static login redirect path that you specified in the OAuth 2.0 validation failure policy. Note that the route path you specify:
- is relative to the deployment path prefix
- must be preceded by a forward slash (`/`)
- can contain multiple forward slashes, provided they are not adjacent
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! ' ( ) , % ; : @ & =`
- must not include path parameters or wildcards

Note that the rules for login back end route paths are different from the rules for logout back end route paths.
- 

Methods : One or more methods accepted by the back end. In the case of login back ends, only`GET`is accepted.
- 

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different back ends.

These instructions assume you want to use a single back end, so select Add a single backend . Alternatively, if you want to use different back ends, select Add multiple backends .
- 

Backend Type : The type of the back-end service as Login .
- 

Select Create to create the route.
- 

Select Next to review the details you entered for the API deployment.
- 

Select Create or Update to create or update the API deployment.
- 

Configure the identity provider to include the full callback URL as a valid redirect URL.

The full callback URL includes the API gateway hostname, deployment path prefix, and static login redirect path. For example:

`https://<gateway-hostname>/<deployment-path-prefix>/auth/callback`

Note that if the deployment path prefix is simply`/`and the static login redirect path is`/auth/callback`, the full callback URL is`https://<gateway-hostname>/auth/callback`(and not`https://<gateway-hostname>//auth/callback`).
- 

Optionally, confirm the API has been deployed successfully by calling it.

## Editing a JSON File to Add Login Back Ends to an API Deployment Specification

To add login back ends to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a login back end, or create a new API deployment specification.

For example, the following basic API deployment specification defines a simple Hello World serverless function in Oracle Functions as a single back end:
```

```

- 

In the`routes`section, include a new section for a login back end:
```

```

where:
- 

`<login-route-path>`specifies the path for redirects from the identity provider to the login back end. The path must match the static login redirect path configured in the OAuth 2.0 validation failure policy. Note that the route path you specify:
- is relative to the deployment path prefix
- must be preceded by a forward slash (`/`)
- can contain multiple forward slashes, provided they are not adjacent
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! ' ( ) , % ; : @ & =`
- must not include path parameters or wildcards

Note that the rules for login back end route paths are different from the rules for logout back end route paths.
- 

`<method-list>`specifies one or more methods accepted by the login back end, separated by commas. In the case of login back ends, only`GET`is accepted.
- 

`"type": "OAUTH2_LOGIN_BACKEND"`specifies that the back end is a login back end.
- 

Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

Configure the identity provider to include the full callback URL as a valid redirect URL.

The full callback URL includes the API gateway hostname, deployment path prefix, and static login redirect path. For example:

`https://<gateway-hostname>/<deployment-path-prefix>/auth/callback`

Note that if the deployment path prefix is simply`/`and the static login redirect path is`/auth/callback`, the full callback URL is`https://<gateway-hostname>/auth/callback`(and not`https://<gateway-hostname>//auth/callback`).
- 

(Optional) Confirm the API has been deployed successfully by calling it. See[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
