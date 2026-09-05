# Adding Logout as an API Gateway Back End
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Logout as an API Gateway Back End

Find out how to define a logout back end with API Gateway.

A common requirement is for APIs to provide the facility for API clients to log out cleanly by revoking access tokens, and potentially call other URLs to perform additional post-logout tasks. API Gateway enables you to define logout back ends to provide such functionality when using an OAuth 2.0 token authentication policy for an API deployment. Requests to the logout back end can optionally include a post-logout URL as the value of a query parameter named`postLogoutUrl`.

When defining an OAuth 2.0 token authentication policy , you can optionally specify a path to the logout back end (the logout path) to revoke access tokens in the event of an authentication failure. See[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm).

The logout back end definition optionally includes:
- A list of allowed post-logout URLs to which a request can be redirected to revoke access tokens. If the`postLogoutUrl`query parameter is included in the request, its value must be one of these URLs. The URLs in the list can be absolute paths or relative paths, and the URLs can include context variables. Note that if you specify a relative path (that is, to another route in the API deployment), then both the API deployment and the route must allow anonymous access. Also note that if you don't explicitly include one or more URLs in the list, any post-logout URL is allowed.
- Data to pass to logout URLs when the request is redirected, as the value of the`state`query parameter. The data can only include context variables (not static values).

On receiving a request to the logout path from an API client, the API gateway checks that the API client is authenticated to call the logout back end, checks that any post-logout URL included in the request is allowed, and removes any stored information about the API client's session (for example, in cookies). Assuming the post-logout URL is allowed, what happens next depends on whether the API client is authenticated, and whether the previously cached response from the Discovery URL specified in the OAuth 2.0 token authentication policy provided an end session endpoint:
- If the API client is not authenticated, the API gateway redirects the logout request to the post-logout URL.
- If the API client is authenticated, but the OAuth 2.0 token authentication policy did not provide an end session endpoint, the API gateway redirects the logout request to the post-logout URL and passes any state information specified in the logout back end definition.
- If the API client is authenticated, and the OAuth 2.0 token authentication policy did provide an end session endpoint, the API gateway redirects the logout request to that end session endpoint and passes the post-logout URL, and any state information specified in the logout back end definition. In this case, it is the identity provider's responsibility to redirect the request to the post-logout URL.

You can add a logout back end to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Logout Back Ends to an API Deployment Specification

To add logout back ends to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

On the Authentication page, specify authentication options.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

On the Routes page, create a new route and specify:
- 

Path: A path for API calls using the listed methods to the back-end service. Note that the route path you specify:
- is relative to the deployment path prefix (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- Methods: One or more methods accepted by the back-end service. In the case of logout back ends, only`GET`is accepted.
- 

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different back ends according to the context variable and rules you enter.

These instructions assume you want to use a single back end, so select Add a single backend . Alternatively, if you want to use different back ends, select Add multiple backends and follow the instructions in[Using the Console to Add Dynamic Back End Selection to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm#apigatewaydynamicroutingbasedonrequest_topic-Using_the_Console_to_Add_Dynamic_Backend_Selection_to_an_API_Deployment_Specification).
- Backend Type: The type of the back-end service as`Logout`.
- Allowed post logout URIs: (optional) A list of one or more allowed URLs to which a logout request can be redirected to revoke tokens. The URLs in the list can be absolute paths or relative paths, and the URLs can include context variables. For example,`["https://${request.header[tenant-id].page.html}", "https://fixed-path.page.html", "/logout_html"`] .

Note the following:
- A post-logout URL can be included in a request to the logout back end as the value of a query parameter named`postLogoutUrl`.
- If you specify a relative path (that is, to another route in the API deployment), then both the API deployment and the route must allow anonymous access.
- If you don't explicitly include one or more URLs in the list, any post-logout URL is allowed.
- Post logout state: (optional) Data to pass when a logout request is redirected to an end session endpoint and/or a post-logout URL. The data can only include context variables (not static values). For example,`request.query[region]`

The data is passed as the value of the`state`query parameter.
- (Optional) Select Another URL to enter details of additional post-logout URLs.
- Select Create to create the route.
- (Optional) Select Add route to enter details of additional routes.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Logout Back Ends to an API Deployment Specification

To add logout back ends to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add a logout back end, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in Oracle Functions as a single back end:

```

```

- 

In the`routes`section, include a new section for a logout back end:

```

```

where:
- 

`<logout-route-path>`specifies a path for calls using the listed methods to the logout back end. Note that the route path you specify:
- is relative to the deployment path prefix (see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm))
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- 

can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- `<method-list>`specifies one or more methods accepted by the logout back end, separated by commas. In the case of logout back ends, only`GET`is accepted.
- `"type": "OAUTH2_LOGOUT"`specifies that the back end is a logout back end.
- 

`"allowedPostLogoutUris": ["<url>", "<url>"]`optionally specifies a list of one or more allowed URLs to which a logout request can be redirected to revoke tokens. The URLs in the list can be absolute paths or relative paths, and the URLs can include context variables. For example,`["https://${request.header[tenant-id].page.html}", "https://fixed-path.page.html", "/logout_html"`] .

Note the following:
- A post-logout URL can be included in a request to the logout back end as the value of a query parameter named`postLogoutUrl`.
- If you specify a relative path (that is, to another route in the API deployment), then both the API deployment and the route must allow anonymous access.
- If you don't explicitly include one or more URLs in the list, any post-logout URL is allowed.
- 

`"postLogoutState": "<logout-data>"`optionally specifies data to pass when a logout request is redirected to an end session endpoint and/or a post-logout URL. The data can only include context variables (not static values). For example,`request.query[region]`

The data is passed as the value of the`state`query parameter.

In this example, a request to the`/logout`back end can include one of the URLs specified for`allowedPostLogoutUris`as the value of the`postLogoutUrl`query parameter. When the post-logout URL is called, the value of the`request.query[region]`context variable is passed to the URL. Note that in this example, one of the`allowedPostLogoutUris`values (`"/logout_html"`) is a relative path to the`/logout_html`stock response back end in the same API deployment. Because it is a relative path to another route in the same API deployment, the`/logout_html`back end has to include an authorization policy of type`ANONYMOUS`, as shown here.

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
